# python -m PyInstaller --onefile --windowed --icon=SIGMA_ICON.ico --add-data "SIGMA_ICON.svg;." --name "Sigma Controls - IntelliScan Updater" --exclude-module matplotlib --exclude-module numpy --exclude-module pandas --exclude-module pyqtgraph --exclude-module pymodbus --exclude-module mplcursors --exclude-module scipy --exclude-module sklearn --exclude-module tensorflow --exclude-module torch --exclude-module torchvision --exclude-module torchaudio --exclude-module jupyter --exclude-module jupyterlab --exclude-module PyQt6 --clean --noconfirm updater.py

import json
import re
import requests
import os
import sys
import tempfile
import zipfile
import shutil
import subprocess
import time

# ruff: noqa: E402,F403,F405,F541,E722,F841,F401,E702, E741

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

LATEST_JSON = "https://snehshah-tech-2004.github.io/Sigma-Controls-IntelliScan/latest.json"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_current_version():
    try:
        with open("version.json", "r") as f:
            return json.load(f)["version"]
    except Exception:
        return "0.0.0"

def get_latest_release():
    try:
        r = requests.get(LATEST_JSON, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Update check failed:", e)
        return None

def is_newer(current, latest):
    c = tuple(map(int, current.split(".")))
    l = tuple(map(int, latest.split(".")))
    return l > c


# ----------------------------------------------------
# 1. Update Worker Thread (Handles Download & Extract)
# ----------------------------------------------------
class UpdateWorker(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal(bool, str)

    # ---> ADD latest_version HERE <---
    def __init__(self, download_url, latest_version):
        super().__init__()
        self.download_url = download_url
        self.latest_version = latest_version

    def run(self):
        try:
            app_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
            temp_dir = tempfile.mkdtemp()
            zip_path = os.path.join(temp_dir, "update.zip")
            
            # --- STEP 1: Download ---
            self.status.emit("Downloading update package...")
            response = requests.get(self.download_url, stream=True, timeout=15)
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))
            
            downloaded = 0
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            prog = int((downloaded / total_size) * 40) 
                            self.progress.emit(prog)
            
            # --- STEP 2: Extract ---
            self.status.emit("Extracting files...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                total_files = len(zip_ref.infolist())
                for i, member in enumerate(zip_ref.infolist()):
                    self.status.emit(f"Extracting: {member.filename[:35]}...")
                    zip_ref.extract(member, temp_dir)
                    
                    prog = 40 + int(((i + 1) / total_files) * 20)
                    self.progress.emit(prog)

            os.remove(zip_path)
            
            update_root = temp_dir
            extracted_items = os.listdir(temp_dir)
            if len(extracted_items) == 1:
                single_item = os.path.join(temp_dir, extracted_items[0])
                if os.path.isdir(single_item):
                    update_root = single_item
            
            # --- STEP 3: Kill Main App to Release File Locks ---
            self.status.emit("Closing background processes...")
            
            exe_names = [
                f for f in os.listdir(app_dir) 
                if f.endswith('.exe') and "updater" not in f.lower()
            ]
            
            for exe in exe_names:
                subprocess.run(["taskkill", "/F", "/IM", exe], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            time.sleep(1.5) 

            # --- STEP 4: Install & Overwrite ---
            exclusions = [
                "scanner files", "scanner_files", 
                "scanner db", "scanner_db", 
                "config.json", "credentials.json"
            ]
            
            items = os.listdir(update_root)
            total_items = len(items)
            
            for idx, item in enumerate(items):
                src_path = os.path.join(update_root, item)
                dst_path = os.path.join(app_dir, item)
                
                if item.lower() in exclusions and os.path.exists(dst_path):
                    continue
                
                self.status.emit(f"Installing: {item[:35]}...")
                
                if os.path.isdir(src_path):
                    self.copy_tree_overwrite(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
                    
                self.progress.emit(60 + int(((idx + 1) / total_items) * 35))

            # --- STEP 4b: Remove stale old-version main-app exe ---
            # Only "Sigma Controls - IntelliScan vX.Y[...].exe" is ever
            # version-suffixed and thus at risk of leaving a stale duplicate
            # behind (see explanation in previous comment). Any other .exe
            # sitting in app_dir (license installer, master generator, etc.)
            # must never be touched by this cleanup.
            self.status.emit("Removing old version files...")
            main_app_exe_pattern = re.compile(
                r"^Sigma Controls - IntelliScan v\d+(\.\d+)*\.exe$", re.IGNORECASE
            )
            for old_exe in exe_names:
                if not main_app_exe_pattern.match(old_exe):
                    continue
                if old_exe not in items:
                    old_exe_path = os.path.join(app_dir, old_exe)
                    if os.path.exists(old_exe_path):
                        try:
                            os.remove(old_exe_path)
                        except Exception as cleanup_err:
                            print(f"Could not remove old exe {old_exe}: {cleanup_err}")

            # ---> NEW STEP 5: FORCE UPDATE VERSION.JSON <---
            self.status.emit("Finalizing version verification...")
            version_file = os.path.join(app_dir, "version.json")
            with open(version_file, "w") as f:
                json.dump({"version": self.latest_version}, f, indent=4)
                
            # --- STEP 6: Cleanup ---
            self.status.emit("Cleaning up temporary files...")
            shutil.rmtree(temp_dir)
            
            self.progress.emit(100)
            self.finished.emit(True, "Update installed successfully!")
            
        except PermissionError:
            self.finished.emit(False, "Permission Error: Files are locked. Please close the main app manually.")
        except Exception as e:
            self.finished.emit(False, f"Error during update: {str(e)}")

    def copy_tree_overwrite(self, src, dst):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            
            self.status.emit(f"Writing: {item[:35]}...")
            
            if os.path.isdir(s):
                self.copy_tree_overwrite(s, d)
            else:
                shutil.copy2(s, d)


# ----------------------------------------------------
# 2. Progress Dialog UI
# ----------------------------------------------------
class DownloadDialog(QDialog):
    def __init__(self, download_url, latest_version, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sigma Controls | Updating...")
        self.setFixedSize(450, 220)
        self.setWindowIcon(QIcon(resource_path("SIGMA_ICON.svg")))
        
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        self.setStyleSheet("""
        QDialog { background:#1b1b1b; color:white; font-family: "Segoe UI"; }
        QLabel { color:white; font-family: "Segoe UI"; font-size: 15px; }
        
        QProgressBar {
            border: 1px solid #555;
            border-radius: 8px;
            background-color: #2d2d2d;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 14px;
        }
        QProgressBar::chunk {
            background-color: #00A0E3;
            border-radius: 7px;
        }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)

        self.title_lbl = QLabel("Downloading Update...")
        self.title_lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #00A0E3;")
        self.title_lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_lbl)

        self.status_lbl = QLabel("Initializing connection...")
        self.status_lbl.setAlignment(Qt.AlignCenter)
        self.status_lbl.setStyleSheet("color: #b5b5b5; font-size: 14px;")
        layout.addWidget(self.status_lbl)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(30)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        layout.addSpacing(10)

        # Worker initialization with the new version parameter
        self.worker = UpdateWorker(download_url, latest_version)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.status.connect(self.status_lbl.setText)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_finished(self, success, message):
        self.progress_bar.setValue(100 if success else 0)
        self.status_lbl.setText(message)
        
        if success:
            msg = QMessageBox(self)
            msg.setWindowTitle("Sigma Controls | Update Complete")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Download and extraction completed successfully!\n\nPlease restart your PC or launch the software to take updates.")
            msg.setStyleSheet("QMessageBox { background:#1b1b1b; font-family: 'Segoe UI'; font-size: 14px; } QLabel { color: white; background: transparent; } QPushButton { background:#00c853; color:white; font-weight: bold; padding: 6px 14px; border-radius: 6px; border:none; } QPushButton:hover { background:#00e676; }")
            msg.exec_()
            sys.exit(0)
        else:
            self.title_lbl.setText("Update Failed")
            self.title_lbl.setStyleSheet("font-size: 20px; font-weight: bold; color: #ff4c4c;")
            self.progress_bar.setStyleSheet("QProgressBar::chunk { background-color: #ff4c4c; }")
            
            msg = QMessageBox(self)
            msg.setWindowTitle("Sigma Controls | Update Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText(message)
            msg.setStyleSheet("QMessageBox { background:#1b1b1b; font-family: 'Segoe UI'; font-size: 14px; } QLabel { color: white; background: transparent; } QPushButton { background:#ff4c4c; color:white; font-weight: bold; padding: 6px 14px; border-radius: 6px; border:none; } QPushButton:hover { background:#e53935; }")
            msg.exec_()
            sys.exit(1)

# ----------------------------------------------------
# 3. Initial Update Prompt Dialog
# ----------------------------------------------------
class UpdateDialog(QDialog):
    def __init__(self, current_ver, latest_ver, release_notes, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sigma Controls | Software Update")
        self.setFixedSize(550, 520)
        self.setWindowIcon(QIcon(resource_path("SIGMA_ICON.svg")))

        self.setStyleSheet("""
        QDialog { background:#1b1b1b; color:white; font-family: "Segoe UI"; }
        QLabel { color:white; font-family: "Segoe UI"; background:transparent; }
        QTextEdit { background:#2d2d2d; border:1px solid #555; border-radius:8px; color:#d0d0d0; padding:12px; font-family: "Segoe UI"; font-size: 14px; }
        QPushButton { border:none; border-radius:8px; min-height:42px; font-family: "Segoe UI"; font-size: 15px; font-weight:bold; color: white; }
        QPushButton#updateBtn { background:#00c853; }
        QPushButton#updateBtn:hover { background:#00e676; }
        QPushButton#laterBtn { background:#3a3a3a; border: 1px solid #555; }
        QPushButton#laterBtn:hover { background:#4a4a4a; }
        QFrame#versionBox { background: #252525; border: 1px solid #444; border-radius: 8px; }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 35, 40, 30)
        layout.setSpacing(10)

        title = QLabel("🚀 Update Available")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color:#00A0E3; font-size:26px; font-weight:bold; padding-bottom:5px;")
        layout.addWidget(title)

        subtitle = QLabel("A newer version of IntelliScan is ready to install.")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color:#b5b5b5; font-size:15px; font-weight:normal;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(20)

        version_layout = QHBoxLayout()
        version_layout.setSpacing(20)

        current_frame = QFrame(); current_frame.setObjectName("versionBox")
        c_layout = QVBoxLayout(current_frame); c_layout.setContentsMargins(15, 15, 15, 15); c_layout.setSpacing(5)
        c_title = QLabel("Current Version"); c_title.setAlignment(Qt.AlignCenter); c_title.setStyleSheet("color:#888; font-size:13px; font-weight:bold;")
        c_val = QLabel(current_ver); c_val.setAlignment(Qt.AlignCenter); c_val.setStyleSheet("color:#ff4c4c; font-size:18px; font-weight:bold;") 
        c_layout.addWidget(c_title); c_layout.addWidget(c_val)

        latest_frame = QFrame(); latest_frame.setObjectName("versionBox")
        l_layout = QVBoxLayout(latest_frame); l_layout.setContentsMargins(15, 15, 15, 15); l_layout.setSpacing(5)
        l_title = QLabel("Latest Version"); l_title.setAlignment(Qt.AlignCenter); l_title.setStyleSheet("color:#888; font-size:13px; font-weight:bold;")
        l_val = QLabel(latest_ver); l_val.setAlignment(Qt.AlignCenter); l_val.setStyleSheet("color:#00ff66; font-size:18px; font-weight:bold;") 
        l_layout.addWidget(l_title); l_layout.addWidget(l_val)

        version_layout.addWidget(current_frame)
        version_layout.addWidget(latest_frame)
        layout.addLayout(version_layout)

        layout.addSpacing(20)

        notes_lbl = QLabel("📋 Release Notes:")
        notes_lbl.setStyleSheet("font-size: 15px; font-weight: bold;")
        layout.addWidget(notes_lbl)

        notes_box = QTextEdit()
        notes_box.setReadOnly(True)
        notes_box.setPlainText(release_notes)
        layout.addWidget(notes_box)

        layout.addSpacing(25)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)

        later_btn = QPushButton("Remind Me Later")
        later_btn.setObjectName("laterBtn")
        later_btn.clicked.connect(self.reject) 

        update_btn = QPushButton("⬇️ Download and Update")
        update_btn.setObjectName("updateBtn")
        update_btn.clicked.connect(self.accept) 

        btn_layout.addWidget(later_btn)
        btn_layout.addWidget(update_btn)

        layout.addLayout(btn_layout)


def check_for_updates(parent=None):
    current = get_current_version()
    
    # 0.0.0 Error Check
    if current == "0.0.0":
        msg = QMessageBox()
        msg.setWindowTitle("Sigma Controls | Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowIcon(QIcon(resource_path("SIGMA_ICON.svg")))
        msg.setText("Version 0.0.0 detected.\n\nUpdates are disabled for unverified installations.")
        msg.setStyleSheet("QMessageBox { background:#1b1b1b; font-family: 'Segoe UI'; font-size: 14px; } QLabel { color: white; background: transparent; } QPushButton { background:#ff4c4c; font-weight: bold; color:white; padding: 6px 14px; border-radius: 6px; border:none; } QPushButton:hover { background:#e53935; }")
        msg.exec_()
        sys.exit(1)

    latest = get_latest_release()
    
    if latest is None:
        return
        
    if is_newer(current, latest["version"]):
        dialog = UpdateDialog(current, latest["version"], latest["release_notes"], parent)
        
        if dialog.exec_() == QDialog.Accepted:
            url = latest.get(
                "download_url", 
                f"https://github.com/snehshah-tech-2004/Sigma-Controls-IntelliScan/releases/download/v1.2/Sigma.Controls.-.IntelliScan.v1.2.zip"
            )
            download_ui = DownloadDialog(url, latest["version"], parent)
            download_ui.exec_()
        else:
            print("Update postponed by user.")
            sys.exit(0) # Ensure updater closes silently so main_3 unblurs
    else:
        print("Already Latest")
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    check_for_updates()