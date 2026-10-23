# python -m PyInstaller --onefile --windowed --uac-admin --icon=SIGMA_ICON.ico --add-data "SIGMA_ICON.svg;." --name "Sigma Controls License Installer" --exclude-module matplotlib --exclude-module numpy --exclude-module pandas --exclude-module pyqtgraph --exclude-module pymodbus --exclude-module mplcursors --exclude-module scipy --exclude-module sklearn --exclude-module tensorflow --exclude-module torch --exclude-module torchvision --exclude-module torchaudio --exclude-module jupyter --exclude-module jupyterlab --exclude-module PyQt6 --clean --noconfirm fingerprint.py
# # # ruff: noqa: E402,F403,F405,F541,E722,F841

import subprocess
import hashlib
import winreg
from PyQt5.QtWidgets import (
    QApplication,
    QMessageBox,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------- UPDATED REGISTRY PATHS ----------------
REG_PATH = r"SOFTWARE\Sigma_Controls_IntelliScan\Fingerprint"
VALUE_NAME = "Sigma_Controls_IntelliScan_License_Key"
VERSION_VALUE_NAME = "Sigma_Controls_IntelliScan_Version_Key"
CUSTOMER_VALUE_NAME = "Sigma_Controls_IntelliScan_Customer"
# --------------------------------------------------------

def get_motherboard_uuid():
    try:
        result = subprocess.check_output("wmic csproduct get uuid", shell=True).decode(errors="ignore")
        lines = [x.strip() for x in result.splitlines() if x.strip()]
        return lines[1]
    except:
        return ""

def get_disk_serial():
    try:
        result = subprocess.check_output("wmic diskdrive get serialnumber", shell=True).decode(errors="ignore")
        lines = [x.strip() for x in result.splitlines() if x.strip()]
        return lines[1]
    except:
        return ""

def get_machine_hash():
    uuid = get_motherboard_uuid()
    disk = get_disk_serial()
    raw = f"{uuid}|{disk}"
    return hashlib.sha256(raw.encode()).hexdigest()

def get_machine_id():
    machine_hash = get_machine_hash()
    return (
        machine_hash[:4] + "-" + machine_hash[4:8] + "-" + 
        machine_hash[8:12] + "-" + machine_hash[12:16]
    ).upper()

class ActivationWindow(QWidget):
    SECRET = "SC_7YkP1592mQa_4LShahxZ_2026_Sigma_Controls_88RSneh"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sigma Controls | License Activation")
        self.resize(700, 780)
        self.setMinimumSize(700, 780)
        self.setWindowIcon(QIcon(resource_path("SIGMA_ICON.svg")))

        self.setStyleSheet("""
        QWidget { background:#1b1b1b; color:white; font-family: "Segoe UI"; font-size: 14px; }
        QLabel { color:white; font-family: "Segoe UI"; font-size: 14px; font-weight:600; background:transparent; }
        QLineEdit { background:#2d2d2d; border:1px solid #555; border-radius:8px; color:white; padding:10px 14px; min-height:42px; font-family: "Segoe UI"; font-size: 15px; }
        QLineEdit:focus { border:2px solid #00A0E3; }
        QPushButton { background:#2d8cff; color:white; border:none; border-radius:8px; min-height:46px; font-family: "Segoe UI"; font-size: 15px; font-weight:bold; }
        QPushButton:hover { background:#1976d2; }
        QPushButton:pressed { background:#0d5db8; }
        QPushButton#copyBtn { background: #3a3a3a; border: 1px solid #555; min-width: 120px; }
        QPushButton#copyBtn:hover { background: #4a4a4a; }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 45, 50, 45)
        layout.setSpacing(8)

        title = QLabel("License Activation")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color:#00A0E3; font-size:28px; font-weight:bold; padding-bottom:5px;")
        layout.addWidget(title)

        subtitle = QLabel("Enter your details and keys to activate the software.")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color:#b5b5b5; font-size:15px; font-weight:normal;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(35) 

        lbl = QLabel("💻  Machine ID")
        lbl.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(lbl)

        machine_id = get_machine_id()
        id_layout = QHBoxLayout()
        self.machine_label = QLineEdit(machine_id)
        self.machine_label.setReadOnly(True)
        self.machine_label.setStyleSheet("color:#00ff66; font-family: Consolas; font-size: 18px; font-weight: bold;")
        
        copy_btn = QPushButton("📋 Copy")
        copy_btn.setObjectName("copyBtn")
        copy_btn.clicked.connect(self.copy_machine_id)
        
        id_layout.addWidget(self.machine_label)
        id_layout.addWidget(copy_btn)
        layout.addLayout(id_layout)

        layout.addSpacing(25) 

        lbl = QLabel("👤  Customer Name")
        lbl.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(lbl)

        self.customer_box = QLineEdit()
        self.customer_box.setPlaceholderText("Enter Customer Name")
        layout.addWidget(self.customer_box)

        layout.addSpacing(25) 

        lbl = QLabel("🔑  License Key")
        lbl.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(lbl)

        self.key_box = QLineEdit()
        self.key_box.setPlaceholderText("XXXX-XXXX-XXXX-XXXX")
        self.key_box.setStyleSheet("font-family: Consolas; font-size: 16px; text-transform: uppercase;")
        layout.addWidget(self.key_box)
        
        layout.addSpacing(25) 

        lbl = QLabel("⚙️  Version Key")
        lbl.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(lbl)

        self.version_box = QLineEdit()
        self.version_box.setPlaceholderText("XXXX-XXXX-XXXX-XXXX")
        self.version_box.setStyleSheet("font-family: Consolas; font-size: 16px; text-transform: uppercase;")
        layout.addWidget(self.version_box)

        layout.addSpacing(40) 

        activate_btn = QPushButton("✅  Verify and Activate Software")
        activate_btn.setStyleSheet("background-color: #00c853;") 
        activate_btn.clicked.connect(self.activate)
        layout.addWidget(activate_btn)

        layout.addStretch()

    def copy_machine_id(self):
        machine_id = self.machine_label.text().strip()
        QApplication.clipboard().setText(machine_id)
        QMessageBox.information(self, "Copied", "Machine ID copied to clipboard.")

    def activate(self):
        machine_id = self.machine_label.text().strip().upper()
        customer_name = self.customer_box.text().strip().upper()
        entered_key = self.key_box.text().strip().upper()
        version_key = self.version_box.text().strip().upper()

        if not customer_name or not entered_key or not version_key:
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        expected_hash = hashlib.sha256((machine_id + customer_name + self.SECRET).encode()).hexdigest()
        expected_key = (
            expected_hash[:4] + "-" + expected_hash[4:8] + "-" + 
            expected_hash[8:12] + "-" + expected_hash[12:16]
        ).upper()

        if entered_key != expected_key:
            QMessageBox.critical(self, "Activation Failed", "Invalid License Key.")
            return

        # Pass customer_name alongside version_key so the registry remembers it
        write_registry(version_key, customer_name)
        self.close()

def write_registry(version_key, customer_name):
    existing_hash, existing_version = read_registry()
    machine_hash = get_machine_hash()

    # Previously this blocked ANY write once a license existed at all --
    # meaning a legitimate plan upgrade (re-running activation with a new
    # version key on the SAME already-licensed machine) silently did
    # nothing and left the old version key in place. The only case that
    # actually needs blocking is trying to activate a license that's
    # bound to a DIFFERENT machine (the fingerprint hash won't match) --
    # that's the real anti-piracy check. Same machine re-activating to
    # change plans should always be allowed.
    if existing_hash is not None and existing_hash != machine_hash:
        print("License is bound to a different machine")
        raise SystemExit

    key = winreg.CreateKeyEx(
        winreg.HKEY_LOCAL_MACHINE,
        REG_PATH,
        0,
        winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY,
    )

    winreg.SetValueEx(key, VALUE_NAME, 0, winreg.REG_SZ, machine_hash)
    winreg.SetValueEx(key, VERSION_VALUE_NAME, 0, winreg.REG_SZ, str(version_key))
    winreg.SetValueEx(key, CUSTOMER_VALUE_NAME, 0, winreg.REG_SZ, str(customer_name))

    winreg.CloseKey(key)

    print("Registry Written")
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    msg = QMessageBox()
    msg.setWindowTitle("Sigma Controls")
    action_word = "updated" if existing_hash is not None else "activated"
    msg.setText(f"License and Version limits {action_word} successfully.")
    msg.setIcon(QMessageBox.Information)
    msg.setWindowIcon(QIcon(resource_path("SIGMA_ICON.svg")))
    msg.setStyleSheet("QMessageBox { background-color: rgb(25,25,25); } QLabel { color: white; font: 10pt 'Segoe UI'; } QPushButton { background-color: rgb(0,160,227); color: white; border: none; border-radius: 6px; min-width: 90px; min-height: 30px; } QPushButton:hover { background-color: rgb(0,120,215); }")
    msg.exec_()

def read_registry():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        value, _ = winreg.QueryValueEx(key, VALUE_NAME)
        try:
            version_key, _ = winreg.QueryValueEx(key, VERSION_VALUE_NAME)
        except FileNotFoundError:
            version_key = None
        winreg.CloseKey(key)
        return value, version_key
    except:
        return None, None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActivationWindow()
    window.show()
    sys.exit(app.exec_())