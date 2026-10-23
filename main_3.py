# python -m PyInstaller main_3.py --onefile --windowed --icon=sigma1.ico --name "Sigma Controls - IntelliScan v1.2" --optimize=2 --hidden-import=license_check --hidden-import=updater --hidden-import=id_sett --hidden-import=db_manager --hidden-import=login --hidden-import=ui_2 --hidden-import=pyqtgraph --hidden-import=matplotlib --hidden-import=pymodbus --hidden-import=mplcursors --hidden-import=getmac --exclude-module=keras --exclude-module=tensorflow --exclude-module=torch --exclude-module=torchvision --exclude-module=torchaudio --exclude-module=sklearn --exclude-module=PyQt6 --exclude-module=jupyter --exclude-module=jupyterlab --exclude-module=astropy --exclude-module=altair --exclude-module=docker --exclude-module=gTTS --exclude-module=pytesseract --exclude-module=ultralytics --exclude-module=twilio --collect-all=matplotlib --collect-all=pyqtgraph --add-data "output-onlinepngtools.png;." --add-data "sigma.png;." --add-data "sigma1.ico;." --add-data "license_check.py;." --add-data "updater.py;." --add-data "id_sett.py;." --add-data "login.py;." --add-data "ui_2.py;." --add-data "ico_rc.py;." --add-data "db_manager.py;." --distpath "Sigma Controls - IntelliScan v1.1" --clean --noconfirm

# python -m PyInstaller main_3.py --onefile --windowed --icon=SIGMA_ICON.ico --name "Sigma Controls - IntelliScan v1.2" --optimize=2 --hidden-import=license_check --hidden-import=updater --hidden-import=id_sett --hidden-import=db_manager --hidden-import=login --hidden-import=ui_2 --hidden-import=pyqtgraph --hidden-import=matplotlib --hidden-import=pymodbus --hidden-import=mplcursors --hidden-import=getmac --exclude-module=keras --exclude-module=tensorflow --exclude-module=torch --exclude-module=torchvision --exclude-module=torchaudio --exclude-module=sklearn --exclude-module=PyQt6 --exclude-module=jupyter --exclude-module=jupyterlab --exclude-module=astropy --exclude-module=altair --exclude-module=docker --exclude-module=gTTS --exclude-module=pytesseract --exclude-module=ultralytics --exclude-module=twilio --collect-all=matplotlib --collect-all=pyqtgraph --add-data "SIGMA_ICON.svg;." --add-data "SIGMA_cache.png;." --add-data "license_check.py;." --add-data "updater.py;." --add-data "id_sett.py;." --add-data "login.py;." --add-data "ui_2.py;." --add-data "ico_rc.py;." --add-data "db_manager.py;." --distpath "Sigma Controls - IntelliScan v1.1" --clean --noconfirm

# ruff: noqa: E402,F403,F405,F541,E722,F841,F401,E702

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGraphicsBlurEffect
from pymodbus.client import ModbusSerialClient
from fpdf import FPDF
from PIL import Image
# from updater import check_for_updates
from matplotlib.dates import MinuteLocator
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import ico_rc
from PyQt5.QtCore import QProcess
import matplotlib.pyplot as plt
import winreg
import hashlib
import time
import pyqtgraph as pg
import numpy as np
import pandas as pd
import csv
import datetime
import getmac
import os
import shutil
import tempfile
import sys
import json
import importlib.util
import re
import warnings

warnings.filterwarnings(
    "ignore",
    message=r"AutoDateLocator was unable to pick an appropriate interval.*",
    category=UserWarning,
)

def _format_channel_label(ch_name):
    """Display-format a channel key like 'CH1' / 'CH24' as 'CH01' / 'CH24'
    (zero-padded to 2 digits), matching the CH01..CH24 naming used
    everywhere else in the UI. Internal dict keys stay as 'CH1'.. -- only
    the on-screen label goes through this."""
    m = re.match(r"^(CH)(\d+)$", str(ch_name).strip(), re.IGNORECASE)
    if not m:
        return str(ch_name)
    return f"{m.group(1)}{int(m.group(2)):02d}"


def get_app_icon_svg():
    return get_resource_path("SIGMA_ICON.svg")

def get_app_icon_png(size=256):
    png_path = get_resource_path("SIGMA_cache.png")
    if not os.path.exists(png_path):
        from PyQt5.QtSvg import QSvgRenderer
        from PyQt5.QtGui import QImage, QPainter
        renderer = QSvgRenderer(get_app_icon_svg())
        image = QImage(size, size, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        painter = QPainter(image)
        renderer.render(painter)
        painter.end()
        image.save(png_path)
    return png_path

# --------- for select Path -----------
def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# -------- to import modules ------------
def load_module(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


calibrate_path = get_resource_path("id_sett.py")
login_path = get_resource_path("login.py")
ui_2_path = get_resource_path("ui_2.py")
calibrate = load_module("calibrate", calibrate_path)
login = load_module("login", login_path)
ui_2 = load_module("ui_2", ui_2_path)


from id_sett import *
from login import *
from ui_2 import *
from license_check import validate_machine
from db_manager import init_db, write_row, write_event

CREDENTIALS_FILE = "credentials.json"
CONFIG_FILE = "config.json"


def atomic_write_json(path, data):
    """Write JSON to `path` without ever leaving it truncated/partial.
    config.json is written from the GUI thread (e.g. on every CH01-CH24
    checkbox toggle) while the background Worker thread reads it every
    poll cycle -- a plain open(path,'w') truncates the file the instant
    it's opened, so a concurrent read can catch it empty and blow up with
    a JSONDecodeError. Writing to a temp file in the same directory and
    os.replace()-ing it over the target is atomic on both Windows and
    POSIX: readers only ever see the old complete file or the new
    complete file, never a half-written one."""
    directory = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp_path = tempfile.mkstemp(prefix=".tmp_", dir=directory)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(data, f)
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


# ------------- Data Table window (shown alongside the Featured Graph) -------------
class ChannelTableModel(QAbstractTableModel):
    """Table model backing the data-table window. Qt's QTableView only ever
    asks data() for the rows actually scrolled into view, so this stays
    fast even with tens of thousands of rows -- no pagination needed, the
    view just scrolls (vertically for rows, horizontally for channel
    columns beyond the visible width)."""

    def __init__(self, date_col, time_col, channel_cols, channel_labels, parent=None):
        super().__init__(parent)
        self._date_col = date_col
        self._time_col = time_col
        self._channel_cols = channel_cols
        self._channel_labels = channel_labels

    def rowCount(self, parent=QModelIndex()):
        return len(self._date_col)

    def columnCount(self, parent=QModelIndex()):
        return 2 + len(self._channel_labels)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            if section == 0:
                return "Date"
            if section == 1:
                return "Time"
            return _format_channel_label(self._channel_labels[section - 2])
        return str(section + 1)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row, col = index.row(), index.column()
        if role == Qt.DisplayRole:
            if col == 0:
                return str(self._date_col[row])
            if col == 1:
                return str(self._time_col[row])
            val = self._channel_cols[col - 2][row]
            try:
                if val is None or (isinstance(val, float) and pd.isna(val)):
                    return ""
            except Exception:
                pass
            return str(val)
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return None


class ChannelDataTableWindow(QDialog):
    """Standalone data-table window opened alongside the Featured Graph on
    Submit. Shows the same date/time range and the same channel selection
    used for the graph, in one continuously scrollable table (scroll
    vertically for rows, horizontally for extra channel columns) rather
    than paged. Independent of the graph window -- either can be closed
    without affecting the other, and multiple table windows can be open
    at once for different CSVs."""

    def __init__(self, parent, date_col, time_col, channel_data, ordered_channels,
                 file_name, company_name=""):
        super().__init__(parent)
        self.setWindowTitle("Sigma Controls | Data Table")
        self.setWindowIcon(QIcon(get_app_icon_svg()))
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint
        )
        self.resize(1200, 760)

        # Everything defaults to transparent so the QDialog's own dark
        # background shows through uniformly -- no boxed/blocky panels.
        self.setStyleSheet("""
            QDialog       { background:#1b1b1b; }
            QWidget       { background:transparent; }
            QLabel        { color:#EEEEEE; font-family:'Segoe UI'; background:transparent; }
            QLabel#brand_grey    { color:#9E9E9E; font:600 15pt 'Segoe UI'; background:transparent; }
            QLabel#brand_title   { color:#00A0E3; font:bold 20pt 'Segoe UI'; background:transparent; }
            QLabel#sub           { color:#9E9E9E; font:9pt 'Segoe UI'; padding-top:2px; background:transparent; }
            QLabel#controls_brand{ color:#00A0E3; font:bold 9pt 'Segoe UI'; background:transparent; }
            QTableView {
                background:#232336;
                alternate-background-color:#20202e;
                gridline-color:#3a3a4a;
                color:#EEEEEE;
                font:10pt 'Segoe UI';
                border:1px solid #3a3a4a;
                border-radius:6px;
            }
            QHeaderView::section {
                background:#00A0E3;
                color:white;
                font:bold 10pt 'Segoe UI';
                padding:6px;
                border:none;
            }
            QScrollBar:horizontal, QScrollBar:vertical {
                background:#232336;
                border:none;
            }
            QScrollBar::handle {
                background:#00A0E3;
                border-radius:5px;
            }
            QScrollBar::handle:hover { background:#0088C1; }
        """)

        root = QVBoxLayout(self)
        root.setContentsMargins(20, 16, 20, 14)
        root.setSpacing(10)

        # ---- Header: matches the graph's header layout exactly --
        # left = company name (plain text, no icon), right = icon stacked
        # above "Controls", same as the Featured Graph's top-right mark.
        header_row = QHBoxLayout()

        title_col = QVBoxLayout()
        title_col.setSpacing(0)
        brand = QLabel(company_name or "Sigma Controls")
        brand.setObjectName("brand_grey")
        title_col.addWidget(brand)
        subtitle = QLabel("Table Record")
        subtitle.setObjectName("brand_title")
        title_col.addWidget(subtitle)
        header_row.addLayout(title_col)

        header_row.addStretch()

        controls_col = QVBoxLayout()
        controls_col.setSpacing(2)
        controls_col.setAlignment(Qt.AlignHCenter)
        icon_lbl = QLabel()
        pix = QPixmap(get_app_icon_png()).scaled(
            64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        icon_lbl.setPixmap(pix)
        icon_lbl.setAlignment(Qt.AlignHCenter)
        controls_col.addWidget(icon_lbl)
        controls_brand = QLabel("Controls")
        controls_brand.setObjectName("controls_brand")
        controls_brand.setAlignment(Qt.AlignHCenter)
        controls_col.addWidget(controls_brand)
        header_row.addLayout(controls_col)

        root.addLayout(header_row)

        info = QLabel(
            f"File: {file_name}    |    Channels shown: {len(ordered_channels)}"
            f"    |    Rows: {len(date_col)}"
        )
        info.setObjectName("sub")
        root.addWidget(info)

        # ---- Table: all channels in one continuous, scrollable view ----
        self.table = QTableView()
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.table.horizontalHeader().setDefaultSectionSize(120)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # channel_data is keyed by channel name (e.g. "CH1"); the model
        # indexes columns positionally, so it needs an ordered list built
        # from ordered_channels, not the dict itself.
        channel_cols_list = [channel_data[ch] for ch in ordered_channels]
        self.model = ChannelTableModel(date_col, time_col, channel_cols_list, ordered_channels)
        self.table.setModel(self.model)
        root.addWidget(self.table, stretch=1)


# ------------- MainWindow Class --------------
class MainWindow(QMainWindow):
    # ---------- initialization -----------
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.allowed_ids = self.extract_allowed_ids()
        if not validate_machine():
            msg = QMessageBox()

            msg.setWindowTitle("Sigma Controls | License Error")
            msg.setText("License validation failed.")
            msg.setIcon(QMessageBox.Critical)

            msg.setWindowIcon(QIcon(get_app_icon_svg()))

            msg.setStyleSheet("""
            QMessageBox {
                background-color: rgb(25,25,25);
            }

            QLabel {
                color: white;
                font: 11pt "Segoe UI";
                background-color: transparent;
            }

            QPushButton {
                background-color: rgb(0,160,227);
                color: white;
                border: none;
                border-radius: 6px;
                min-width: 90px;
                min-height: 32px;
                font: 10pt "Segoe UI";
            }

            QPushButton:hover {
                background-color: rgb(0,120,215);
            }
            """)

            msg.exec_()
            sys.exit()
        # ------------ Scanner Files Store -------------
        if not os.path.exists("Scanner_Files"):
            try:
                os.mkdir("Scanner_Files")
            except Exception as E:
                pass

        today_date = datetime.date.today().strftime("%d-%m-%Y")

        # Create the directory for today's date if it doesn't exist
        self.directory_path = os.path.join("Scanner_Files", today_date)
        if not os.path.exists(self.directory_path):
            os.makedirs(self.directory_path)

        self.initiate()
        self.last_csv_write_time = time.time()

        self.latest_rr = None
        self.latest_raw_rr = None  # raw Modbus values
        self.latest_scaled_rr = None  # scaled & validated values

        self.csv_writer = csvWriter()
        self.worker = None

        # Channel selection used ONLY for the "Featured Graph" built from a
        # historical CSV file. Deliberately separate from the live
        # CH01Check..CH24Check checkboxes, which control the on-screen live
        # plot/logging view and must not be disturbed by graph generation.
        # Key: "CH1".."CH24" -> bool (default True == shown).
        self._graph_channel_selection = {}

        try:
            init_db()
            write_event("SYSTEM", "APP_START", "Application started")
        except Exception as e:
            pass

    # --- UPDATE THIS FUNCTION IN main_3.py ---
    def extract_allowed_ids(self):
        # This MUST read the exact same registry path/value names that
        # fingerprint.py (IntelliScan's activation tool) writes to, and
        # that license_check.py's validate_machine() reads from --
        # SOFTWARE\Sigma_Controls_IntelliScan\Fingerprint. This function
        # was previously reading from a DIFFERENT, never-written key
        # ("Sigma_Controls_IntelliScan_v1.1\Fingerprint" -- note the
        # extra "_v1.1"), so it silently failed every single time and
        # fell back to the 2-ID default regardless of what plan was
        # actually activated. That's the root cause of licenses never
        # going past 2 IDs.
        REG_PATH = r"SOFTWARE\Sigma_Controls_IntelliScan\Fingerprint"
        VERSION_VALUE_NAME = "Sigma_Controls_IntelliScan_Version_Key"
        CUSTOMER_VALUE_NAME = "Sigma_Controls_IntelliScan_Customer"
        SECRET = "SC_7YkP1592mQa_4LShahxZ_2026_Sigma_Controls_88RSneh"

        # Diagnostics captured regardless of outcome, so callers can tell
        # the user WHY they ended up on a given plan instead of failing
        # silently.
        diag = {
            "reg_path": REG_PATH,
            "key_found": False,
            "version_key": "",
            "customer": "",
            "matched_plan": None,
            "error": "",
        }

        try:
            import winreg
            import hashlib

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
            diag["key_found"] = True
            version_key, _ = winreg.QueryValueEx(key, VERSION_VALUE_NAME)
            diag["version_key"] = version_key or ""

            try:
                customer, _ = winreg.QueryValueEx(key, CUSTOMER_VALUE_NAME)
            except Exception:
                customer = ""
            diag["customer"] = customer or ""

            winreg.CloseKey(key)

            if version_key and customer:
                for test_id in ["2", "4", "8"]:
                    test_hash = hashlib.sha256((customer + test_id + SECRET).encode()).hexdigest()
                    expected_key = (
                        test_hash[:4] + "-" + test_hash[4:8] + "-" +
                        test_hash[8:12] + "-" + test_hash[12:16]
                    ).upper()

                    if version_key == expected_key:
                        diag["matched_plan"] = int(test_id)
                        self.license_diag = diag
                        return int(test_id)

                diag["error"] = "Version key present but did not match any known plan hash."
            else:
                diag["error"] = "Registry key found but Version Key or Customer Name is empty."

        except FileNotFoundError:
            diag["error"] = f"Registry key not found at HKLM\\{REG_PATH}."
        except Exception as e:
            diag["error"] = f"Unexpected error reading license registry: {e}"

        self.license_diag = diag
        return 2  # Default fallback to Starter Plan

    # -------------- Initiate Login Page ---------------
    def initiate(self):
        self.ui = Ui_SigmaControls_2()
        self.ui.setupUi(self)
        self.setMaximumSize(641, 446)
        self.ui.Start_2.setShortcut("Ctrl+S")
        self.ui.lineEdit_5.setEchoMode(QLineEdit.Password)

        try:
            self.ui.Start_2.clicked.connect(self.startMain)
        except Exception as E:
            pass

    # ---------------- Check for ID & Pass ---------------
    def startMain(self):
        while True:
            x = self.ui.lineEdit_4.text()
            y = self.ui.lineEdit_5.text()

            users = self.load_credentials()
            if self.validate_credentials(users, x, y):
                self.show_message("Login", "Login successfully!", "#02c702")
                write_event(x, "LOGIN", "User logged in successfully")
                self.ui = Ui_SigmaControls_1()
                self.setMaximumSize(1920, 1050)
                self.ui.setupUi(self)
                self.start_button_default_style = self.ui.Start.styleSheet()
                self.record_blink_timer = QTimer(self)
                self.record_blink_timer.timeout.connect(self.blink_start_button)
                self.record_blink_state = False
                
                self.ui.logo.setCursor(Qt.PointingHandCursor)
                self.ui.logo.mousePressEvent = self.show_about_dialog
                self.ui.lineEdit_4.setMaxLength(30)
                self.center()

                self.ui.tabWidget.setCurrentIndex(0)
                self._init_comm_status_indicator()
                
                # --- 3. RESTRICT SLAVE COMBOBOX ---
                while self.ui.Slave.count() > self.allowed_ids:
                    self.ui.Slave.removeItem(self.ui.Slave.count() - 1)

                self.timer = QTimer(self)
                self.timer.timeout.connect(self.update_time)
                self.timer.start(1000)
                self.load_config()
                self.update_all_y_axis_labels()

                self.graph_layout = QVBoxLayout(self.ui.totalgraph)
                self.ui.totalgraph.setLayout(self.graph_layout)
                self.plot_widget = pg.PlotWidget()
                self.graph_layout.addWidget(self.plot_widget)
                self.plot_widget.setBackground("w")
                self.plot_widget.getAxis("left").setTextPen("k")
                self.plot_widget.getAxis("bottom").setTextPen("k")
                self.plot_widget.getAxis("left").setPen("k")
                self.plot_widget.getAxis("bottom").setPen("k")
                self.plot_widget.setTitle(
                    f"Graph (ID-{self.selected_slave})",
                    color="#00A0E3",
                )
                # Legend added once here (not per-update) so it persists
                # across .clear() calls and pyqtgraph auto-syncs its
                # entries to whatever channels are currently plotted --
                # previously plot() was called with name= but addLegend()
                # was never called anywhere, so no legend ever appeared.
                # Because plot_last_reading() re-plots only the checked
                # channels after every clear(), toggling a channel off
                # makes its legend entry disappear on the very next
                # refresh with no extra code needed.
                # Two-column legend, split at 12 channels, so a full
                # 24-channel setup doesn't get one giant legend box that
                # runs off the bottom of the plot. Built and managed
                # manually (not via addLegend()/clear()) so hiding a
                # channel actually removes its entry for good instead of
                # it reappearing on the next reading.
                self.live_legend1 = pg.LegendItem(offset=(-260, 10), spacing=4)
                self.live_legend1.setParentItem(self.plot_widget.graphicsItem())
                self.live_legend2 = pg.LegendItem(offset=(-130, 10), spacing=4)
                self.live_legend2.setParentItem(self.plot_widget.graphicsItem())
                _live_legend_font = QFont()
                _live_legend_font.setPixelSize(9)
                for _lg in (self.live_legend1, self.live_legend2):
                    _lg.setFont(_live_legend_font)
                    _lg.setBrush(pg.mkBrush(0, 0, 0, 220))
                    _lg.setPen(pg.mkPen(color="#00A0E3", width=1))
                    _lg.setLabelTextColor("#ffffff")
                # ch_index (0-23) -> PlotDataItem currently on screen, so
                # update_graph() can add/remove/update individual curves
                # instead of clearing and rebuilding everything (and the
                # legend along with it) on every single reading.
                self._live_curves = {}
                _yt = self.y_axis_text.strip() if hasattr(self, "y_axis_text") else ""
                self.update_all_y_axis_labels()
                self.plot_widget.setLabel(
                    "bottom",
                    '<span style="color:#00A0E3; font-weight:bold;">Date & Time</span>',
                    justify="center",
                )

                self.multigraph_layout = QVBoxLayout(self.ui.multigraph)
                self.ui.multigraph.setLayout(self.multigraph_layout)
                self.plot_widget10 = pg.PlotWidget()
                self.multigraph_layout.addWidget(self.plot_widget10)

                self.plot_widget10.setBackground("w")
                self.plot_widget10.getAxis("left").setTextPen("k")
                self.plot_widget10.getAxis("bottom").setTextPen("k")
                self.plot_widget10.getAxis("left").setPen("k")
                self.plot_widget10.getAxis("bottom").setPen("k")
                self.plot_widget10.setTitle(
                    f"Last 10 Readings (ID-{self.selected_slave})",
                    color="#00A0E3",
                )
                # No legend on this graph -- it's a small "at a glance"
                # chart and the legend box was crowding it out.
                _yt10 = self.y_axis_text.strip() if hasattr(self, "y_axis_text") else ""
                self.update_all_y_axis_labels()
                self.plot_widget10.setLabel(
                    "bottom",
                    '<span style="color:#00A0E3; font-weight:bold;">Date & Time</span>',
                    justify="center",
                )

                # self.plot_last_10_readings()
                self.display_csv()
                self.display_csv10()
                self.load_config()
                self.update_channel_icons(getattr(self, "selected_slave", 1))

                self._reset_ui_to_initial()  # ← add this line right after
                self._check_com_port_on_startup()

                self.update_all_y_axis_labels()

                self.ui.textEdit.setText(self.header)
                self.update_header_status_text()
                # self.plot_graph()

                self.telemetry_timer = QTimer(self)
                self.telemetry_timer.timeout.connect(self.update_telemetry_continuous)
                self.telemetry_timer.start(100)  # 0.1 sec
                self.replay_speed = 1

                self.replay_mode = False
                self.replay_rows = []
                self.replay_index = 0
                self.replay_speed = 1  # default 1x
                self.replay_paused = False

                self.replay_timer = QtCore.QTimer()
                self.replay_timer.timeout.connect(self.replay_next_row)

                QShortcut(QKeySequence("Ctrl+R"), self, self.start_csv_replay)

                QShortcut(
                    QKeySequence("Ctrl+1"), self, lambda: self.set_replay_speed(1)
                )

                QShortcut(
                    QKeySequence("Ctrl+2"), self, lambda: self.set_replay_speed(2)
                )

                QShortcut(
                    QKeySequence("Ctrl+3"), self, lambda: self.set_replay_speed(10)
                )

                # Pause / resume the running replay. Space is the quick
                # toggle; Ctrl+P kept as an explicit alternate binding for
                # anyone used to media-player style pause shortcuts.
                QShortcut(QKeySequence("Space"), self, self.toggle_replay_pause)
                QShortcut(QKeySequence("Ctrl+P"), self, self.toggle_replay_pause)

                self.update_timer = QTimer(self)
                self.update_timer.timeout.connect(self.launch_updater_exe)
                self.update_timer.start(86400000) # Trigger every 24 hours (86,400,000 ms)

                # Check once automatically 5 seconds after login
                QTimer.singleShot(5000, self.launch_updater_exe)
                break
            else:
                write_event(x, "LOGIN_FAILED", "Invalid username or password")
                self.show_message("Login", "Invalid credentials", "#ff4c4c")
                break

        # In startMain(), add:
        try:
            self.ui.Save.clicked.connect(self.save_slave_selection)
        except Exception as E:
            pass

        # ----------- Check if Start button clicked or not ----------
        try:
            self.ui.Start.clicked.connect(self.start_worker)
        except Exception as E:
            pass

        # ---------- Check if Stop button clicked or not -----------
        try:
            self.ui.Stop.clicked.connect(self.stop_worker)
        except Exception as E:
            pass

        # ---------- Check if ID Settings button clicked or not -----------
        try:
            self.ui.IDSetting.clicked.connect(self.run_calibration)
        except Exception as E:
            pass

        # ---------- Check if Open CSV File button clicked or not -----------
        try:
            self.ui.pushButton.clicked.connect(self.csv_file_open)
        except Exception as E:
            pass

        # ---------- Check if Open LetterHead file button clicked or not ------------
        try:
            self.ui.pushButton_2.clicked.connect(self.letterhead_file_open)
        except Exception as E:
            pass

        # ---------- Check if Set file button clicked or not ------------
        try:
            self.ui.Start_2.clicked.connect(self.set_button)
        except Exception as E:
            pass

        # ---------- Check if Set file button clicked or not ------------
        try:
            self.ui.Start_3.clicked.connect(self.submit_button)
        except Exception as E:
            pass

        # ---------- Check if Set file button clicked or not ------------
        try:
            self.ui.Start_4.clicked.connect(self.print_button)
        except Exception as E:
            pass

    # --------------------------------------------------------
    # UPDATER LAUNCHER LOGIC
    # --------------------------------------------------------
    def launch_updater_exe(self):
        # --- 1. NEW DATE CHECK LOGIC ---
        today_str = datetime.date.today().strftime("%d-%m-%Y")
        existing_config = {}
        
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    existing_config = json.load(f)
            except Exception:
                pass
                
        last_check = existing_config.get("last_update_check", "")
        
        # If we already checked today, silently abort the function!
        if last_check == today_str:
            return
            
        # Otherwise, save today's date so subsequent logins today are skipped
        existing_config["last_update_check"] = today_str
        try:
            atomic_write_json(CONFIG_FILE, existing_config)
        except Exception:
            pass
        # -------------------------------

        # 2. Instantly blur the main UI
        self.blur_main() 
        
        # 3. Check for the custom named executable first, then fallback to testing names
        custom_exe_name = "Sigma Controls - IntelliScan Updater.exe"
        
        if os.path.exists(custom_exe_name):
            target = custom_exe_name
        elif os.path.exists("updater.exe"):
            target = "updater.exe"
        elif os.path.exists("updater.py"):
            target = "updater.py"
        else:
            self.unblur_main()
            return
            
        # 4. Run completely silently in the background!
        self.updater_process = QProcess(self)
        self.updater_process.finished.connect(self.on_updater_finished)
        
        if target.endswith(".py"):
            self.updater_process.start(sys.executable, [target])
        else:
            self.updater_process.start(target, [])

    def on_updater_finished(self):
        # 5. Automatically unblur the background the moment the updater closes
        self.unblur_main()

    def _reset_ui_to_initial(self):
        # Clear all LCD displays
        for i in range(1, 25):
            try:
                getattr(self.ui, f"lcdNumber_{i:02d}").display(0)
            except:
                pass

        # Clear data tables
        if hasattr(self, "csv_table_widget"):
            self.csv_table_widget.clearContents()
            self.csv_table_widget.setRowCount(0)
        if hasattr(self, "csv_table_widget1"):
            self.csv_table_widget1.clearContents()
            self.csv_table_widget1.setRowCount(0)

        # Clear graphs
        try:
            self.plot_widget.clear()
            self._live_curves = {}
            for _lg in (getattr(self, "live_legend1", None), getattr(self, "live_legend2", None)):
                if _lg is not None:
                    _lg.clear()
            self.plot_widget.setTitle(
                f"Graph (ID-{self.selected_slave})",
                color="#00A0E3",
            )
        except:
            pass
        try:
            self.plot_widget10.clear()
            self.plot_widget10.setTitle(
                f"Last 10 Readings (ID-{self.selected_slave})",
                color="#00A0E3",
            )
        except:
            pass

        # Reset latest data state only
        self.latest_scaled_rr = None
        self.latest_raw_rr = None
        if hasattr(self, "_slave_latest"):
            self._slave_latest = {}

    def set_replay_speed(self, speed):
        self.replay_speed = speed
        self.statusBar().showMessage(f"Replay Speed = {speed}x", 3000)

    def _check_com_port_on_startup(self):
        import serial.tools.list_ports
        available = [p.device for p in serial.tools.list_ports.comports()]
        saved_com = getattr(self, "com", "").strip()

        if not saved_com:
            self.show_message(
                "COM Port",
                "No COM Port configured.\nPlease select one in Settings.",
                "#ff4c4c",
            )
            return

        if saved_com in available:
            self.show_message("COM Port", f"{saved_com} detected and ready.", "#02c702")
        else:
            self.show_message(
                "COM Port",
                f"{saved_com} not found.\nAvailable ports: {', '.join(available) or 'None'}\n\nPlease check your connection.",
                "#ff4c4c",
            )

    def blink_start_button(self):
        if self.record_blink_state:
            self.ui.Start.setStyleSheet("""
            QPushButton{
                background-color:#0D6EFD;
                color:white;
                font-weight:bold;
                border-radius:6px;
            }
            """)
        else:
            self.ui.Start.setStyleSheet("""
            QPushButton{
                background-color:#0052CC;
                color:white;
                font-weight:bold;
                border-radius:6px;
            }
            """)

        self.record_blink_state = not self.record_blink_state


    def start_record_indicator(self):
        self.record_blink_state = False
        self.record_blink_timer.start(500)


    def stop_record_indicator(self):
        self.record_blink_timer.stop()
        self.ui.Start.setStyleSheet(self.start_button_default_style)

    def blur_main(self):
        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(12)
        self.ui.centralwidget.setGraphicsEffect(self.blur)
        self.ui.centralwidget.repaint()
        QCoreApplication.processEvents()

    def unblur_main(self):
        self.ui.centralwidget.setGraphicsEffect(None)
        self.ui.centralwidget.repaint()
        QCoreApplication.processEvents()
        
    def show_about_dialog(self, event):
        self.blur_main()
        dialog = QDialog(self)
        dialog.setWindowTitle("Sigma Controls | About Us")
        dialog.setFixedSize(850,150)
        dialog.setWindowIcon(QIcon(get_app_icon_svg()))
        dialog.setStyleSheet("""
        QDialog{
            background-color:#000000;
            border:2px solid white;
        }
        QLabel{
            color:white;
            font:11pt Segoe UI;
        }
        QPushButton{
            background:#1E90FF;
            color:white;
            border-radius:8px;
            padding:8px;
            font:11pt Segoe UI;
        }
        QPushButton:hover{
            background:#0B70D0;
        }
        """)
        layout = QVBoxLayout(dialog)
        layout.setSizeConstraint(QLayout.SetFixedSize)

        logo = QLabel()
        pix = QtGui.QPixmap(":/ico/icons/Sigma_Logo_Temp.png")

        BOX_W = 360
        BOX_H = 120
        IMG_W = 340
        IMG_H = 100

        logo.setFixedSize(BOX_W, BOX_H)
        logo.setAlignment(Qt.AlignCenter)
        logo.setPixmap(
            pix.scaled(
                IMG_W,
                IMG_H,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
        )
        logo.setStyleSheet("""
        QLabel{
            background:white;
            border:2px solid #2d8cff;
            border-radius:10px;
            padding:3px;
        }
        """)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo, 0, Qt.AlignCenter)
        layout.addSpacing(15)
        
        company = QLabel("""
        <table style="
        color:white;
        font-family:'Segoe UI';
        font-size:11pt;
        border-spacing:8px 10px;
        ">

        <tr>
        <td width="150"><b>🌐 Website</b></td>
        <td width="10">:</td>
        <td>www.sigmacontrolsindia.com</td>
        </tr>

        <tr>
        <td><b>📩 Email</b></td>
        <td>:</td>
        <td>sales@sigmacontrolsindia.com</td>
        </tr>

        <tr>
        <td><b>📞 Phone</b></td>
        <td>:</td>
        <td>95100 31871 &nbsp; | &nbsp; 79902 73727</td>
        </tr>

        <tr>
        <td valign="top"><b>📍 Address</b></td>
        <td valign="top">:</td>
        <td>
        15, Jahnavi Industrial Estate, S.P. Ring Road Circle,<br>
        Odhav, Ahmedabad - 382415, Gujarat, India.
        </td>
        </tr>

        </table>
        """)

        company.setTextFormat(Qt.RichText)
        company.setAlignment(Qt.AlignCenter)
        layout.addWidget(company)
        layout.addSpacing(8)
        
        copyright = QLabel(
            "<center><span style='font-size:9pt;color:#b0b0b0;'>"
            "© 2026 Sigma Controls · All Rights Reserved"
            "</span></center>"
        )

        copyright.setContentsMargins(0, 0, 0, 0)
        copyright.setAlignment(Qt.AlignCenter)
        copyright.setStyleSheet("""
        QLabel{
            color: #b0b0b0;
            font-size: 9pt;
            font-family: Segoe UI;
        }
        """)
        layout.addWidget(copyright)
        layout.addSpacing(4)
        
        # buttonLayout.setSpacing(12)
        # buttonLayout.setContentsMargins(0, 4, 0, 0)
        
        buttonLayout = QHBoxLayout()
        visit = QPushButton("Visit Website")
        close = QPushButton("Close")
        buttonLayout.addWidget(visit)
        buttonLayout.addWidget(close)
        layout.addLayout(buttonLayout)
        
        from PyQt5.QtGui import QDesktopServices
        from PyQt5.QtCore import QUrl
        
        visit.clicked.connect(
            lambda:
            QDesktopServices.openUrl(
                QUrl("https://www.sigmacontrolsindia.com")
            )
        )
        close.clicked.connect(dialog.accept)
        dialog.exec_()
        self.unblur_main()
    
    # ---------- Update Telemetry Continuous -----------
    def update_telemetry_continuous(self):
        if self.latest_scaled_rr is None:
            return

        rr = self.latest_scaled_rr

        check_boxes = [
            getattr(self.ui, f"CH{i:02d}Check").isChecked() for i in range(1, 25)
        ]
        lcds = [getattr(self.ui, f"lcdNumber_{i:02d}") for i in range(1, 25)]

        # blink based on current time (no extra timer)
        blink_on = int(time.time() * 2) % 2 == 0  # ~0.5 sec blink

        for i in range(24):
            if not check_boxes[i]:
                lcds[i].display(0)

            elif rr[i] is None:
                if blink_on:
                    lcds[i].display("OPE")
                else:
                    lcds[i].display("   ")

            else:
                lcds[i].display(rr[i])

    # ------------ Load Credentials --------------
    def load_credentials(self):
        with open(CREDENTIALS_FILE, "r") as file:
            data = json.load(file)
        return data["users"]

    # ------------ Validate Credentials --------------
    def validate_credentials(self, users, user_id, password):
        for user in users:
            self.mac = self.get_machine_mac()
            if (
                user["id"] == user_id
                and user["password"] == password
                and user["mac"] == self.mac
            ):
                return True
        return False

    # ------------ Show Message Box --------------
    def show_message(self, title, text, color):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(text)

        # Add logo icon
        icon = QIcon()
        icon = QIcon(get_app_icon_svg())
        msg.setWindowIcon(icon)

        msg.setStyleSheet(f"""
            QMessageBox {{
                background-color: #000000;
            }}
            QLabel {{
                color: {color};
                font-size: 22px;
            }}
            QPushButton {{
                background-color: #e0dede;
                color: #000000;
                min-width: 80px;
                min-height: 28px;
                border-radius: 4px;
                padding: 4px 14px;
                font-size: 20px;
            }}
            QPushButton:hover {{
                background-color: #525252;
            }}
        """)
        self.blur_main()
        msg.exec_()
        self.unblur_main()

    # ------------ Comms Watchdog LED --------------
    def _init_comm_status_indicator(self):
        """Small always-visible LED + label so operators can see comms
        health at a glance instead of relying on console prints they'll
        never see. Placed as the tab bar's corner widget (top-right of the
        DATA / GRAPH / CSV / ADV. SETTINGS tabs) so it's visible on the
        main screen where the operator is actually looking. (No duplicate
        copy in the status bar -- one clear indicator, not two.)"""
        try:
            corner = QWidget()
            corner_row = QHBoxLayout(corner)
            corner_row.setContentsMargins(0, 0, 8, 0)
            corner_row.setSpacing(6)
            self._comm_led_tab = QLabel()
            self._comm_led_tab.setFixedSize(12, 12)
            self._comm_status_text_tab = QLabel("Comms: Idle")
            self._comm_status_text_tab.setStyleSheet(
                "font:bold 9pt 'Segoe UI'; background:transparent;"
            )
            corner_row.addWidget(self._comm_led_tab)
            corner_row.addWidget(self._comm_status_text_tab)
            self.ui.tabWidget.setCornerWidget(corner, Qt.TopRightCorner)
        except Exception as e:
            pass

        self.update_comm_status("idle")

    def update_comm_status(self, status):
        """status: 'idle' | 'connected' | 'reconnecting' | 'lost' | 'crashed'"""
        styles = {
            "idle":         ("#757575", "Comms: Idle"),
            "connected":    ("#2ECC71", "Comms: Connected"),
            "reconnecting": ("#FFC107", "Comms: Reconnecting..."),
            "lost":         ("#E53935", "Comms: Lost"),
            "crashed":      ("#E53935", "Comms: Stopped"),
        }
        color, text = styles.get(status, styles["idle"])
        led_css = f"background-color:{color}; border-radius:6px; border:1px solid #222;"

        if hasattr(self, "_comm_led_tab"):
            self._comm_led_tab.setStyleSheet(led_css)
            self._comm_status_text_tab.setText(text)
            self._comm_status_text_tab.setStyleSheet(
                f"color:{color}; font:bold 9pt 'Segoe UI'; background:transparent;"
            )

        if status == "lost":
            self.show_toast(
                "Comms connection lost — attempting to reconnect...",
                level="error", duration=5000,
            )

    def handle_worker_crash(self, error_message):
        """Connected to Worker.crashed_signal. A QThread's unhandled
        exception doesn't crash the app -- it just silently kills that
        thread, so logging/polling stops with zero visible indication
        (this is exactly what caused readings to stop mid-session with
        nothing but a JSONDecodeError buried in the console). Surface it
        loudly instead: red LED + a persistent toast, and stop the UI
        from pretending logging is still active."""
        self.update_comm_status("crashed")
        self.show_toast(
            "Logging thread stopped unexpectedly — press Stop, then Start "
            "again to resume. (" + error_message[:120] + ")",
            level="error", duration=8000,
        )
        try:
            self.ui.Start.setEnabled(True)
            self.ui.Stop.setEnabled(False)
        except Exception:
            pass
        try:
            self.stop_record_indicator()
        except Exception:
            pass
        # Don't call self.worker.stop()/wait() here -- the thread already
        # exited on its own after the exception. Just drop our reference
        # so a fresh Start press builds a brand new Worker instead of
        # reusing/restarting a dead one.
        self.worker = None

    # ------------ Non-blocking toast/banner --------------
    def show_toast(self, text, level="warning", duration=4000):
        """Non-blocking banner notification (e.g. a scheduled CSV write
        failing mid-session) that doesn't interrupt the operator the way
        show_message's modal dialog does. Self-dismisses after `duration`
        ms; a new call replaces whatever toast is currently showing."""
        if not hasattr(self, "_toast_label"):
            self._toast_label = QLabel(self)
            self._toast_label.setWordWrap(True)
            self._toast_label.setAlignment(Qt.AlignCenter)
            self._toast_label.hide()
            self._toast_timer = QTimer(self)
            self._toast_timer.setSingleShot(True)
            self._toast_timer.timeout.connect(self._toast_label.hide)

        colors = {
            "error":   "#B71C1C",
            "warning": "#E65100",
            "info":    "#01579B",
        }
        bg = colors.get(level, colors["warning"])
        self._toast_label.setText(f"  ⚠ {text}  ")
        self._toast_label.setStyleSheet(f"""
            background-color: {bg};
            color: white;
            font: bold 10pt 'Segoe UI';
            border-radius: 6px;
            padding: 10px 16px;
        """)
        self._toast_label.setMaximumWidth(int(self.width() * 0.6) or 420)
        self._toast_label.adjustSize()
        margin = 16
        x = self.width() - self._toast_label.width() - margin
        self._toast_label.move(max(margin, x), margin)
        self._toast_label.show()
        self._toast_label.raise_()
        self._toast_timer.start(duration)

    # ------------ Get Machine MAC Address --------------
    def get_machine_mac(self):
        try:
            self.mac = getmac.get_mac_address()
            return self.mac
        except Exception as e:
            return None

    # ------------ Check com port & baud rate ------------
    def check_connection(self):
        # self.connection_timer = QTimer(self)
        # self.connection_timer.timeout.connect(self.verify_connection)
        # self.connection_timer.start(1000)
        pass

    # ----------- for Verify Connection -------------
    def verify_connection(self):
        # com = self.ui.COMport.currentText()
        # baud = self.ui.Baud.currentText()
        # client = ModbusSerialClient(port=com, baudrate=int(baud), timeout=2)
        # if client.connect():
        #     self.connection_timer.stop()
        #     client.close()
        #     self.show_message("COM Port", "COM Port Connected", "#02c702")

        # else:
        #     self.connection_timer.stop()
        #     client.close()
        #     self.show_message("COM Error", "COM Port Not Connected", "#ff4c4c")
        pass

    # ----------- Start Communication ----------
    def start_worker(self):
        write_event("ADMIN", "START", "Temperature recording started")
        # Stop any running CSV replay so live logging owns the plot/tables
        self.stop_csv_replay()
        com = self.ui.COMport.currentText().strip()
        baud = self.ui.Baud.currentText().strip()

        if not com or com == "Select COM Port":
            self.show_message("COM Error", "Please select a COM Port.", "#ff4c4c")
            return

        # Validate port exists
        import serial.tools.list_ports

        available_ports = [p.device for p in serial.tools.list_ports.comports()]
        if com not in available_ports:
            write_event("SYSTEM", "COM_ERROR", f"{com} not found")

            self.show_message(
                "COM Error",
                f"{com} not found.\nAvailable: {', '.join(available_ports) or 'None'}",
                "#ff4c4c",
            )
            return

        # Read serial settings directly from UI
        parity_raw = self.ui.ParityType.currentText().strip()  # "N", "E", "O"
        databits = int(self.ui.StartBitOpt.currentText().strip())  # 7 or 8
        stopbits = int(self.ui.StopBitOpt.currentText().strip())  # 1 or 2

        slave_configs = []
        for i in range(1, 9):
            if getattr(self, f"slave_enabled_{i}", False):
                slave_configs.append(
                    {
                        "num": i,
                        "slave_id": i,
                        "address": getattr(self, f"address_{i}", 0),
                    }
                )

        if not slave_configs:
            self.show_message("Start", "No slaves enabled in ID Settings!", "#ff4c4c")
            return

        self.worker = Worker(
            com,
            baud,
            self.log_time,
            slave_configs,
            parity=parity_raw,
            stopbits=stopbits,
            databits=databits,
        )
        self.worker.update_signal.connect(self.start_update_ui)
        self.worker.error_signal.connect(self.handle_slave_error)
        self.worker.comm_status_signal.connect(self.update_comm_status)
        self.worker.crashed_signal.connect(self.handle_worker_crash)
        self.worker.start()
        self.update_comm_status("reconnecting")

        self.start_record_indicator()
        # Disable ID Settings while communication is running
        self.ui.COMport.setEnabled(False)
        self.ui.Baud.setEnabled(False)
        self.ui.ParityType.setEnabled(False)
        self.ui.StartBitOpt.setEnabled(False)
        self.ui.StopBitOpt.setEnabled(False)
        self.ui.IDSetting.setEnabled(False)

        self.csv_writer_start_all(slave_configs)

        # Clean slate on Start: only today's file, no leftover rows/legends
        # from a previous day or from a report that was just generated.
        if hasattr(self, "csv_table_widget"):
            self.csv_table_widget.setRowCount(0)
        if hasattr(self, "csv_table_widget1"):
            self.csv_table_widget1.setRowCount(0)

        self._live_curves = {}
        for _lg in (
            getattr(self, "live_legend1", None),
            getattr(self, "live_legend2", None),
        ):
            if _lg is not None:
                try:
                    _lg.clear()
                except Exception:
                    pass
        try:
            self.plot_widget.clear()
            self.plot_widget.setTitle(
                f"Graph (ID-{self.selected_slave})",
                color="#00A0E3",
            )
        except Exception:
            pass
        self._attach_live_legends()
        try:
            self.plot_widget10.clear()
            self.plot_widget10.setTitle(
                f"Last 10 Readings (ID-{self.selected_slave})",
                color="#00A0E3",
            )
        except Exception:
            pass

        # Reload ONLY the current day's CSV for the selected slave
        self.display_csv()
        self.display_csv10()

    # ---------- Start display values -----------
    def start_update_ui(self, slave_num, regs):
        selected = getattr(self, "selected_slave", 1)

        # ── PART 1: failed read ──
        if regs is None:
            if slave_num == selected:
                self._show_graph_error(f"Slave ID-{slave_num}: No Response")
                if hasattr(self, "csv_table_widget"):
                    self.csv_table_widget.clearContents()
                    self.csv_table_widget.setRowCount(0)
                if hasattr(self, "csv_table_widget1"):
                    self.csv_table_widget1.clearContents()
                    self.csv_table_widget1.setRowCount(0)
            return

        # ── PART 2: successful read — scale values ──
        try:
            div = float(getattr(self, f"div_factor_{slave_num}", 10) or 10)
        except:
            div = 10

        scaled = []
        for v in regs:
            try:
                raw = int(v)  # raw 16-bit Modbus register, range 0..65535

                # --- Two's complement conversion (must happen BEFORE any range check) ---
                if raw >= 32768:
                    raw -= 65536
                # raw is now a signed value in range -32768..32767

                # --- Valid data window: -2000 to 15000 (raw/signed units, pre-division) ---
                # Anything outside this window is treated as OPEN / sensor fault (OPE),
                # since legitimate readings never fall outside it.
                if raw < -2000 or raw > 15000:
                    scaled.append(None)  # -> displayed as "OPE"
                    continue

                value = raw / div
                value_rounded = round(value, 2)
                scaled.append(value_rounded)

            except:
                scaled.append(None)

        if not hasattr(self, "_slave_latest"):
            self._slave_latest = {}
        self._slave_latest[slave_num] = scaled

        # ── LCD: set EVERY poll before any early returns ──
        if slave_num == selected:
            self.latest_scaled_rr = scaled  # timer reads this at 100ms

        # ── CSV write: only at log_time interval ──
        if not (hasattr(self, "slave_writers") and slave_num in self.slave_writers):
            return

        # Always resolve path for the CURRENT calendar day so a session
        # that crosses midnight (or a Start after generating a report for
        # another day) never appends into yesterday's file.
        path = self.get_slave_csv_path(slave_num)
        self.slave_writers[slave_num] = path
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
        except Exception:
            pass

        now_t = time.time()
        last_key = f"last_csv_write_{slave_num}"
        last_t = getattr(self, last_key, 0)

        if now_t - last_t < float(self.log_time):
            return

        setattr(self, last_key, now_t)

        now = datetime.datetime.now()
        date = datetime.date.today().strftime("%d-%m-%Y")
        ts = now.strftime("%H:%M:%S")
        row = [date, ts] + [(f"{v:.1f}" if isinstance(v, (int, float)) else "") for v in scaled]

        # Channel OFF → empty in CSV
        for i in range(24):
            try:
                if not getattr(self.ui, f"CH{i + 1:02d}Check").isChecked():
                    row[i + 2] = ""
            except:
                pass

        row = [("" if (v == 0 or v == 0.0 or v == "0") else v) for v in row]

        try:
            with open(path, "a", newline="") as f:
                csv.writer(f).writerow(row)
        except Exception as e:
            self.show_toast(
                f"CSV write failed for Slave {slave_num} — data for this "
                f"reading was NOT saved. Check disk space / file access.",
                level="error", duration=6000,
            )

        # ── DB write (mirror of CSV write) ──
        try:
            write_row(
                slave_id=slave_num,
                date=date,
                time_str=ts,
                values=[v if v != "" else None for v in scaled],
            )
        except Exception as e:
            pass

        # ── Tables + graphs: only for selected slave, only at CSV write time ──
        if slave_num == selected:
            self.ui.Start.setEnabled(False)  # ← moved here, only runs at log_time rate
            self.update_csv_tab(scaled)
            self.update_csv_tab10(scaled)
            self.update_graph()
            self.update_graph10()

    def _attach_live_legends(self):
        """Re-parent legend boxes after plot.clear() so they stay visible
        and interactive. Hide a legend when it has no entries (prevents
        the empty black square next to CH1-CH8)."""
        for _lg in (
            getattr(self, "live_legend1", None),
            getattr(self, "live_legend2", None),
        ):
            if _lg is None:
                continue
            try:
                _lg.setParentItem(self.plot_widget.graphicsItem())
            except Exception:
                pass
            try:
                has_items = bool(getattr(_lg, "items", None)) and len(_lg.items) > 0
                _lg.setVisible(has_items)
            except Exception:
                pass

    def _rebuild_live_legends(self):
        """Clear both legends and re-add every active live curve.
        More reliable than incremental add/remove which left the legend
        stuck/inactive after clear() or failed removeItem calls."""
        for _lg in (
            getattr(self, "live_legend1", None),
            getattr(self, "live_legend2", None),
        ):
            if _lg is not None:
                try:
                    _lg.clear()
                except Exception:
                    pass
        curves = getattr(self, "_live_curves", {}) or {}
        for i, curve in list(curves.items()):
            target = (
                getattr(self, "live_legend1", None)
                if i < 12
                else getattr(self, "live_legend2", None)
            )
            if target is None or curve is None:
                continue
            try:
                target.addItem(curve, f"CH{i + 1}")
            except Exception:
                pass
        self._attach_live_legends()

    def _show_graph_error(self, message):
        try:
            self.plot_widget.clear()
            self.plot_widget.setTitle(
                f"<span style='font-size:10pt;color:#ff4c4c'>{message}</span>"
            )
            # clear() just wiped every curve out from under _live_curves --
            # drop our bookkeeping (and any now-stale legend entries) so
            # the next update_graph() rebuilds from a clean slate instead
            # of trying to update PlotDataItems that no longer exist.
            self._live_curves = {}
            for _lg in (getattr(self, "live_legend1", None), getattr(self, "live_legend2", None)):
                if _lg is not None:
                    _lg.clear()
            self._attach_live_legends()
        except:
            pass

        try:
            self.plot_widget10.clear()
            self.plot_widget10.setTitle(
                f"<span style='font-size:10pt;color:#ff4c4c'>{message}</span>"
            )
        except:
            pass

    def handle_slave_error(self, slave_num, message):
        if message == "":
            write_event("SYSTEM", "SLAVE_RECOVERED", f"Slave {slave_num} recovered")
            return

        write_event("SYSTEM", "SLAVE_ERROR", f"Slave {slave_num}: {message}")

        if slave_num == getattr(self, "selected_slave", 1):
            self._show_graph_error(message)
            self.statusBar().showMessage(f"⚠ Slave {slave_num}: {message}", 5000)

    def csv_writer_start_all(self, slave_configs):
        self.slave_writers = {}
        for sc in slave_configs:
            n = sc["num"]
            path = self.get_slave_csv_path(n)
            if not os.path.exists(path):
                open(path, "w").close()
            self.slave_writers[n] = path

    # ----------- Stop Communication ----------
    def stop_worker(self):
        write_event("ADMIN", "STOP", "Temperature recording stopped")
        # Stop Worker thread
        if hasattr(self, "worker") and self.worker is not None:
            self.worker.stop()
            self.worker = None
            self.update_comm_status("idle")

        # Stop csv_writer and clear slave writers
        self.csv_writer.stop()
        if hasattr(self, "slave_writers"):
            self.slave_writers = {}

        # Reset per-slave write timers
        for i in range(1, 9):
            if hasattr(self, f"last_csv_write_{i}"):
                delattr(self, f"last_csv_write_{i}")

        # Reset latest data
        self.latest_scaled_rr = None
        if hasattr(self, "_slave_latest"):
            self._slave_latest = {}

        # Clear all LCD displays
        for i in range(1, 25):
            try:
                getattr(self.ui, f"lcdNumber_{i:02d}").display(0)
            except:
                pass

        # Clear data table
        if hasattr(self, "csv_table_widget"):
            self.csv_table_widget.setRowCount(0)

        # Clear last 10 table
        if hasattr(self, "csv_table_widget1"):
            self.csv_table_widget1.setRowCount(0)

        # Clear pyqtgraph plots (your graphs use plot_widget, not matplotlib figure)
        try:
            self.plot_widget.clear()
            self._live_curves = {}
            for _lg in (getattr(self, "live_legend1", None), getattr(self, "live_legend2", None)):
                if _lg is not None:
                    _lg.clear()
            self.plot_widget.setTitle(
                f"Graph (ID-{self.selected_slave})",
                color="#00A0E3",
            )
        except:
            pass
        try:
            self.plot_widget10.clear()
            self.plot_widget10.setTitle(
                f"Last 10 Readings (ID-{self.selected_slave})",
                color="#00A0E3",
            )
        except:
            pass

        self._show_graph_error("System Stopped — Press Start to begin")

        # Re-enable all settings inputs
        self.ui.Start.setEnabled(True)
        self.ui.COMport.setEnabled(True)
        self.ui.Baud.setEnabled(True)
        self.ui.ParityType.setEnabled(True)
        self.ui.StartBitOpt.setEnabled(True)
        self.ui.StopBitOpt.setEnabled(True)
        self.ui.Slave.setEnabled(True)
        self.ui.Save.setEnabled(True)
        self.ui.IDSetting.setEnabled(True)

        # Reset slave dropdown back to index 0 (Slave 1)
        try:
            self.ui.Slave.setCurrentIndex(0)
            self.selected_slave = 1
        except:
            pass

        self.save_config()
        self.show_message(
            "Stopped", "Logging stopped.\nSystem reset to initial state.", "#02c702"
        )
        self.stop_record_indicator()

        # Stop the telemetry update timer so LCDs don't keep showing old values
        if hasattr(self, "telemetry_timer"):
            self.telemetry_timer.stop()
            self.telemetry_timer.start(
                100
            )  # restart — it'll return immediately since latest_scaled_rr = None

        # Reload config so dropdowns show last-saved values
        self.load_config()

    def save_slave_selection(self):
        selected = int(self.ui.Slave.currentText().strip())

        # Check if this slave is actually enabled in ID Settings
        if not getattr(self, f"slave_enabled_{selected}", False):
            self.show_message(
                "Invalid Selection",
                f"Slave ID-{selected} is not enabled in ID Settings!\n\nPlease enable it first via ID Settings.",
                "#ff4c4c",
            )
            # Reset dropdown back to currently active slave (don't change selection)
            try:
                self.ui.Slave.setCurrentIndex(self.selected_slave - 1)
            except:
                pass
            return

        # Valid — proceed as normal
        self.selected_slave = selected
        
        self.plot_widget.setTitle(
            f"Graph (ID-{self.selected_slave})",
            color="#00A0E3",
        )

        self.plot_widget10.setTitle(
            f"Last 10 Readings (ID-{self.selected_slave})",
            color="#00A0E3",
        )
        
        self.y_axis_text = getattr(self, f"y_axis_text_{self.selected_slave}", "")
        self.save_config()
        self.display_csv()
        self.display_csv10()
        self.plot_last_10_readings()
        self.plot_graph()
        self.update_all_y_axis_labels()
        self.show_message(
            "Saved", f"Displaying data for Slave ID-{self.selected_slave}", "#02c702"
        )
        self.ui.groupBox.setTitle(f"Telemetry Data ID-{self.selected_slave}")
        self.update_channel_icons(self.selected_slave)
        self.refresh_telemetry()
        
    def refresh_telemetry(self):
        if not hasattr(self, "_slave_latest"):
            return

        rr = self._slave_latest.get(self.selected_slave)
        if rr is None:
            return

        self.latest_scaled_rr = rr
        for i in range(24):
            try:
                value = rr[i]
                lcd = getattr(self.ui, f"lcdNumber_{i+1:02d}")
                if value is None:
                    lcd.display("OPE")
                else:
                    lcd.display(value)
            except Exception:
                pass

    def update_channel_icons(self, slave_num):
        text = getattr(self, f"y_axis_text_{slave_num}", "").strip().lower()

        if not text:  # blank → clear all icons
            for i in range(1, 25):
                try:
                    getattr(self.ui, f"CH{i:02d}Temp").clear()
                except AttributeError:
                    pass
            return

        if "temp" in text:
            icon_path = ":/ico/icons/high-temperature.png"
        elif "pressure" in text:
            icon_path = ":/ico/icons/pressure.png"
        elif "humid" in text:
            icon_path = ":/ico/icons/humidity.png"
        elif "speed" in text:
            icon_path = ":/ico/icons/speed.png"
        elif "kwh" in text or "energy" in text:
            icon_path = ":/ico/icons/energy.png"
        else:
            icon_path = ":/ico/icons/high-temperature.png"

        for i in range(1, 25):
            try:
                label = getattr(self.ui, f"CH{i:02d}Temp")
                if icon_path:
                    pixmap = QPixmap(icon_path).scaled(
                        24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                    label.setPixmap(pixmap)
                else:
                    label.clear()
            except AttributeError:
                pass

    def get_slave_csv_path(self, slave_num):
        today = datetime.date.today().strftime("%d-%m-%Y")
        folder = os.path.join("Scanner_Files", today)
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, f"{today}_ID_{slave_num}.csv")

    def get_selected_slave_csv_path(self):
        return self.get_slave_csv_path(getattr(self, "selected_slave", 1))

    # ---------- Center Login Page -----------
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # ---------- Update Time Conti.. --------------
    def update_time(self):
        date = datetime.date.today()
        self.ui.dateEdit.setDate(date)
        now = datetime.datetime.now()
        current_time = QTime(now.hour, now.minute, now.second)
        self.ui.timeEdit.setTime(current_time)

    # ------------ Load last config --------------
    def load_config(self):
        # Disconnect signals first to prevent save_config firing during restore
        try:
            self.ui.COMport.currentTextChanged.disconnect(self.save_config)
            self.ui.Baud.currentTextChanged.disconnect(self.save_config)
            self.ui.ParityType.currentTextChanged.disconnect(self.save_config)
            self.ui.StartBitOpt.currentTextChanged.disconnect(self.save_config)
            self.ui.StopBitOpt.currentTextChanged.disconnect(self.save_config)
        except:
            pass  # not yet connected on first load — fine

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)

            self.com = config.get("com", "").strip()  # strip spaces
            self.baud = config.get("baud", "").strip()
            self.parity = config.get("parity", "N").strip()
            self.data_bits = config.get("data_bits", "8").strip()
            self.stop_bits = config.get("stop_bits", "1").strip()
            self.log_time = float(config.get("log_time", 2.0))
            self.div_factor = config.get("div_factor_1", "10")
            self.csv_filepath = config.get("csv_filepath", "")
            self.start_time = config.get("start_time", "")
            self.end_time = config.get("end_time", "")
            self.start_date = config.get("start_date", "")
            self.end_date = config.get("end_date", "")
            self.letterhead_file = config.get("letterhead_file", "")
            self.header = config.get("header", "")
            self.folder_id = config.get("folder_id", "")
            self.company_name = config.get("company_name", "")
            selected = int(config.get("selected_slave", 1))
            self.y_axis_text = config.get(f"y_axis_text_{selected}", "").strip()
            self.last_update_check = config.get("last_update_check", "")

            for i in range(1, 9):
                setattr(self, f"div_factor_{i}", config.get(f"div_factor_{i}", ""))
                setattr(self, f"y_axis_text_{i}", config.get(f"y_axis_text_{i}", ""))
                setattr(self, f"address_{i}", config.get(f"address_{i}", ""))
                setattr(
                    self, f"slave_enabled_{i}", config.get(f"slave_enabled_{i}", False)
                )

            self.selected_slave = int(config.get("selected_slave", 1))
            slave_index = self.selected_slave - 1  # dropdown is 0-indexed
            self.ui.Slave.setCurrentIndex(slave_index)
            self.ui.groupBox.setTitle(f"Telemetry Data ID-{self.selected_slave}")
            self.update_channel_icons(self.selected_slave)

            saved_company = config.get("company_name", "").strip()

            if saved_company:
                self.ui.lineEdit_4.setText(saved_company)
                self.ui.lineEdit_4.setReadOnly(True)
                self.company_name = saved_company
            else:
                self.ui.lineEdit_4.setText("")
                self.ui.lineEdit_4.setReadOnly(False)

            for i in range(1, 25):
                ch_value = config.get(f"ch{i:02d}", False)
                setattr(self, f"ch{i:02d}", ch_value)
                checkbox = getattr(self.ui, f"CH{i:02d}Check")
                checkbox.setChecked(ch_value)


            # Restore COM port
            if self.com:
                index = self.ui.COMport.findText(self.com, Qt.MatchContains)
                if index != -1:
                    self.ui.COMport.setCurrentIndex(index)

            # Restore Baud rate
            if self.baud:
                index = self.ui.Baud.findText(self.baud, Qt.MatchContains)
                if index != -1:
                    self.ui.Baud.setCurrentIndex(index)

            # Restore Parity
            if self.parity:
                index = self.ui.ParityType.findText(self.parity, Qt.MatchContains)
                if index != -1:
                    self.ui.ParityType.setCurrentIndex(index)

            # Restore Data Bits
            if self.data_bits:
                index = self.ui.StartBitOpt.findText(self.data_bits, Qt.MatchContains)
                if index != -1:
                    self.ui.StartBitOpt.setCurrentIndex(index)

            # Restore Stop Bits
            if self.stop_bits:
                index = self.ui.StopBitOpt.findText(self.stop_bits, Qt.MatchContains)
                if index != -1:
                    self.ui.StopBitOpt.setCurrentIndex(index)

        else:
            self.com = ""
            self.baud = ""
            self.parity = "N"
            self.data_bits = "8"
            self.stop_bits = "1"
            self.log_time = 2.0
            self.div_factor = "10"
            self.csv_filepath = ""
            self.start_time = ""
            self.end_time = ""
            self.start_date = ""
            self.end_date = ""
            self.letterhead_file = ""
            self.header = ""
            self.folder_id = ""
            self.y_axis_text = ""
            self.company_name = ""
            for i in range(1, 9):
                setattr(self, f"div_factor_{i}", "")
                setattr(self, f"y_axis_text_{i}", "")
                setattr(self, f"address_{i}", "")
                setattr(self, f"slave_enabled_{i}", False)
            self.selected_slave = 1
            self.ui.Slave.setCurrentIndex(0)
            self.ui.groupBox.setTitle("Telemetry Data ID-1")
            self.update_channel_icons(1)

            for i in range(1, 25):
                setattr(self, f"ch{i:02d}", False)
            self.save_config()

        # Reconnect signals AFTER all restores are done
        self.ui.COMport.currentTextChanged.connect(self.save_config)
        self.ui.Baud.currentTextChanged.connect(self.save_config)
        self.ui.ParityType.currentTextChanged.connect(self.save_config)
        self.ui.StartBitOpt.currentTextChanged.connect(self.save_config)
        self.ui.StopBitOpt.currentTextChanged.connect(self.save_config)
        for i in range(1, 25):
            checkbox = getattr(self.ui, f"CH{i:02d}Check")
            checkbox.stateChanged.connect(self.save_config)

    # ------------- Save Last config --------------
    def save_config(self):
        self.com = self.ui.COMport.currentText().strip()  # strip here
        self.baud = self.ui.Baud.currentText().strip()
        self.parity = self.ui.ParityType.currentText().strip()
        self.data_bits = self.ui.StartBitOpt.currentText().strip()
        self.stop_bits = self.ui.StopBitOpt.currentText().strip()

        existing = {}
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as _f:
                existing = json.load(_f)

        for i in range(1, 25):
            checkbox = getattr(self.ui, f"CH{i:02d}Check")
            setattr(self, f"ch{i:02d}", checkbox.isChecked())

        company_text = self.ui.lineEdit_4.text().strip()

        if company_text:
            self.company_name = company_text

        config = {
            "com": self.com,
            "baud": self.baud,
            "parity": self.parity,
            "data_bits": self.data_bits,
            "stop_bits": self.stop_bits,
            "log_time": existing.get("log_time", self.log_time),
            "csv_filepath": self.csv_filepath,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "letterhead_file": self.letterhead_file,
            "header": self.header,
            "folder_id": self.folder_id,
            "company_name": self.company_name,
            "last_update_check": self.last_update_check if hasattr(self, "last_update_check") else "" ,
        }

        for i in range(1, 9):
            config[f"div_factor_{i}"] = existing.get(
                f"div_factor_{i}", getattr(self, f"div_factor_{i}", "")
            )
            config[f"y_axis_text_{i}"] = existing.get(
                f"y_axis_text_{i}", getattr(self, f"y_axis_text_{i}", "")
            )
            config[f"address_{i}"] = existing.get(
                f"address_{i}", getattr(self, f"address_{i}", "")
            )
            config[f"slave_enabled_{i}"] = existing.get(
                f"slave_enabled_{i}", getattr(self, f"slave_enabled_{i}", False)
            )

        config["selected_slave"] = getattr(self, "selected_slave", 1)

        for i in range(1, 25):
            config[f"ch{i:02d}"] = getattr(self, f"ch{i:02d}", False)

        atomic_write_json(CONFIG_FILE, config)
        write_event("ADMIN", "SETTINGS", "Configuration Updated")

    # ------------- Display in CSV Tab -------------
    def display_csv(self):
        if not hasattr(self, "csv_table_widget"):
            frame_layout = QVBoxLayout()
            self.csv_table_widget = QTableWidget()
            self.csv_table_widget.setRowCount(0)
            self.csv_table_widget.setColumnCount(26)
            fieldnames = [
                "DATE",
                "TIME",
                "CH01",
                "CH02",
                "CH03",
                "CH04",
                "CH05",
                "CH06",
                "CH07",
                "CH08",
                "CH09",
                "CH10",
                "CH11",
                "CH12",
                "CH13",
                "CH14",
                "CH15",
                "CH16",
                "CH17",
                "CH18",
                "CH19",
                "CH20",
                "CH21",
                "CH22",
                "CH23",
                "CH24",
            ]
            self.csv_table_widget.setHorizontalHeaderLabels(fieldnames)
            header = self.csv_table_widget.horizontalHeader()
            header.setStyleSheet(
                "color: black; background-color: white; font-weight: bold;"
            )
            header1 = self.csv_table_widget.verticalHeader()
            header1.setStyleSheet(
                "color: black; background-color: white; font-weight: bold;"
            )
            self.csv_table_widget.resizeColumnsToContents()
            self.csv_table_widget.setAutoScroll(True)

            column_widths = [
                90,
                90,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
            ]
            for col, width in enumerate(column_widths):
                self.csv_table_widget.setColumnWidth(col, width)

            self.csv_table_widget.setStyleSheet(
                "QTableWidget { color: black; background-color: white; }"
            )
            frame_layout.addWidget(self.csv_table_widget)
            self.ui.allcsv.setLayout(frame_layout)
        else:
            self.csv_table_widget.clearContents()
            self.csv_table_widget.setRowCount(0)

        today_date = datetime.date.today().strftime("%d-%m-%Y")
        file_path = self.get_selected_slave_csv_path()
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)

        font = QFont()
        font.setPointSize(9)

        # Live DATA/CSV tables must only show rows that belong to today.
        # Any foreign-date rows (e.g. leftover from a midnight crossover
        # before the path fix, or a file that was manually mixed) are skipped.
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            display_row = 0
            for row_data in reader:
                if not row_data:
                    continue
                # Skip rows whose date column is not today
                if str(row_data[0]).strip() != today_date:
                    continue
                if display_row >= self.csv_table_widget.rowCount():
                    self.csv_table_widget.insertRow(display_row)
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(col_data)
                    if col_idx in range(2, 26):
                        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    if col_idx in [0, 1]:
                        item.setFont(font)
                    self.csv_table_widget.setItem(display_row, col_idx, item)
                display_row += 1

        QTimer.singleShot(0, self.csv_table_widget.scrollToBottom)

    # -------------- Conti. Updating CSV Tab and CSV File --------------
    def update_csv_tab(self, rr=None):
        if rr is None:
            return

        if not hasattr(self, "csv_table_widget"):
            return

        now = datetime.datetime.now()
        date = datetime.date.today().strftime("%d-%m-%Y")
        ts = now.strftime("%H:%M:%S")

        scaled_rr = []
        for i in range(24):
            try:
                v = rr[i]
                checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
                if not checkbox or v is None:
                    scaled_rr.append("")
                # elif float(v) > 15000:
                elif float(v) < -200 or float(v) > 2000:
                    scaled_rr.append("")
                else:
                    scaled_rr.append(v)
            except:
                scaled_rr.append("")

        data = [date, ts] + scaled_rr
        data = [("" if (v == 0 or v == 0.0 or v == "0") else v) for v in data]

        font = QFont()
        font.setPointSize(9)
        row_idx = self.csv_table_widget.rowCount()
        self.csv_table_widget.insertRow(row_idx)
        for col_idx, reg in enumerate(data):
            item = QTableWidgetItem(str(reg))
            if col_idx in range(2, 26):
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            if col_idx in [0, 1]:
                item.setFont(font)
            self.csv_table_widget.setItem(row_idx, col_idx, item)

        self.update_graph()
        self.update_graph10()

    # -------------- last 10 data Display as CSV -------------
    def display_csv10(self):
        if not hasattr(self, "csv_table_widget1"):
            frame_layout = QVBoxLayout()
            self.csv_table_widget1 = QTableWidget()
            self.csv_table_widget1.setRowCount(0)
            self.csv_table_widget1.setColumnCount(26)
            fieldnames = [
                "DATE",
                "TIME",
                "CH01",
                "CH02",
                "CH03",
                "CH04",
                "CH05",
                "CH06",
                "CH07",
                "CH08",
                "CH09",
                "CH10",
                "CH11",
                "CH12",
                "CH13",
                "CH14",
                "CH15",
                "CH16",
                "CH17",
                "CH18",
                "CH19",
                "CH20",
                "CH21",
                "CH22",
                "CH23",
                "CH24",
            ]
            self.csv_table_widget1.setHorizontalHeaderLabels(fieldnames)

            header = self.csv_table_widget1.horizontalHeader()
            header.setStyleSheet(
                "color: black; background-color: white; font-weight: bold; font-size: 16px;"
            )

            header1 = self.csv_table_widget1.verticalHeader()
            header1.setStyleSheet(
                "color: black; background-color: white; font-weight: bold; font-size: 16px;"
            )

            self.csv_table_widget1.resizeColumnsToContents()
            self.csv_table_widget1.setAutoScroll(True)

            column_widths = [
                90,
                86,
                40,
                40,
                40,
                40,
                40,
                40,
                40,
                40,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
                70,
            ]
            for col, width in enumerate(column_widths):
                self.csv_table_widget1.setColumnWidth(col, width)

            self.csv_table_widget1.setStyleSheet(
                "QTableWidget { background-color: white; }"
            )
            frame_layout.addWidget(self.csv_table_widget1)
            self.ui.csv10.setLayout(frame_layout)
        else:
            self.csv_table_widget1.clearContents()
            self.csv_table_widget1.setRowCount(0)

        today_date = datetime.date.today().strftime("%d-%m-%Y")
        file_path = self.get_selected_slave_csv_path()
        if not os.path.exists(file_path):
            with open(file_path, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(fieldnames)
                zero_row = [today_date, "00:00:00"] + ["0"] * 24
                writer.writerow(zero_row)

        font = QFont()
        font.setPointSize(9)
        black_brush = QBrush(Qt.black)

        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            # Keep only today's rows, then the last 10 of those
            rows = [
                r for r in reader
                if r and str(r[0]).strip() == today_date
            ]
            if len(rows) > 10:
                rows = rows[-10:]

            for row_idx, row_data in enumerate(rows):
                if row_idx >= self.csv_table_widget1.rowCount():
                    self.csv_table_widget1.insertRow(row_idx)
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(col_data)
                    item.setForeground(black_brush)
                    if col_idx in range(2, 26):
                        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    if col_idx in [0, 1]:
                        item.setFont(font)
                    self.csv_table_widget1.setItem(row_idx, col_idx, item)

        QTimer.singleShot(0, self.csv_table_widget1.scrollToBottom)

    # -------------- Conti. Updating last 10 data as CSV --------------
    def update_csv_tab10(self, rr=None):
        if rr is None:
            return

        if not hasattr(self, "csv_table_widget1"):
            return

        now = datetime.datetime.now()
        date = datetime.date.today().strftime("%d-%m-%Y")
        ts = now.strftime("%H:%M:%S")

        scaled_rr = []
        for i in range(24):
            try:
                v = rr[i]
                checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
                if not checkbox or v is None:
                    scaled_rr.append("")
                # elif float(v) > 15000:
                elif float(v) < -200 or float(v) > 2000:
                    scaled_rr.append("")
                else:
                    scaled_rr.append(v)
            except:
                scaled_rr.append("")

        data = [date, ts] + scaled_rr
        data = [("" if (v == 0 or v == 0.0 or v == "0") else v) for v in data]

        font = QFont()
        font.setPointSize(9)
        black_brush = QBrush(Qt.black)

        row_idx = self.csv_table_widget1.rowCount()
        self.csv_table_widget1.insertRow(row_idx)
        for col_idx, reg in enumerate(data):
            item = QTableWidgetItem(str(reg))
            item.setForeground(black_brush)
            if col_idx in range(2, 26):
                item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            if col_idx in [0, 1]:
                item.setFont(font)
            self.csv_table_widget1.setItem(row_idx, col_idx, item)

        # keep only last 10 rows
        if self.csv_table_widget1.rowCount() > 10:
            self.csv_table_widget1.removeRow(0)

    # ---------- convert time str to float ----------
    def time_str_to_float(self, time_str):
        try:
            parts = time_str.split(":")
            if len(parts) != 3:
                raise ValueError(f"Invalid time format: {time_str}")
            hours, minutes, seconds = map(int, parts)
            total_hours = hours + minutes / 60.0 + seconds / 3600.0
            return total_hours
        except FileNotFoundError as e:
            return np.nan
        except ValueError as e:
            return np.nan
        except Exception as e:
            return np.nan

    # --------- for read CSV data -----------
    def read_csv_data(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        if os.stat(file_path).st_size == 0:
            raise ValueError(f"File '{file_path}' is empty.")
        raw_data = np.genfromtxt(file_path, delimiter=",", skip_header=1, dtype=str)

        if raw_data.ndim != 2:
            raise ValueError(
                f"Unexpected data format in '{file_path}'. Expected 2-dimensional array."
            )

        date_strings = raw_data[:, 0]
        time_strings = raw_data[:, 1]
        time_data = np.array([self.time_str_to_float(t) for t in raw_data[:, 1]])
        sensor_data = []

        for col in raw_data[:, 2:].T:
            col_data = []
            for v in col:
                if v == "" or v is None:
                    col_data.append(np.nan)
                else:
                    try:
                        col_data.append(float(v))
                    except ValueError:
                        col_data.append(np.nan)
            sensor_data.append(col_data)

        sensor_data = np.array(sensor_data)
        return date_strings, time_strings, time_data, sensor_data

    # ---------- for plot Main Graph -----------
    def plot_graph(self):
        today_date = datetime.date.today().strftime("%d-%m-%Y")
        file_path = self.get_selected_slave_csv_path()

        if not os.path.exists(file_path):
            return

        try:
            date_strings, time_strings, time_data, data = self.read_csv_data(file_path)
        except (FileNotFoundError, ValueError) as e:
            date_strings = [today_date]
            time_strings = ["00:00:00"]
            time_data = [0.0]
            data = np.zeros((24, 1))
            return

        time_data = np.array(time_data, dtype=np.float64)
        data = np.array(data, dtype=np.float64)

        plot_widget = pg.PlotWidget()
        plot_widget.setFixedWidth(1360)

        font = QFont()
        font.setPixelSize(12)
        axis = plot_widget.getAxis("bottom")
        axis.setTickFont(font)
        axis.setStyle(tickTextOffset=10)

        # ----------- Determine minor_interval ---------
        time_range = pd.to_datetime(time_strings[-1]) - pd.to_datetime(time_strings[0])
        total_minutes = int(time_range.total_seconds() / 60)

        if total_minutes <= 60:
            minor_interval = 1
        elif total_minutes <= 120:
            minor_interval = 2
        elif total_minutes <= 300:
            minor_interval = 5
        elif total_minutes <= 600:
            minor_interval = 10
        else:
            minor_interval = 30

        tick_indices = range(0, len(time_strings), minor_interval)
        tick_labels = {
            time_data[i]: f"{time_strings[i]}\n{date_strings[i]}" for i in tick_indices
        }
        ticks = [(value, tick_labels[value]) for value in sorted(tick_labels.keys())]
        axis.setTicks([ticks])

        # Re-use the single pair of live legends created in startMain.
        # Creating extra LegendItems here used to leave 4 legend boxes
        # on the same plot (the classic "4 legends" bug).
        for _lg in (
            getattr(self, "live_legend1", None),
            getattr(self, "live_legend2", None),
        ):
            if _lg is not None:
                try:
                    _lg.clear()
                except Exception:
                    pass
        self._live_curves = {}

        colors = [
            "#FF0000",
            "#3CB44B",
            "#FFE100",
            "#0000FF",
            "#F58231",
            "#911EB4",
            "#46F0F0",
            "#FF1493",
            "#000075",
            "#800000",
            "#AA6E28",
            "#E6BEFF",
            "#2F6324",
            "#FFB6C1",
            "#7B68EE",
            "#008080",
            "#808000",
            "#00FA9A",
            "#1E90FF",
            "#808080",
            "#BCF60C",
            "#FFFF00",
            "#FFA500",
            "#FF00FF",
        ]

        # Plotting — use live_legend1 (CH1-12) / live_legend2 (CH13-24)
        for i in range(0, 24):
            checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
            if not checkbox:
                continue

            x = []
            y = []
            for t, v in zip(time_data, data[i]):
                if v != "" and v is not None:
                    try:
                        y.append(float(v))
                        x.append(t)
                    except ValueError:
                        continue

            if not y:
                continue

            pen = pg.mkPen(color=colors[i], width=2)
            c = self.plot_widget.plot(x, y, pen=pen, name=f"CH{i + 1}")
            self._live_curves[i] = c
            target_legend = (
                self.live_legend1 if i < 12 else self.live_legend2
            )
            if target_legend is not None:
                target_legend.addItem(c, f"CH{i + 1}")

        self.update_all_y_axis_labels()
        self.plot_widget.setTitle(
            f"Graph (ID-{self.selected_slave})",
            color="#00A0E3",
        )
        self.plot_widget.setLabel(
            "left",
            f'<span style="color:#00A0E3; font-weight:bold; font-size:11px;">{self.y_axis_text}</span>',
            justify="center",
        )
        self.plot_widget.setLabel(
            "bottom",
            '<span style="color:#00A0E3; font-weight:bold;">Date & Time</span>',
            justify="center",
        )
        self.plot_widget.showGrid(x=True, y=True, alpha=0.8)

    # -------- for conti.. update Main Graph ----------
    def update_graph(self):
        today_date = datetime.date.today().strftime("%d-%m-%Y")
        file_path = self.get_selected_slave_csv_path()

        try:
            date_strings, time_strings, time_data, data = self.read_csv_data(file_path)
        except (FileNotFoundError, ValueError) as e:
            return

        if not os.path.exists(file_path):
            return
        if self.plot_widget is None:
            return

        # Curves are added/removed/updated individually below instead of
        # calling self.plot_widget.clear() every reading -- clear() wiped
        # every curve (and detached the legend's entries) each time, so a
        # channel you'd just unchecked would get its legend entry rebuilt
        # from scratch and reappear the moment the NEXT reading came in.
        if not hasattr(self, "_live_curves"):
            self._live_curves = {}
        time_data = np.array(time_data, dtype=np.float64)
        data = np.array(data, dtype=np.float64)

        num_points = len(time_strings)

        # Tick step based on the plot's actual current pixel width instead
        # of a fixed stride of 16 -- a fixed stride overlaps once the
        # window is narrower than ~16*85px, and never adapts as it's
        # resized.
        widget_width_px = max(1, self.plot_widget.width())
        max_ticks_that_fit = max(3, widget_width_px // 85)
        tick_step = max(1, -(-num_points // max_ticks_that_fit))  # ceil div
        tick_indices = range(0, num_points, tick_step)
        ticks = [
            (time_data[i], f"{time_strings[i]}\n{date_strings[i]}")
            for i in tick_indices
        ]

        axis = self.plot_widget.getAxis("bottom")
        axis.setTicks([ticks])
        axis.setRange(min(time_data), max(time_data))

        colors = [
            "#FF0000",
            "#3CB44B",
            "#FFE100",
            "#0000FF",
            "#F58231",
            "#911EB4",
            "#46F0F0",
            "#FF1493",
            "#000075",
            "#800000",
            "#AA6E28",
            "#E6BEFF",
            "#2F6324",
            "#FFB6C1",
            "#7B68EE",
            "#008080",
            "#808000",
            "#00FA9A",
            "#1E90FF",
            "#808080",
            "#BCF60C",
            "#FFFF00",
            "#FFA500",
            "#FF00FF",
        ]

        # Plot each channel with a unique color -- add/update/remove only
        # what actually changed, so unchecked channels stay gone and their
        # legend entry (in legend1 for CH1-12, legend2 for CH13-24) is
        # explicitly removed rather than relying on a rebuild.
        for i in range(data.shape[0]):
            checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
            ch_name = f"CH{i + 1}"
            target_legend = self.live_legend1 if i < 12 else self.live_legend2

            has_data = not np.all((data[i] == "") | np.isnan(data[i]))

            if not checkbox or not has_data:
                existing = self._live_curves.pop(i, None)
                if existing is not None:
                    self.plot_widget.removeItem(existing)
                continue

            y = []
            x = []

            for t, v in zip(time_data, data[i]):
                if v != "" and not np.isnan(v):
                    x.append(t)
                    y.append(v)

            if len(y) == 0:
                existing = self._live_curves.pop(i, None)
                if existing is not None:
                    self.plot_widget.removeItem(existing)
                continue

            pen = pg.mkPen(color=colors[i], width=2)
            if i in self._live_curves:
                self._live_curves[i].setData(x, y, pen=pen)
            else:
                curve = self.plot_widget.plot(x, y, pen=pen, name=ch_name)
                self._live_curves[i] = curve

        # Rebuild legend from the curves that are actually on the plot.
        # Incremental add/remove left the legend inactive after clear() and
        # left an empty black box (legend2) when only CH1-CH8 were active.
        self._rebuild_live_legends()

        self.update_all_y_axis_labels()
        # --------- Customize plot appearance -----------
        self.plot_widget.showGrid(x=True, y=True, alpha=0.8)
        self.plot_widget.setBackground("w")
        self.plot_widget.getAxis("left").setTextPen("k")
        self.plot_widget.getAxis("bottom").setTextPen("k")
        self.plot_widget.getAxis("left").setPen("k")
        self.plot_widget.getAxis("bottom").setPen("k")
        self.plot_widget.setTitle(
            f"Graph (ID-{self.selected_slave})",
            color="#00A0E3",
        )
        self.plot_widget.setLabel(
            "left",
            f'<span style="color:#00A0E3; font-weight:bold; font-size:11px;">{self.y_axis_text}</span>',
            justify="center",
        )
        self.plot_widget.setLabel(
            "bottom",
            '<span style="color:#00A0E3; font-weight:bold;">Date & Time</span>',
            justify="center",
        )
        self.plot_widget.update()

    # --------- Read last 10 data from CSV ----------
    def read_csv10(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        if os.stat(file_path).st_size == 0:
            raise ValueError(f"File '{file_path}' is empty.")

        raw_data = np.genfromtxt(file_path, delimiter=",", skip_header=1, dtype=str)

        if raw_data.ndim != 2:
            raise ValueError(
                f"Unexpected data format in '{file_path}'. Expected 2-dimensional array."
            )

        date_strings = raw_data[:, 0]
        time_strings = raw_data[:, 1]
        time_data = np.array([self.time_str_to_float(t) for t in raw_data[:, 1]])
        sensor_data = []

        for col in raw_data[:, 2:].T:
            col_data = []
            for v in col:
                if v == "" or v is None:
                    col_data.append(np.nan)
                else:
                    try:
                        col_data.append(float(v))
                    except ValueError:
                        col_data.append(np.nan)
            sensor_data.append(col_data)
        sensor_data = np.array(sensor_data)
        return (
            date_strings[-10:],
            time_strings[-10:],
            time_data[-10:],
            sensor_data[:, -10:],
        )

    # ---------- plot graph of last 10 data -----------
    def plot_last_10_readings(self):
        today_date = datetime.date.today().strftime("%d-%m-%Y")
        file_path = self.get_selected_slave_csv_path()

        if not os.path.exists(file_path):
            return

        try:
            date_strings, time_strings, time_data, data = self.read_csv_data(file_path)
        except (FileNotFoundError, ValueError) as e:
            date_strings = [today_date]
            time_strings = ["00:00:00"]
            time_data = [0.0]
            data = np.zeros((24, 1))
            return

        if len(time_data) > 10:
            last_10_time_data = time_data[-10:]
            last_10_data = data[:, -10:]
        else:
            last_10_time_data = time_data
            last_10_data = data

        last_10_time_data = np.array(last_10_time_data, dtype=np.float64)
        last_10_data = np.array(last_10_data, dtype=np.float64)

        # Was missing entirely -- without clearing first, every refresh
        # just added more curves on top of the old ones instead of
        # replacing them, so a channel toggled off would never actually
        # disappear from the plot OR its legend (its old curve/legend
        # entry would just sit there forever).
        self.plot_widget10.clear()

        plot_widget10 = pg.PlotWidget()
        plot_widget10.setFixedWidth(650)

        font = QFont()
        font.setPixelSize(12)
        axis = plot_widget10.getAxis("bottom")
        axis.setTickFont(font)
        axis.setStyle(tickTextOffset=10)

        num_points = len(last_10_time_data)
        tick_spacing = max(1, num_points // 10)
        tick_indices = list(range(0, num_points, tick_spacing))

        tick_labels = {}
        for i in tick_indices:
            if i < num_points:
                tick_labels[last_10_time_data[i]] = (
                    f"{time_strings[i]}\n{date_strings[i]}"
                )

        colors = [
            "#FF0000",
            "#3CB44B",
            "#FFE100",
            "#0000FF",
            "#F58231",
            "#911EB4",
            "#46F0F0",
            "#FF1493",
            "#000075",
            "#800000",
            "#AA6E28",
            "#E6BEFF",
            "#2F6324",
            "#FFB6C1",
            "#7B68EE",
            "#008080",
            "#808000",
            "#00FA9A",
            "#1E90FF",
            "#808080",
            "#BCF60C",
            "#FFFF00",
            "#FFA500",
            "#FF00FF",
        ]

        # Plotting
        for i in range(0, 12):
            checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
            if not checkbox:
                continue

            x, y = [], []
            for t, v in zip(last_10_time_data, last_10_data[i]):
                if not np.isnan(v):
                    x.append(t)
                    y.append(v)

            if not y:
                continue

            pen = pg.mkPen(color=colors[i], width=2)
            self.plot_widget10.plot(x, y, pen=pen, name=f"CH{i + 1}")
        for i in range(12, 24):
            checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
            if not checkbox:
                continue

            x, y = [], []
            for t, v in zip(last_10_time_data, last_10_data[i]):
                if not np.isnan(v):
                    x.append(t)
                    y.append(v)

            if not y:
                continue

            pen = pg.mkPen(color=colors[i], width=2)
            self.plot_widget10.plot(x, y, pen=pen, name=f"CH{i + 1}")
        self.update_all_y_axis_labels()
        self.plot_widget10.showGrid(x=True, y=True, alpha=0.8)
        self.plot_widget10.setBackground("w")
        self.plot_widget10.getAxis("left").setTextPen("k")
        self.plot_widget10.getAxis("bottom").setTextPen("k")
        self.plot_widget10.getAxis("left").setPen("k")
        self.plot_widget10.getAxis("bottom").setPen("k")
        self.plot_widget10.setTitle(
            f"Last 10 Readings (ID-{self.selected_slave})",
            color="#00A0E3",
        )
        _yt = self.y_axis_text.strip() if hasattr(self, "y_axis_text") else ""
        self.plot_widget10.setLabel(
            "left",
            f'<span style="color:#00A0E3; font-weight:bold;">{_yt}</span>',
            justify="center",
        )
        self.plot_widget10.setLabel(
            "bottom",
            '<span style="color:#00A0E3; font-weight:bold;">Date & Time</span>',
            justify="center",
        )

    # ----------- conti.. update Graph of last 10 data ----------
    def update_graph10(self):
        today_date = datetime.date.today().strftime("%d-%m-%Y")
        file_path = self.get_selected_slave_csv_path()

        try:
            date_strings, time_strings, time_data, data = self.read_csv10(file_path)
        except (FileNotFoundError, ValueError) as e:
            return

        if not os.path.exists(file_path):
            return
        if self.plot_widget10 is None:
            return

        self.plot_widget10.clear()
        time_data = np.array(time_data, dtype=np.float64)
        data = np.array(data, dtype=np.float64)

        if len(time_data) > 10:
            last_10_time_data = time_data[-10:]
            last_10_data = data[:, -10:]
        else:
            last_10_time_data = time_data
            last_10_data = data

        last_10_time_data = np.array(last_10_time_data, dtype=np.float64)
        last_10_data = np.array(last_10_data, dtype=np.float64)

        font = QFont()
        font.setPixelSize(10)
        axis = self.plot_widget10.getAxis("bottom")
        axis.setTickFont(font)
        axis.setStyle(tickTextOffset=15)

        num_points = len(last_10_time_data)
        tick_spacing = max(1, num_points // 10)
        tick_indices = list(range(0, num_points, tick_spacing))

        tick_labels = {}
        for i in tick_indices:
            if i < num_points:
                tick_labels[last_10_time_data[i]] = (
                    f"{time_strings[i]}\n{date_strings[i]}"
                )
                ticks = [
                    (value, tick_labels[value]) for value in sorted(tick_labels.keys())
                ]
                axis.setTicks([ticks])

        colors = [
            "#FF0000",
            "#3CB44B",
            "#FFE100",
            "#0000FF",
            "#F58231",
            "#911EB4",
            "#46F0F0",
            "#FF1493",
            "#000075",
            "#800000",
            "#AA6E28",
            "#E6BEFF",
            "#2F6324",
            "#FFB6C1",
            "#7B68EE",
            "#008080",
            "#808000",
            "#00FA9A",
            "#1E90FF",
            "#808080",
            "#BCF60C",
            "#FFFF00",
            "#FFA500",
            "#FF00FF",
        ]

        # Plotting
        for i in range(data.shape[0]):
            checkbox = getattr(self.ui, f"CH{i + 1:02d}Check").isChecked()
            if not checkbox:
                continue
            x, y = [], []

            for t, v in zip(last_10_time_data, last_10_data[i]):
                if v == "" or v is None:
                    continue
                try:
                    y.append(float(v))
                    x.append(t)
                except ValueError:
                    continue

            if not y:
                continue
            pen = pg.mkPen(color=colors[i], width=2)
            self.plot_widget10.plot(x, y, pen=pen, name=f"CH{i + 1}")

        self.update_all_y_axis_labels()
        self.plot_widget10.showGrid(x=True, y=True, alpha=0.8)
        self.plot_widget10.setBackground("w")
        self.plot_widget10.getAxis("left").setTextPen("k")
        self.plot_widget10.getAxis("bottom").setTextPen("k")
        self.plot_widget10.getAxis("left").setPen("k")
        self.plot_widget10.getAxis("bottom").setPen("k")
        self.plot_widget10.setTitle(
            f"Last 10 Readings (ID-{self.selected_slave})",
            color="#00A0E3",
        )
        self.plot_widget10.setLabel(
            "left",
            f'<span style="color:#00A0E3; font-weight:bold;">{self.y_axis_text}</span>',
            justify="center",
        )
        self.plot_widget10.setLabel(
            "bottom",
            '<span style="color:#00A0E3; font-weight:bold;">Date & Time</span>',
            justify="center",
        )

    # ----------- Open Calibrate Window ------------
    # def run_calibration(self):
    #     self.blur_main()

    #     self.calib_window = QtWidgets.QMainWindow()
    #     self.calib_window.setMinimumSize(1400, 800)

    #     self.calib_ui = Ui_SigmaControls_4()
    #     self.calib_ui.setupUi(self.calib_window)
        
    #     # --- NEW CODE: Enforce UI Limits based on License ---
    #     for i in range(self.allowed_ids + 1, 9):
    #         suffix = f"_{i}" if i > 1 else ""
            
    #         # Disable anything matching standard PyQt5 auto-naming for restricted IDs
    #         for prefix in ["groupBox", "checkBox", "tab", "id", "slave", "ID", "Slave"]:
    #             widget = getattr(self.calib_ui, f"{prefix}{suffix}", None)
    #             if widget:
    #                 widget.setEnabled(False)
                    
    #             widget_no_us = getattr(self.calib_ui, f"{prefix}{i}", None)
    #             if widget_no_us:
    #                 widget_no_us.setEnabled(False)
    #     # ----------------------------------------------------

    #     self.calib_window.destroyed.connect(self.check_calibration_closed)

    #     self.calib_window.installEventFilter(self)
    #     self.calib_window.show()
    #     # self.unblur_main()

    # ----------- Open Calibrate Window ------------
    # ----------- Open Calibrate Window ------------
    def _show_license_gating_message(self, cleared_ids):
        """Explain WHY slave IDs just got disabled, instead of doing it
        silently. Surfaces exactly which registry path was read, what was
        found there, and what plan that resolved to."""
        diag = getattr(self, "license_diag", {})
        reg_path = diag.get("reg_path", "(unknown)")
        customer = diag.get("customer", "")
        version_key = diag.get("version_key", "")
        matched_plan = diag.get("matched_plan")
        error = diag.get("error", "")

        id_list = ", ".join(f"ID-{i}" for i in cleared_ids)

        lines = [
            f"Slave IDs disabled because they exceed your licensed limit "
            f"of {self.allowed_ids}: {id_list}",
            "",
            f"Registry key checked: HKLM\\{reg_path}",
        ]
        if customer:
            lines.append(f"Customer on record: {customer}")
        if version_key:
            lines.append(f"Version key on record: {version_key}")
        if matched_plan:
            lines.append(f"This matched the {matched_plan}-ID plan.")
        if error:
            lines.append(f"Reason no higher plan matched: {error}")
        lines.append("")
        lines.append(
            "If you activated a higher-ID plan, re-run the license "
            "activation tool and confirm the Customer Name matches "
            "exactly (it's case-sensitive in the hash)."
        )

        self.show_message(
            "License Limit Applied",
            "\n".join(lines),
            "#ffb300",
        )

    def _enforce_license_limit_on_config(self):
        """Clear the slave_enabled_i flags for any Slave ID beyond
        self.allowed_ids, and warn if anything was actually cleared."""
        if not os.path.exists(CONFIG_FILE):
            return
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
            changed = False
            cleared_ids = []
            for i in range(self.allowed_ids + 1, 9):
                if config.get(f"slave_enabled_{i}", False):
                    config[f"slave_enabled_{i}"] = False
                    changed = True
                    cleared_ids.append(i)
            if changed:
                atomic_write_json(CONFIG_FILE, config)
                self._show_license_gating_message(cleared_ids)
        except Exception:
            pass

    def run_calibration(self):
        self.blur_main()

        # --- FORCE CONFIG CLEAN BEFORE OPENING SETTINGS ---
        self._enforce_license_limit_on_config()
        # -----------------------------------------------------

        self.calib_window = QtWidgets.QMainWindow()
        self.calib_window.setMinimumSize(1400, 800)

        self.calib_ui = Ui_SigmaControls_4()
        self.calib_ui.setupUi(self.calib_window)

        # --- DYNAMICALLY DISABLE RESTRICTED UI ELEMENTS ---
        for i in range(self.allowed_ids + 1, 9):
            target_text = f"Slave ID-{i}"

            for widget in self.calib_window.findChildren(QtWidgets.QWidget):
                if hasattr(widget, 'text') and target_text in str(widget.text()):
                    widget.setEnabled(False) 
                    
                    parent = widget.parentWidget()
                    if parent and type(parent) in [QtWidgets.QFrame, QtWidgets.QGroupBox]:
                        parent.setEnabled(False)

            for key, widget in vars(self.calib_ui).items():
                if key.endswith(f"_{i}") or key.endswith(str(i)):
                    try:
                        widget.setEnabled(False)
                    except:
                        pass
        # -----------------------------------------------------

        self.calib_window.destroyed.connect(self.check_calibration_closed)
        self.calib_window.installEventFilter(self)
        self.calib_window.show()

    def eventFilter(self, obj, event):
        # Catch both Close and Hide events to guarantee we unblur the main window
        if obj == getattr(self, "calib_window", None):
            if event.type() == QEvent.Close or event.type() == QEvent.Hide:
                self.check_calibration_closed()
                self.unblur_main()
                
                # Remove filter so it doesn't fire multiple times
                try:
                    obj.removeEventFilter(self)
                except:
                    pass
        return super().eventFilter(obj, event)

    def check_calibration_closed(self):
        # --- 1. FORCE CONFIG CLEAN TO ENFORCE LIMITS ---
        self._enforce_license_limit_on_config()
        # -----------------------------------------------

        # --- 2. RELOAD CONFIG AND UNBLUR ---
        self.load_config()
        self.update_all_y_axis_labels()
        
        # Absolute guarantee that the main window unblurs
        self.unblur_main() 


    def update_all_y_axis_labels(self):
        label = self.y_axis_text.strip() if hasattr(self, "y_axis_text") else ""
        style = (
            '<span style="color:#00A0E3; font-weight:bold; font-size:8pt;">{}</span>'
        )

        if hasattr(self, "plot_widget"):
            self.plot_widget.setLabel(
                "left",
                f'<span style="color:#00A0E3; font-weight:bold;">{label}</span>',
                justify="center",
            )

        if hasattr(self, "plot_widget10"):
            self.plot_widget10.setLabel(
                "left",
                f'<span style="color:#00A0E3; font-weight:bold;">{label}</span>',
                justify="center",
            )

    # ----------- End Communication -------------
    def close_communication(self):
        if hasattr(self, "worker"):
            self.worker.stop()
            self.worker.wait()

    # ----------- CSV File selected by user & store ------------
    def csv_file_open(self):
        self.blur_main()
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv)", options=options
        )
        self.unblur_main()
        if not file_path:
            self.ui.lineEdit.setText("No file selected")
            self.unblur_main()
            return

        file_name_with_ext = os.path.basename(file_path)  # e.g. 11-05-2025_ID_1.csv
        file_name = os.path.splitext(file_name_with_ext)[
            0
        ]  # e.g. 11-05-2025_ID_1  ← use splitext, not strip

        date_part = (
            file_name.split("_ID_")[0]
            if "_ID_" in file_name
            else file_name.split("_")[0]
        )
        date_folder = os.path.join(
            "Scanner_Files", date_part
        )  # Scanner_Files/11-05-2025
        report_folder = os.path.join(
            date_folder, file_name
        )  # Scanner_Files/11-05-2025/11-05-2025_ID_1
        os.makedirs(report_folder, exist_ok=True)

        dest_csv = os.path.join(report_folder, file_name_with_ext)
        # Always refresh the copy inside the per-ID folder. Copying only when
        # dest_csv didn't exist meant that once logging was stopped and later
        # resumed (source file grows / gets new rows appended), re-selecting
        # the same CSV would keep using the stale first-time snapshot forever
        # -- the graph/PDF steps always read from dest_csv, never the source
        # directly, so the graph plotted the old, smaller file even though a
        # newer one was picked.
        import shutil

        if os.path.abspath(file_path) != os.path.abspath(dest_csv):
            shutil.copy2(file_path, dest_csv)

        self.csv_filepath = dest_csv
        self.save_config()
        self.ui.lineEdit.setText(file_name_with_ext)
        self.unblur_main()

    # --------- Letterhead File selected by user and store ------------
    def letterhead_file_open(self):
        self.blur_main()
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Letterhead File",
            "",
            "Image Files (*.png *.jpg *.jpeg);",
            options=options,
        )
        # SVG removed from the filter: prepare_letterhead_image() rasterizes
        # everything through PIL, which cannot open SVGs at all, so an SVG
        # either crashed later or slipped past the size checks below into
        # the generic "Image Load Error" instead of a proper rejection.

        if file_path:
            try:
                # Letterhead hard limits: max size is exactly the letterhead box
                # (980x200). Larger images are rejected (not scaled down).
                # Smaller images are accepted and drawn at original
                # resolution, centered inside the 980x200 box.
                MIN_LETTERHEAD_W, MIN_LETTERHEAD_H = 150, 40
                MAX_LETTERHEAD_W = self.LETTERHEAD_BOX_W   # 980
                MAX_LETTERHEAD_H = self.LETTERHEAD_BOX_H   # 200
                # A letterhead must be banner-shaped, not a random square/
                # portrait photo -- cap how tall it's allowed to be relative
                # to its width.
                MIN_LETTERHEAD_ASPECT = 2.0   # width must be >= 2x height
                MAX_LETTERHEAD_ASPECT = 10.0  # and not absurdly thin either
                MAX_LETTERHEAD_FILE_MB = 5

                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                if file_size_mb > MAX_LETTERHEAD_FILE_MB:
                    QMessageBox.warning(
                        self,
                        "File Too Large",
                        f"This file is {file_size_mb:.1f} MB, too large for "
                        f"a letterhead. Maximum file size is "
                        f"{MAX_LETTERHEAD_FILE_MB} MB.",
                    )
                    self.ui.lineEdit_2.setText("No file selected")
                    self.letterhead_file = ""
                    self.save_config()
                    self.unblur_main()
                    return

                with Image.open(file_path) as img:
                    img.verify()

                # verify() invalidates the image object for further use,
                # so re-open to actually read its dimensions.
                with Image.open(file_path) as img:
                    width, height = img.size

                aspect = width / height if height else 0
                if aspect < MIN_LETTERHEAD_ASPECT or aspect > MAX_LETTERHEAD_ASPECT:
                    QMessageBox.warning(
                        self,
                        "Wrong Shape For A Letterhead",
                        f"This image is {width}x{height} px (aspect ratio "
                        f"{aspect:.2f}:1). A letterhead must be a wide "
                        f"banner shape, between {MIN_LETTERHEAD_ASPECT:.0f}:1 "
                        f"and {MAX_LETTERHEAD_ASPECT:.0f}:1. Please crop it "
                        f"to a banner and try again.",
                    )
                    self.ui.lineEdit_2.setText("No file selected")
                    self.letterhead_file = ""
                    self.save_config()
                    self.unblur_main()
                    return

                if width < MIN_LETTERHEAD_W or height < MIN_LETTERHEAD_H:
                    QMessageBox.warning(
                        self,
                        "Image Too Small",
                        f"This image is {width}x{height} px, too small for a "
                        f"letterhead. Minimum size is "
                        f"{MIN_LETTERHEAD_W}x{MIN_LETTERHEAD_H} px.",
                    )
                    self.ui.lineEdit_2.setText("No file selected")
                    self.letterhead_file = ""
                    self.save_config()
                    self.unblur_main()
                    return

                if width > MAX_LETTERHEAD_W or height > MAX_LETTERHEAD_H:
                    QMessageBox.warning(
                        self,
                        "Image Too Large",
                        f"This image is {width}x{height} px, too large for a "
                        f"letterhead. Maximum size is "
                        f"{MAX_LETTERHEAD_W}x{MAX_LETTERHEAD_H} px. Please "
                        f"crop/resize it to a banner-shaped image and try "
                        f"again.",
                    )
                    self.ui.lineEdit_2.setText("No file selected")
                    self.letterhead_file = ""
                    self.save_config()
                    self.unblur_main()
                    return

                file_name = os.path.basename(file_path)
                self.letterhead_file = file_path
                self.save_config()
                self.ui.lineEdit_2.setText(file_name)
                self.update_header_status_text()
                self.unblur_main()
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Image Load Error",
                    f"An error occurred while loading the image: {e}",
                )
                self.ui.lineEdit_2.setText("No file selected")
                self.letterhead_file = ""
                self.save_config()
                self.unblur_main()
        else:
            self.letterhead_file = ""
            self.save_config()
            self.ui.lineEdit_2.setText("No file selected")
            self.unblur_main()

    # Letterhead box: fixed 980 x 200 px. Upload rejects anything larger.
    # Smaller images keep their native pixels and are centered on a white
    # 980x200 canvas so the PDF always places a consistent banner slot.
    LETTERHEAD_BOX_W = 980
    LETTERHEAD_BOX_H = 200

    def prepare_letterhead_image(self, source_path):
        """Place the letterhead on a white LETTERHEAD_BOX_W x LETTERHEAD_BOX_H
        canvas at original resolution (no upscale, no downscale — oversized
        files are already rejected at upload). Centered horizontally and
        vertically. Returns (path, box_w, box_h) so PDF placement always
        uses the fixed box aspect ratio."""
        try:
            with Image.open(source_path) as img:
                if img.mode in ("RGBA", "LA") or (
                    img.mode == "P" and "transparency" in img.info
                ):
                    img = img.convert("RGBA")
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                else:
                    img = img.convert("RGB")

                src_w, src_h = img.size
                box_w = self.LETTERHEAD_BOX_W
                box_h = self.LETTERHEAD_BOX_H

                # Cover the box (fill width + height), then center-crop.
                # No side white bars — banner always edge-to-edge.
                scale = max(box_w / float(src_w), box_h / float(src_h))
                new_w = max(1, round(src_w * scale))
                new_h = max(1, round(src_h * scale))
                resized = img.resize((new_w, new_h), Image.LANCZOS)
                left = max(0, (new_w - box_w) // 2)
                top = max(0, (new_h - box_h) // 2)
                final = resized.crop((left, top, left + box_w, top + box_h))

                cache_dir = os.path.join(tempfile.gettempdir(), "sigma_intelliscan_cache")
                os.makedirs(cache_dir, exist_ok=True)
                out_path = os.path.join(cache_dir, "letterhead_fitted.png")
                final.save(out_path, "PNG")
                return out_path, box_w, box_h
        except Exception as e:
            write_event("ADMIN", "LETTERHEAD", f"Failed to fit letterhead image: {e}")
            try:
                with Image.open(source_path) as img:
                    return source_path, img.size[0], img.size[1]
            except Exception:
                return source_path, self.LETTERHEAD_BOX_W, self.LETTERHEAD_BOX_H

    def update_header_status_text(self):
        if getattr(self, "letterhead_file", "") == "":
            if getattr(self, "header", "") == "":
                self.ui.lineEdit_3.setText("No Header, No Letterhead")
            else:
                self.ui.lineEdit_3.setText("Header Present, No Letterhead")
        else:
            if getattr(self, "header", "") == "":
                self.ui.lineEdit_3.setText("No Header, Letterhead Present")
            else:
                self.ui.lineEdit_3.setText("Header Present, Letterhead Present")

    # --------- Set btn for (time & date of selected file) ------------
    def set_button(self):
        write_event("ADMIN", "SETTINGS", "Configuration updated")
        file_path = self.csv_filepath
        header = self.header

        company_name = self.ui.lineEdit_4.text().strip()

        if len(company_name) > 30:
            self.show_message(
                "Error", "Company Name cannot exceed 30 characters.", "#ff4c4c"
            )
            return

        # Require a CSV file BEFORE touching/locking the Company Name --
        # previously the company name got committed and the field locked
        # read-only even when this step was about to fail, leaving no way
        # to re-enter a corrected name afterwards.
        if not file_path:
            self.show_message(
                "Error",
                "Please select a CSV file first (Set File) before clicking Set.",
                "#ff4c4c",
            )
            return

        is_first_time_setup = not getattr(self, "company_name", "").strip()
        if is_first_time_setup and not company_name:
            self.show_message("Error", "Please enter Company Name", "#ff4c4c")
            return

        if is_first_time_setup:
            reply = QMessageBox.question(
                self,
                "Confirm Company Name",
                f"Company Name:\n\n{company_name}\n\nThis cannot be changed later.",
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply != QMessageBox.Yes:
                return

        self.load_config()

        try:
            df = pd.read_csv(file_path)
            if df.empty:
                self.ui.lineEdit.setText("Empty")
                return

            first_row = df.iloc[0]
            last_row = df.iloc[-1]

            start_date_str = first_row.iloc[0]
            end_date_str = last_row.iloc[0]

            original_start_date = df.iloc[0, 0]
            original_end_date = df.iloc[-1, 0]
            original_start_time = df.iloc[0, 1]
            original_end_time = df.iloc[-1, 1]

            start_date = QDate.fromString(original_start_date, "dd-MM-yyyy")
            end_date = QDate.fromString(original_end_date, "dd-MM-yyyy")
            start_time = QTime.fromString(original_start_time, "HH:mm:ss")
            end_time = QTime.fromString(original_end_time, "HH:mm:ss")

            self.ui.dateEdit_2.setDate(start_date)
            self.ui.dateEdit_3.setDate(end_date)
            self.ui.timeEdit_2.setTime(start_time)
            self.ui.timeEdit_4.setTime(end_time)

            # Only commit + lock the Company Name once everything above
            # has actually succeeded.
            self.company_name = company_name
            if is_first_time_setup:
                self.ui.lineEdit_4.setReadOnly(True)

            self.show_message("Set", "Values Updated!", "#FBFF26")

            new_header = self.ui.textEdit.toPlainText()
            header_lines = new_header.split("\n")
            if len(header_lines) > 3:
                # Previously this showed the error but still went ahead
                # and saved/used the over-limit text anyway (it printed
                # fine in the graph PDFs despite the warning). Now it's
                # actually rejected: keep whatever the last valid header
                # was, and restore the text box to match so it's obvious
                # nothing over the limit got kept.
                self.show_message(
                    "Header Alert",
                    "Header cannot exceed 3 lines! Not saved -- please "
                    "shorten it to 3 lines or fewer.",
                    "#ff4c4c",
                )
                self.ui.textEdit.setText(getattr(self, "header", ""))
            else:
                self.header = new_header
                self.ui.textEdit.setText(self.header)
            self.save_config()
            self.update_header_status_text()

        except Exception as e:
            # Show the real reason instead of a generic message, and don't
            # leave the Company Name field locked if nothing was actually
            # saved.
            self.show_message("Set", f"Values Not Updated!\n{e}", "#ff4c4c")

        if self.worker is None:
            self.start_csv_replay()

    def stop_csv_replay(self):
        """Stop replay fully so Start / live logging can take over cleanly."""
        try:
            if getattr(self, "replay_timer", None) is not None:
                self.replay_timer.stop()
        except Exception:
            pass
        was_replaying = bool(getattr(self, "replay_mode", False))
        self.replay_mode = False
        self.replay_paused = False
        self.replay_rows = []
        self.replay_index = 0
        self.replay_x = []
        self.replay_y = [[] for _ in range(24)]
        self._live_curves = {}
        for _lg in (
            getattr(self, "live_legend1", None),
            getattr(self, "live_legend2", None),
        ):
            if _lg is not None:
                try:
                    _lg.clear()
                except Exception:
                    pass
        if was_replaying:
            try:
                self.plot_widget.clear()
            except Exception:
                pass
            self._attach_live_legends()
            try:
                if hasattr(self, "csv_table_widget"):
                    self.csv_table_widget.setRowCount(0)
            except Exception:
                pass

    def start_csv_replay(self):
        if hasattr(self, "worker") and self.worker is not None:
            self.show_message(
                "Replay", "Stop live communication before replay.", "#ff4c4c"
            )
            return

        csv_path = self.csv_filepath
        if not csv_path:
            return

        if not os.path.exists(csv_path):
            return

        try:
            df = pd.read_csv(csv_path, header=None)
        except Exception as e:
            return

        self.replay_rows = df.values.tolist()
        if len(self.replay_rows) == 0:
            return

        self.replay_index = 0
        self.replay_y = [[] for _ in range(24)]
        self.replay_x = []
        self.csv_table_widget.setRowCount(0)
        self.plot_widget.clear()
        # Replay reuses the same plot_widget as the live graph -- drop our
        # curve/legend bookkeeping so update_replay_display() (which plots
        # fresh each row anyway) and any later update_graph() call both
        # start from a clean slate instead of touching now-stale items.
        self._live_curves = {}
        for _lg in (getattr(self, "live_legend1", None), getattr(self, "live_legend2", None)):
            if _lg is not None:
                _lg.clear()

        self.plot_widget.getAxis("left").setPen("k")
        self.plot_widget.getAxis("left").setTextPen("k")
        self.plot_widget.getAxis("bottom").setPen("k")
        self.plot_widget.getAxis("bottom").setTextPen("k")
        
        self.replay_mode = True
        self.replay_paused = False

        interval = max(1, int(1000 / max(1, self.replay_speed)))
        self.replay_timer.start(interval)

    def toggle_replay_pause(self):
        """Space / Ctrl+P: pause or resume an in-progress CSV replay.
        No-op if no replay is currently running."""
        if not getattr(self, "replay_mode", False):
            return
        if self.replay_paused:
            interval = max(1, int(1000 / max(1, self.replay_speed)))
            self.replay_timer.start(interval)
            self.replay_paused = False
            self.show_message("Replay", "Resumed", "#02c702")
        else:
            self.replay_timer.stop()
            self.replay_paused = True
            self.show_message("Replay", "Paused", "#ffb300")

    def replay_next_row(self):
        if self.replay_index >= len(self.replay_rows):
            self.replay_timer.stop()
            self.replay_mode = False
            self.replay_paused = False
            self.show_message("Replay", "Replay completed", "#02c702")
            return

        row = self.replay_rows[self.replay_index]
        self.replay_index += 1
        self.update_replay_display(row)

    def update_replay_display(self, row):
        try:
            # --- 1. Skip the Header Row ---
            date = str(row[0]).strip()
            time = str(row[1]).strip()
            if date.upper() == "DATE":
                return

            # --- 2. Update the Table ---
            row_idx = self.csv_table_widget.rowCount()
            self.csv_table_widget.insertRow(row_idx)
            for col_idx, value in enumerate(row):
                # Clean up 'nan' visuals in the table
                disp_val = "" if str(value).lower() in ["nan", "none", "null"] else str(value)
                item = QTableWidgetItem(disp_val)
                self.csv_table_widget.setItem(row_idx, col_idx, item)

            self.csv_table_widget.scrollToBottom()

            # --- 3. Extract X-Axis Time ---
            x_idx = len(self.replay_x)
            self.replay_x.append((x_idx, f"{time}\n{date}"))
            
            # --- 4. Process Y-Axis values safely ---
            for ch in range(24):
                try:
                    val_str = str(row[ch + 2]).strip()
                    # Handle empty strings or NaNs from pandas
                    if not val_str or val_str.lower() in ['nan', 'none', 'null', '']:
                        value = np.nan
                    else:
                        value = float(val_str)
                        # Filter out fault codes (like 15000) so they don't squish the graph
                        if value < -200 or value > 2000:
                            value = np.nan
                except Exception:
                    value = np.nan
                    
                self.replay_y[ch].append(value)
                
            # --- 5. Format the Graph ---
            self.plot_widget.clear()
            # Replay rebuilds every row anyway (unlike the live graph, this
            # isn't trying to avoid a full clear), but it now needs to
            # clear OUR two-column legends specifically, since the old
            # addLegend()-based legend was replaced with live_legend1/2.
            for _lg in (getattr(self, "live_legend1", None), getattr(self, "live_legend2", None)):
                if _lg is not None:
                    _lg.clear()
            axis = self.plot_widget.getAxis("bottom")

            # Tick step based on the plot's ACTUAL current pixel width,
            # not a fixed "every 15th point" ratio -- the old approach
            # showed every single point's label whenever fewer than ~15
            # rows had accumulated yet (exactly the overlapping mess seen
            # early in a replay), and never adapted to the widget being
            # resized. Recomputed on every row so it also adjusts live if
            # the window is resized mid-replay.
            widget_width_px = max(1, self.plot_widget.width())
            # Balance between "labels collide" (too dense) and "barely any
            # ticks" (too sparse): budget for the left-axis margin, use a
            # smaller font, and pack ticks in at ~75px each instead of the
            # original 85px (no margin) or the earlier overcorrection to
            # 110px (way too sparse).
            replay_tick_font = QFont()
            replay_tick_font.setPixelSize(10)
            axis.setTickFont(replay_tick_font)
            usable_width_px = max(1, widget_width_px - 50)  # left-axis/margin allowance
            max_ticks_that_fit = max(3, usable_width_px // 75)
            step = max(1, -(-len(self.replay_x) // max_ticks_that_fit))  # ceil div
            ticks = self.replay_x[::step]
            axis.setTicks([ticks])
            
            self.plot_widget.showGrid(x=True, y=True, alpha=0.8)
            axis.setPen("k")
            axis.setTextPen("k")
            self.plot_widget.getAxis("left").setPen("k")
            self.plot_widget.getAxis("left").setTextPen("k")

            colors = [
                "#FF0000","#3CB44B","#FFE100","#0000FF","#F58231","#911EB4",
                "#46F0F0","#FF1493","#000075","#800000","#AA6E28","#E6BEFF",
                "#2F6324","#FFB6C1","#7B68EE","#008080","#808000","#00FA9A",
                "#1E90FF","#808080","#BCF60C","#FFFF00","#FFA500","#FF00FF"
            ]

            # --- 6. Plot the Lines ---
            for ch in range(24):
                checkbox = getattr(self.ui, f"CH{ch+1:02d}Check")
                if not checkbox.isChecked():
                    continue
                    
                # Convert list to numpy array for safe handling
                y_data = np.array(self.replay_y[ch], dtype=np.float64)
                
                # If everything is NaN (empty column), don't attempt to plot
                if np.all(np.isnan(y_data)):
                    continue
                    
                # X data must match Y data length perfectly
                x_data = np.arange(len(y_data))
                pen = pg.mkPen(colors[ch], width=2)

                # connect="finite" prevents PyQtGraph from connecting lines
                # across missing data (NaN) gaps. name= + explicit
                # addItem() registers this curve with the correct
                # 12-channel-split legend (legend1 for CH1-12, legend2 for
                # CH13-24) since the plot was fully cleared above.
                _replay_curve = self.plot_widget.plot(
                    x_data,
                    y_data,
                    pen=pen,
                    connect="finite",
                    name=f"CH{ch + 1}",
                )
                target_legend = self.live_legend1 if ch < 12 else self.live_legend2
                if target_legend is not None:
                    try:
                        target_legend.addItem(_replay_curve, f"CH{ch + 1}")
                    except Exception:
                        pass

            # Hide empty legend box; keep legends attached after clear()
            self._attach_live_legends()

            # --- 7. Final Polish ---
            self.plot_widget.setXRange(0, max(1, len(self.replay_x)-1))
            self.plot_widget.setTitle(f"Graph (Replay ID-{getattr(self, 'selected_slave', 1)})", color="#00A0E3")
            
            y_text = getattr(self, "y_axis_text", "")
            self.plot_widget.setLabel("left", f'<span style="color:#00A0E3; font-weight:bold;">{y_text}</span>', justify="center")

        except Exception as e:
            pass

    # --------- Submit btn for (filterd graph) ------------
    def _prompt_graph_channels(self, available_channels):
        """Ask which channels to include in the Featured Graph built from a
        historical CSV. Completely separate from the live CH01Check..CH24Check
        checkboxes used for logging/live display, so it can never disturb an
        active logging session even if it currently uses a different channel
        count.

        available_channels: list like ["CH1", "CH3", "CH7"] — channels that
        actually have data in the loaded/filtered CSV.

        Returns a dict {channel_name: bool}. Selection is remembered in
        self._graph_channel_selection across calls (per-channel), defaulting
        to True (shown) the first time a channel is seen. If the dialog is
        cancelled or closed (X button), returns None -- the caller should
        abort and not open the graph/table at all.
        """
        if not available_channels:
            return {}

        dlg = QDialog(self)
        dlg.setWindowTitle("Select Channels for Graph")
        dlg.setWindowIcon(QIcon(get_app_icon_svg()))
        dlg.setMinimumWidth(360)
        # Cap the dialog height so it never overflows the screen even with
        # 24 channels -- the scroll area inside takes over instead of the
        # whole dialog growing off-page.
        screen = QApplication.primaryScreen()
        max_h = int(screen.availableGeometry().height() * 0.85) if screen else 700
        dlg.setMaximumHeight(max_h)
        dlg.setStyleSheet("""
            QDialog      { background:#1a1a2e; }
            QLabel       { background:transparent; }
            QLabel#hdr   { color:#90CAF9; font:bold 11pt 'Segoe UI';
                           padding:6px 4px 8px 4px; background:transparent; }
            QScrollArea  { border:none; background:transparent; }
            QScrollArea > QWidget > QWidget { background:transparent; }
            QWidget#scroll_inner { background:transparent; }
            QCheckBox    { color:#EEEEEE; font:9pt 'Segoe UI';
                           padding:4px 8px; border-radius:4px;
                           background:transparent; }
            QCheckBox:hover { background:#2a2a4a; }
            QPushButton  { background:#1565C0; color:white; border:none;
                           border-radius:6px; padding:7px 22px;
                           font:bold 9pt 'Segoe UI'; }
            QPushButton:hover        { background:#1976D2; }
            QPushButton#secondary    { background:#37474F; min-width:110px; }
            QPushButton#secondary:hover { background:#546E7A; }
        """)

        root = QVBoxLayout(dlg)
        root.setContentsMargins(14, 14, 14, 14)

        hdr = QLabel("Channel Selection")
        hdr.setObjectName("hdr")
        hdr.setAlignment(Qt.AlignHCenter)
        root.addWidget(hdr)

        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background:transparent; border:none;")
        scroll.viewport().setStyleSheet("background:transparent;")
        # Keep a very tall channel list (e.g. 24 channels) scrollable
        # instead of pushing the buttons off the bottom of the screen.
        scroll.setMaximumHeight(max(180, max_h - 160))
        inner = QWidget(); inner.setObjectName("scroll_inner")
        inner.setStyleSheet("background:transparent;")
        vbox = QVBoxLayout(inner)
        vbox.setContentsMargins(4, 4, 4, 4)
        scroll.setWidget(inner)
        root.addWidget(scroll)

        checkboxes = {}
        for ch in available_channels:
            default_checked = self._graph_channel_selection.get(ch, True)
            cb = QCheckBox(_format_channel_label(ch))
            cb.setChecked(default_checked)
            cb.setAutoFillBackground(False)
            checkboxes[ch] = cb
            vbox.addWidget(cb)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        all_btn = QPushButton("Select All"); all_btn.setObjectName("secondary")
        none_btn = QPushButton("Select None"); none_btn.setObjectName("secondary")
        all_btn.clicked.connect(lambda: [cb.setChecked(True) for cb in checkboxes.values()])
        none_btn.clicked.connect(lambda: [cb.setChecked(False) for cb in checkboxes.values()])
        btn_row.addWidget(all_btn)
        btn_row.addWidget(none_btn)
        btn_row.addStretch()
        root.addLayout(btn_row)

        ok_row = QHBoxLayout()
        ok_btn = QPushButton("Show Graph and Table")
        ok_btn.clicked.connect(dlg.accept)
        ok_row.addStretch()
        ok_row.addWidget(ok_btn)
        ok_row.addStretch()
        root.addLayout(ok_row)

        if dlg.exec_() != QDialog.Accepted:
            # Cancelled or closed via the X button: abort entirely, nothing
            # should open.
            return None

        selection = {ch: cb.isChecked() for ch, cb in checkboxes.items()}
        self._graph_channel_selection.update(selection)
        return selection

    def _open_channel_data_table(self, df1, df2, active_channels, file_path):
        """Open the paginated data-table window for the same date/time range
        and the same channel selection just used for the Featured Graph.
        Non-modal, and a reference is kept so it isn't garbage-collected
        while open -- multiple table windows (e.g. from different CSVs)
        can stay open side by side."""
        if not active_channels:
            return
        try:
            date_col = df1[0].astype(str).tolist()
            time_col = df1[1].dt.strftime("%H:%M:%S").tolist()

            channel_data = {}
            for i, col in enumerate(df2.columns):
                ch_name = f"CH{i + 1}"
                if ch_name in active_channels:
                    channel_data[ch_name] = df2[col].reset_index(drop=True).tolist()

            window = ChannelDataTableWindow(
                self,
                date_col,
                time_col,
                channel_data,
                list(active_channels),
                os.path.basename(file_path),
                getattr(self, "company_name", ""),
            )
            if not hasattr(self, "_open_data_table_windows"):
                self._open_data_table_windows = []
            self._open_data_table_windows.append(window)
            window.setWindowModality(Qt.NonModal)
            window.showMaximized()
        except Exception as e:
            pass

    def submit_button(self):
        self.start_date = self.ui.dateEdit_2.date().toString("dd-MM-yyyy")
        dummy_start_date = self.ui.dateEdit_2.date().toString("dd-MM-yyyyyyyy")
        self.end_date = self.ui.dateEdit_3.date().toString("dd-MM-yyyy")
        dummy_end_date = self.ui.dateEdit_3.date().toString("dd-MM-yyyyyyyy")
        self.start_time = self.ui.timeEdit_2.time().toString("hh:mm:ss")
        self.end_time = self.ui.timeEdit_4.time().toString("hh:mm:ss")
        self.save_config()

        self.load_config()

        # self.plot_widget.setLabel(
        #     "left",
        #     f'<span style="color:#00A0E3; font-weight:bold;">{graph_y_axis}</span>',
        #     justify="center",
        # )

        # self.plot_widget10.setLabel(
        #     "left",
        #     f'<span style="color:#00A0E3; font-weight:bold;">{graph_y_axis}</span>',
        #     justify="center",
        # )

        file_path = self.csv_filepath
        file_name = os.path.basename(file_path).strip(".csv")
        if file_path:
            directory_path = file_path.replace(f"{file_name}.csv", "")
            graph_file_path = os.path.join(directory_path, f"{file_name}_graph.png")
            pdf_file_path = os.path.join(directory_path, f"{file_name}_graph.pdf")
            filtered_csv_file_path = os.path.join(
                directory_path, f"{file_name}_filtered.csv"
            )

        file_path = self.csv_filepath
        
        graph_y_axis = "Temperature"
        try:
            file_name = os.path.basename(file_path)
            match = re.search(r'ID[_-]?(\d+)', file_name, re.IGNORECASE)
            if match:
                slave_id = int(match.group(1))
                if 1 <= slave_id <= 8:
                    # Read directly from config instead of GUI variables
                    with open(CONFIG_FILE, "r") as f:
                        cfg = json.load(f)
                    with open(CONFIG_FILE, "r") as f:
                        cfg = json.load(f)
                    text = cfg.get(f"y_axis_text_{slave_id}", "").strip()
                    if text:
                        graph_y_axis = text
        except Exception:
            pass
        # Save for the whole submit_button()
        self.graph_y_axis = graph_y_axis
        
        self.plot_widget.setLabel(
            "left",
            f'<span style="color:#00A0E3; font-weight:bold;">{graph_y_axis}</span>',
            justify="center",
        )

        self.plot_widget10.setLabel(
            "left",
            f'<span style="color:#00A0E3; font-weight:bold;">{graph_y_axis}</span>',
            justify="center",
        )
        
        header = self.header
        self.ui.textEdit.setText(header)

        df = pd.read_csv(file_path, header=None)
        df_str = pd.read_csv(file_path, header=None, dtype=str)  # raw strings preserved
        df_str = df_str.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        time_str1 = self.start_time
        time_str2 = self.end_time
        date_str1 = self.start_date
        date_str2 = self.end_date

        start_dt_filter = pd.to_datetime(date_str1 + " " + time_str1, format="%d-%m-%Y %H:%M:%S")
        end_dt_filter = pd.to_datetime(date_str2 + " " + time_str2, format="%d-%m-%Y %H:%M:%S")
        row_dt = pd.to_datetime(df[0] + " " + df[1], format="%d-%m-%Y %H:%M:%S", errors="coerce")

        df1 = []
        for i in range(len(df)):
            if pd.notna(row_dt.iloc[i]) and start_dt_filter <= row_dt.iloc[i] <= end_dt_filter:
                df1.append(df.iloc[i, :])

        if df1:
            df1 = pd.DataFrame(df1)
            df2 = pd.DataFrame(df1.iloc[:, 2 : df1.shape[1]])
            df1[1] = pd.to_datetime(df1[0] + " " + df1[1], format="%d-%m-%Y %H:%M:%S")
            df3 = pd.DataFrame(df1.iloc[:, 1].apply(self.time_str_to_float))

            filtered_file_path = file_path.replace(".csv", "_filtered.csv")
            filtered_df = pd.concat([df1[0], df1[1], df2], axis=1)
            filtered_df.to_csv(filtered_file_path, index=False, header=None)

            plt.figure(figsize=(19, 9.5), tight_layout=True)
            plt.gcf().canvas.manager.set_window_title(f"Sigma Controls | Graph - {file_path.split('/')[-1]}")

            lines = []
            bright_colors = [
                "red",
                "green",
                "blue",
                "orange",
                "purple",
                "pink",
                "cyan",
                "magenta",
                "yellow",
                "lime",
            ]
            active_channels = []

            # Channels that actually have data in this CSV/date range.
            available_channels = [
                f"CH{i + 1}" for i, col in enumerate(df2.columns) if df2[col].any() != 0
            ]
            # Ask which of those to include -- independent of the live
            # logging CH checkboxes, so an active logging session with 8
            # channels is never touched by generating a graph for fewer
            # (or more) channels from an old CSV.
            graph_selection = self._prompt_graph_channels(available_channels)
            if graph_selection is None:
                # Dialog was cancelled / closed via X -- open nothing.
                return

            for i, col in enumerate(df2.columns):
                ch_name = f"CH{i + 1}"
                channel_enabled = graph_selection.get(ch_name, True)

                if channel_enabled and df2[col].any() != 0:
                    color = bright_colors[i % len(bright_colors)]
                    (line,) = plt.plot(
                        df1[1], df2[col], label=_format_channel_label(ch_name), color=color
                    )
                    lines.append(line)
                    active_channels.append(ch_name)

            from matplotlib.dates import AutoDateFormatter
            import matplotlib.dates as _mdates_grid

            # AutoDateLocator's minticks/maxticks are only a soft hint --
            # it snaps to a fixed set of "nice" intervals (1,5,10,15,30min,
            # etc) and will happily land below minticks if the next nicer
            # interval undershoots it. That's why ticks stayed sparse even
            # after raising the min/max range. Pick the interval explicitly
            # instead, sized to actually hit a target tick count for the
            # real filtered span.
            _NICE_MINUTE_STEPS = [1, 2, 3, 5, 10, 15, 20, 30, 45, 60, 90, 120,
                                   180, 240, 360, 480, 720, 1440]

            def _nice_dt_locator(span_minutes, target_ticks):
                span_minutes = max(1, span_minutes)
                target_ticks = max(2, target_ticks)
                ideal = span_minutes / target_ticks
                step = next((n for n in _NICE_MINUTE_STEPS if n >= ideal), _NICE_MINUTE_STEPS[-1])
                if step < 60:
                    return _mdates_grid.MinuteLocator(interval=step)
                elif step < 1440:
                    return _mdates_grid.HourLocator(interval=max(1, step // 60))
                else:
                    return _mdates_grid.DayLocator(interval=max(1, step // 1440))

            _span_minutes = max(1, (end_dt_filter - start_dt_filter).total_seconds() / 60)

            locator = _nice_dt_locator(_span_minutes, target_ticks=8)
            ax = plt.gca()
            ax.set_facecolor((0.9, 0.98, 0.9))
            ax.xaxis.set_major_locator(locator)
            formatter = AutoDateFormatter(locator)
            formatter.scaled[1 / (24 * 60 * 60)] = "%H:%M:%S\n%d-%m-%Y"
            formatter.scaled[1 / (24 * 60)] = "%H:%M:%S\n%d-%m-%Y"
            formatter.scaled[1 / 24] = "%H:%M\n%d-%m-%Y"
            formatter.scaled[1] = "%d-%m-%Y"
            formatter.scaled[30] = "%m-%Y"
            formatter.scaled[365] = "%Y"
            ax.xaxis.set_major_formatter(formatter)

            # Keep x-axis tick count matched to the actual window width as
            # the graph window is resized -- recomputes the target tick
            # count from the current figure width, then re-derives a nice
            # interval for that count, whenever the window is resized.
            def _adjust_xtick_density(event=None):
                try:
                    fig_width_px = ax.figure.get_size_inches()[0] * ax.figure.dpi
                    # ~120px per 2-line date/time label so labels don't overlap
                    target = max(3, min(10, int(fig_width_px // 120)))
                    new_locator = _nice_dt_locator(_span_minutes, target_ticks=target)
                    ax.xaxis.set_major_locator(new_locator)
                    ax.figure.canvas.draw_idle()
                except Exception:
                    pass

            plt.gcf().canvas.mpl_connect("resize_event", _adjust_xtick_density)
            _adjust_xtick_density()

            plt.xlabel("Date & Time", fontsize=16, color="#00A0E3", labelpad=6)
            plt.ylabel(
                str(self.graph_y_axis),
                fontsize=16,
                color="#00A0E3",
                labelpad=10,
            )
            plt.rcParams["axes.titlesize"] = 20
            plt.rcParams["axes.titlepad"] = 12
            plt.title("Featured Graph", fontsize=20, color="#00A0E3", pad=12)

            from matplotlib.ticker import AutoMinorLocator as _AutoMinorLocatorX

            # Explicit per-axis grid control (avoids matplotlib's implicit
            # visible-toggle quirk when mixing ax.grid()/ax.yaxis.grid() calls).
            ax.xaxis.grid(True, which="major", color=(0.4, 0.4, 0.4, 0.6), linestyle="-", linewidth=0.8)
            ax.xaxis.set_minor_locator(_AutoMinorLocatorX(4))  # denser minor gridlines (was 2)
            ax.xaxis.grid(True, which="minor", color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6)
            ax.yaxis.grid(True, which="major", color=(0.4, 0.4, 0.4, 0.6), linestyle="-", linewidth=0.8)

            # ── Single source of truth for the actual plotted span ──
            start_dt = pd.to_datetime(
                self.start_date + " " + self.start_time, format="%d-%m-%Y %H:%M:%S"
            )
            end_dt = pd.to_datetime(
                self.end_date + " " + self.end_time, format="%d-%m-%Y %H:%M:%S"
            )
            total_minutes = max(1, int((end_dt - start_dt).total_seconds() / 60))
            # ── Start / Stop markers on X-axis ──

            ax.axvline(
                x=start_dt,
                color="green",
                linewidth=1.5,
                linestyle="--",
                zorder=5,
                label="Start",
                alpha=0.7,
            )
            ax.axvline(
                x=end_dt,
                color="red",
                linewidth=1.5,
                linestyle="--",
                zorder=5,
                label="Stop",
                alpha=0.7,
            )

            ax.text(
                start_dt,
                ax.get_ylim()[0],
                f"START\n{self.start_time}\n{self.start_date}",
                color="green",
                fontsize=10,
                va="top",
                ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=1),
            )

            ax.text(
                end_dt,
                ax.get_ylim()[0],
                f"STOP\n{self.end_time}\n{self.end_date}",
                color="red",
                fontsize=10,
                va="top",
                ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=1),
            )

            from matplotlib.ticker import AutoMinorLocator

            ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=14, min_n_ticks=10))
            ax.yaxis.set_minor_locator(AutoMinorLocator(4))  # denser minor gridlines (was 2)
            ax.yaxis.grid(
                True, which="minor", color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6
            )
            ax.tick_params(which="major", width=1, length=7)
            ax.tick_params(which="minor", width=0.8, length=4)

            (crosshair,) = plt.plot([], [], "r--", visible=False)
            coords_text = plt.text(
                0.95,
                0.95,
                "",
                transform=plt.gca().transAxes,
                ha="right",
                va="top",
                fontsize=12,
                color="black",
            )

            # ----- X,Y Data Tips -------
            def on_hover(event):
                if event.inaxes == plt.gca():
                    x, y = event.xdata, event.ydata
                    if x is not None:
                        x_timestamp = pd.Timestamp(x, unit="s")
                        index = (df1[1] - x_timestamp).abs().idxmin()
                        nearest_timestamp = df1.iloc[index, 1].strftime("%H:%M:%S")
                        crosshair.set_data(
                            [df1.iloc[index, 1], df1.iloc[index, 1]],
                            [plt.gca().get_ylim()[0], plt.gca().get_ylim()[1]],
                        )
                        coords_text.set_text(
                            f"Time: {nearest_timestamp}, {self.graph_y_axis}: {y:.2f}"
                        )
                        # crosshair.set_visible(True)
                        coords_text.set_visible(True)
                    else:
                        crosshair.set_visible(False)
                        coords_text.set_visible(False)
                else:
                    crosshair.set_visible(False)
                    coords_text.set_visible(False)

                plt.gcf().canvas.draw()

            plt.gcf().canvas.mpl_connect("motion_notify_event", on_hover)

            # ── Permanent Markers (max 5) ──
            # Left-click  = place marker
            # Right-click = delete nearest marker
            # Drag        = move annotation box anywhere on graph
            import matplotlib.dates as mdates
            from PyQt5.QtWidgets import (
                QDialog, QVBoxLayout, QHBoxLayout,
                QCheckBox, QPushButton, QLabel, QFrame, QScrollArea, QWidget
            )

            MAX_MARKERS   = 5
            placed_markers = []
            _show_msg  = self.show_message
            _icon_path = get_app_icon_svg()
            _y_label   = self.graph_y_axis
            # 5 distinct colors — one per marker slot
            MARKER_COLORS = ["#1565C0", "#7B1FA2", "#00695C", "#E65100", "#B71C1C"]
            MARKER_BG     = ["#E3F2FD", "#F3E5F5", "#E0F2F1", "#FFF3E0", "#FFEBEE"]
            _drag = {"active": False, "entry": None, "ox": 0, "oy": 0}

            # ── helpers ──────────────────────────────────────────────────────

            def _row_pos_from_idx(label_idx):
                """Convert df1 label-index to integer position in df2."""
                try:
                    return df2.index.get_loc(label_idx)
                except Exception:
                    return 0

            def _ch_values_at(nearest_idx):
                result = {}
                try:
                    dt = df1.loc[nearest_idx, 1]
                    date_part = dt.strftime("%d-%m-%Y")
                    time_part = dt.strftime("%H:%M:%S")
                    match = df_str[(df_str[0] == date_part) & (df_str[1] == time_part)]
                    if not match.empty:
                        row = match.iloc[0]
                        for col_i, col in enumerate(df2.columns):
                            lbl = f"CH{col_i + 1}"
                            if lbl in active_channels:
                                csv_col = col_i + 2
                                val = str(row.iloc[csv_col]).strip()
                                if val and val.lower() != "nan":
                                    try:
                                        result[lbl] = f"{float(val):.2f}"
                                    except Exception:
                                        result[lbl] = val
                except Exception:
                    pass
                return result

            def _overlapping_groups(ch_vals):
                keys = list(ch_vals.keys())
                visited = set()
                groups = []

                for i in range(len(keys)):
                    if keys[i] in visited:
                        continue

                    grp = [keys[i]]
                    visited.add(keys[i])

                    try:
                        vi = float(ch_vals[keys[i]])
                    except Exception:
                        continue

                    for j in range(i + 1, len(keys)):
                        if keys[j] in visited:
                            continue

                        try:
                            vj = float(ch_vals[keys[j]])
                        except Exception:
                            continue

                        if abs(vi - vj) < 0.001:
                            grp.append(keys[j])
                            visited.add(keys[j])

                    groups.append(grp)

                return [g for g in groups if len(g) > 1]

            def _make_label(num, sel_vals, time_s, date_s):
                lines_t = []

                # Bold title
                lines_t.append(rf"$\bf{{M{num}\ \ \ {date_s}\ \ \ {time_s}}}$")

                # Separator
                lines_t.append("─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ")

                # Bold channel names only
                for ch, v in sel_vals.items():
                    lines_t.append(
                        rf"$\bf{{{ch}}}$: {v} {_y_label}"
                    )

                return "\n".join(lines_t)

            def _place_marker(nearest_dt, label_idx, sel_vals):
                num   = len(placed_markers) + 1
                color = MARKER_COLORS[(num - 1) % len(MARKER_COLORS)]
                bg    = MARKER_BG[(num - 1) % len(MARKER_BG)]
                time_s = nearest_dt.strftime("%H:%M:%S")
                date_s = nearest_dt.strftime("%d-%m-%Y")
                text   = _make_label(num, sel_vals, time_s, date_s)

                vline = ax.axvline(
                    x=nearest_dt, color=color, linewidth=1.8,
                    linestyle=(0, (6, 3)), alpha=0.9, zorder=6
                )

                # Number label on the vline at top
                y_lo, y_hi = ax.get_ylim()
                num_txt = ax.text(
                    nearest_dt, y_hi - (y_hi - y_lo) * 0.03,
                    f" M{num} ", fontsize=8, color="white",
                    fontweight="bold", va="top", ha="center",
                    bbox=dict(boxstyle="round,pad=0.2", fc=color, ec="none", alpha=0.95),
                    zorder=10,
                )

                # Annotation box — use offset points so no Timestamp in xyann
                ann_x_disp, ann_y_disp = ax.transData.transform(
                    (mdates.date2num(nearest_dt), y_lo + (y_hi - y_lo) * 0.72)
                )
                ann = ax.annotate(
                    text,
                    xy=(nearest_dt, y_lo + (y_hi - y_lo) * 0.72),
                    xytext=(ann_x_disp + 8, ann_y_disp),
                    textcoords="figure pixels",
                    fontsize=8.5,
                    color="#111111",
                    fontfamily="monospace",
                    bbox=dict(
                        boxstyle="round,pad=0.55",
                        fc=bg, ec=color,
                        linewidth=2.0, alpha=0.95,
                    ),
                    zorder=9,
                    annotation_clip=False,
                    arrowprops=dict(
                        arrowstyle="-",
                        color=color, lw=1.2, alpha=0.6,
                    ),
                )

                entry = {
                    "vline": vline, "annotation": ann, "num_txt": num_txt,
                    "color": color, "dt": nearest_dt, "idx": label_idx, "num": num,
                }
                placed_markers.append(entry)
                plt.gcf().canvas.draw_idle()

            def _remove_marker(entry):
                for k in ("vline", "annotation", "num_txt"):
                    try:
                        entry[k].remove()
                    except Exception:
                        pass
                if entry in placed_markers:
                    placed_markers.remove(entry)
                plt.gcf().canvas.draw_idle()

            def _ask_channels(ch_vals, time_s, date_s, overlap_groups):
                """Dialog shown only when channels truly overlap. Shows all channels,
                highlights the overlapping ones so user knows why they're being asked."""
                dlg = QDialog()
                dlg.setWindowTitle("Select Channels for Marker")
                dlg.setWindowIcon(QIcon(_icon_path))
                dlg.setMinimumWidth(480)
                dlg.setStyleSheet("""
                    QDialog      { background:#1a1a2e; }
                    QLabel#hdr   { color:#90CAF9; font:bold 11pt 'Segoe UI';
                                   padding:6px 4px 2px 4px; }
                    QLabel#sub   { color:#9E9E9E; font:9pt 'Segoe UI';
                                   padding:0 4px 4px 4px; }
                    QLabel#ts    { color:#FFFFFF; font:bold 9pt 'Segoe UI';
                                   background:#283593; border-radius:4px;
                                   padding:4px 8px; margin:4px; }
                    QScrollArea  { border:none; background:transparent; }
                    QWidget#scroll_inner { background:transparent; }
                    QCheckBox    { color:#EEEEEE; font:9pt 'Segoe UI';
                                   padding:4px 8px; border-radius:4px; }
                    QCheckBox:hover { background:#2a2a4a; }
                    QCheckBox::indicator { width:15px; height:15px; }
                    QPushButton  { background:#1565C0; color:white; border:none;
                                   border-radius:6px; padding:7px 22px;
                                   font:bold 9pt 'Segoe UI'; }
                    QPushButton:hover    { background:#1976D2; }
                    QPushButton#cancel   { background:#37474F; }
                    QPushButton#cancel:hover { background:#546E7A; }
                    QFrame#sep   { color:#2d2d5e; }
                """)

                root = QVBoxLayout(dlg)
                root.setSpacing(4)
                root.setContentsMargins(14, 14, 14, 14)

                hdr = QLabel("Channel Selection")
                hdr.setObjectName("hdr")
                root.addWidget(hdr)

                if overlap_groups:
                    msg = (
                        "Multiple channels overlap at this time point.\n"
                        "Choose which channels to display in the marker:"
                    )
                else:
                    msg = (
                        "Select the channel(s) to include in this marker:"
                    )

                sub = QLabel(msg)
                sub.setObjectName("sub")
                sub.setWordWrap(True)
                root.addWidget(sub)

                ts_lbl = QLabel(f"  \u25cf  {date_s}   {time_s}")
                ts_lbl.setObjectName("ts")
                root.addWidget(ts_lbl)

                sep = QFrame(); sep.setFrameShape(QFrame.HLine); sep.setObjectName("sep")
                root.addWidget(sep)

                # scrollable channel list
                scroll = QScrollArea(); scroll.setWidgetResizable(True)
                inner  = QWidget(); inner.setObjectName("scroll_inner")
                vbox   = QVBoxLayout(inner)
                vbox.setSpacing(2); vbox.setContentsMargins(4, 4, 4, 4)
                scroll.setWidget(inner)
                root.addWidget(scroll)

                overlap_chs = {ch for g in overlap_groups for ch in g}
                checkboxes  = {}
                ch_colors   = {
                    ch: bright_colors[i % len(bright_colors)]
                    for i, ch in enumerate(active_channels)
                }

                for ch, val in ch_vals.items():
                    is_overlap = (
                        len(overlap_groups) > 0 and
                        ch in overlap_chs
                    )
                    cb = QCheckBox(f"{ch}:  {ch_vals[ch]} {_y_label}"
                                   + ("  ⚠ overlap" if is_overlap else ""))
                    cb.setChecked(True)
                    line_col = ch_colors.get(ch, "#ffffff")
                    cb.setStyleSheet(
                        f"QCheckBox {{ color:#EEEEEE; border-left:4px solid {line_col};"
                        f" padding-left:8px; background:{'#1e1e3a' if is_overlap else 'transparent'};"
                        f" border-radius:3px; }}"
                    )
                    checkboxes[ch] = cb
                    vbox.addWidget(cb)

                sep2 = QFrame(); sep2.setFrameShape(QFrame.HLine); sep2.setObjectName("sep")
                root.addWidget(sep2)

                btn_row = QHBoxLayout()
                ok_btn  = QPushButton("Add Marker")
                cl_btn  = QPushButton("Cancel"); cl_btn.setObjectName("cancel")
                ok_btn.clicked.connect(dlg.accept)
                cl_btn.clicked.connect(dlg.reject)
                btn_row.addStretch()
                btn_row.addWidget(ok_btn)
                btn_row.addWidget(cl_btn)
                root.addLayout(btn_row)

                if dlg.exec_() != QDialog.Accepted:
                    return None
                sel = {ch: v for ch, v in ch_vals.items()
                       if ch in checkboxes and checkboxes[ch].isChecked()}
                return sel if sel else None

            # ── drag support (replaces broken ann.draggable) ─────────────────

            def _ann_hit(ann, mouse_x, mouse_y):
                """Return True if mouse display coords are inside annotation bbox."""
                try:
                    renderer = plt.gcf().canvas.get_renderer()
                    bb = ann.get_window_extent(renderer)
                    return bb.contains(mouse_x, mouse_y)
                except Exception:
                    return False

            def on_press(event):
                if event.inaxes != ax:
                    return

                # ── right-click: delete nearest marker ───────────────────────
                if event.button == 3:
                    if not placed_markers:
                        return
                    raw_dt = mdates.num2date(event.xdata).replace(tzinfo=None)
                    x_ts   = pd.Timestamp(raw_dt)
                    best   = min(placed_markers,
                                 key=lambda m: abs((m["dt"] - x_ts).total_seconds()))
                    _remove_marker(best)
                    return

                if event.button != 1:
                    return

                # ── check if clicking on an annotation box (start drag) ───────
                for entry in placed_markers:
                    if _ann_hit(entry["annotation"], event.x, event.y):
                        _drag["active"] = True
                        _drag["entry"]  = entry
                        ann = entry["annotation"]
                        _drag["ox"] = event.x - ann.xyann[0]
                        _drag["oy"] = event.y - ann.xyann[1]
                        return

                # ── place new marker ─────────────────────────────────────────
                if len(placed_markers) >= MAX_MARKERS:
                    _show_msg(
                        "Markers",
                        f"Maximum {MAX_MARKERS} markers reached.\n"
                        "Right-click near any marker to delete it.",
                        "#ff4c4c",
                    )
                    return

                raw_dt     = mdates.num2date(event.xdata).replace(tzinfo=None)
                x_ts       = pd.Timestamp(raw_dt)
                label_idx  = (df1[1] - x_ts).abs().idxmin()
                nearest_dt = df1.loc[label_idx, 1]
                time_s     = nearest_dt.strftime("%H:%M:%S")
                date_s     = nearest_dt.strftime("%d-%m-%Y")

                ch_vals = _ch_values_at(label_idx)
                if not ch_vals:
                    return

                groups = _overlapping_groups(ch_vals)
                overlap_g = [g for g in groups if len(g) > 1]

                # Always ask when more than one channel is active
                if len(active_channels) > 1:
                    sel_vals = _ask_channels(
                        ch_vals,
                        time_s,
                        date_s,
                        overlap_g,          # empty list when there is no overlap
                    )
                    if sel_vals is None:
                        return
                else:
                    sel_vals = ch_vals

                _place_marker(nearest_dt, label_idx, sel_vals)

            def on_motion(event):
                if not _drag["active"] or event.inaxes != ax:
                    return
                ann = _drag["entry"]["annotation"]
                ann.xyann = (event.x - _drag["ox"], event.y - _drag["oy"])
                plt.gcf().canvas.draw_idle()

            def on_release(event):
                _drag["active"] = False
                _drag["entry"]  = None

            plt.gcf().canvas.mpl_connect("button_press_event",   on_press)
            plt.gcf().canvas.mpl_connect("motion_notify_event",  on_motion)
            plt.gcf().canvas.mpl_connect("button_release_event", on_release)

            base_filename = os.path.splitext(os.path.basename(file_path))[0]
            if active_channels:
                # Original legend style; re-ordered for row-major visual:
                # CH01..CH12 / CH13..CH24
                _sorted_pairs = sorted(
                    zip(lines, active_channels),
                    key=lambda p: int(re.sub(r"\D", "", str(p[1])) or 0),
                )
                _s_lines = [p[0] for p in _sorted_pairs]
                _s_labels = [_format_channel_label(p[1]) for p in _sorted_pairs]
                _ncol = min(len(_s_lines), 12)
                _nrows = (len(_s_lines) + _ncol - 1) // _ncol if _ncol else 1
                _rm_lines, _rm_labels = [], []
                for _col in range(_ncol):
                    for _row in range(_nrows):
                        _idx = _row * _ncol + _col
                        if _idx < len(_s_lines):
                            _rm_lines.append(_s_lines[_idx])
                            _rm_labels.append(_s_labels[_idx])
                plt.legend(
                    handles=_rm_lines,
                    labels=_rm_labels,
                    loc="upper center",
                    bbox_to_anchor=(0.5, -0.1),
                    ncol=_ncol,
                    handlelength=2.5,
                )

            def on_close(event):
                today_date = datetime.date.today().strftime("%d-%m-%Y")
                plt.savefig(graph_file_path)

            plt.gcf().canvas.mpl_connect("close_event", on_close)
            current_directory = os.path.dirname(os.path.abspath(__file__))
            image_path = get_app_icon_png(); img = plt.imread(image_path)
            img = plt.imread(image_path)
            imagebox = OffsetImage(img, zoom=0.2, alpha=0.65)
            ab = AnnotationBbox(
                imagebox,
                (0.99, 1.15),
                xycoords="axes fraction",
                frameon=False,
                box_alignment=(1, 1),
            )
            ax.add_artist(ab)

            # plt.text(
            #     0.93,
            #     1.04,
            #     " Sigma Controls",
            #     transform=ax.transAxes,
            #     fontsize=20,
            #     ha="right",
            #     va="top",
            #     color="grey",
            #     alpha=0.5,
            # )
            company_name = getattr(self, "company_name", "").strip()

            if company_name:
                fig = plt.gcf()
                fig.text(
                    0.05,
                    0.90,
                    company_name,
                    fontsize=18,
                    color="grey",
                    alpha=0.5,
                    ha="left",
                    va="top",
                )
            plt.text(
                0.995,
                1.03,
                "Controls",
                transform=ax.transAxes,
                fontsize=14,
                ha="right",
                va="top",
                color="#00A0E3",  # matches Sigma icon fill color exactly
                alpha=0.65,
            )

            plt.tight_layout()

            # Force minor ticks on so the minor gridline locators below
            # actually have tick positions to draw gridlines at.
            ax.minorticks_on()

            # Open the graph maximized to fill the screen.
            try:
                mgr = plt.get_current_fig_manager()
                mgr.window.showMaximized()

                # User-configurable minor gridline DENSITY, as scroll bars
                # (not a checkbox) added to the toolbar row directly below
                # the window's title bar -- one for vertical gridlines
                # (minor X ticks) and one for horizontal gridlines (minor Y
                # ticks), each 0-10 subdivisions per major interval.
                from PyQt5.QtWidgets import QScrollBar as _QScrollBar, QLabel as _QLabel
                from matplotlib.ticker import AutoMinorLocator as _AutoMinorLocatorGrid

                DEFAULT_MINOR_DIV = 5

                v_label = _QLabel(f"  V-Grid: {DEFAULT_MINOR_DIV} ")
                v_scroll = _QScrollBar(Qt.Horizontal)
                v_scroll.setRange(0, 10)
                v_scroll.setValue(DEFAULT_MINOR_DIV)
                v_scroll.setFixedWidth(120)

                h_label = _QLabel(f"  H-Grid: {DEFAULT_MINOR_DIV} ")
                h_scroll = _QScrollBar(Qt.Horizontal)
                h_scroll.setRange(0, 10)
                h_scroll.setValue(DEFAULT_MINOR_DIV)
                h_scroll.setFixedWidth(120)

                def _set_vertical_minor(n):
                    # Vertical gridlines come from the X axis's minor ticks.
                    v_label.setText(f"  V-Grid: {n} ")
                    if n <= 0:
                        ax.xaxis.grid(False, which="minor")
                    else:
                        ax.xaxis.set_minor_locator(_AutoMinorLocatorGrid(n + 1))
                        ax.xaxis.grid(
                            True, which="minor",
                            color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6,
                        )
                    ax.figure.canvas.draw_idle()

                def _set_horizontal_minor(n):
                    # Horizontal gridlines come from the Y axis's minor ticks.
                    h_label.setText(f"  H-Grid: {n} ")
                    if n <= 0:
                        ax.yaxis.grid(False, which="minor")
                    else:
                        ax.yaxis.set_minor_locator(_AutoMinorLocatorGrid(n + 1))
                        ax.yaxis.grid(
                            True, which="minor",
                            color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6,
                        )
                    ax.figure.canvas.draw_idle()

                v_scroll.valueChanged.connect(_set_vertical_minor)
                h_scroll.valueChanged.connect(_set_horizontal_minor)

                mgr.toolbar.addWidget(v_label)
                mgr.toolbar.addWidget(v_scroll)
                mgr.toolbar.addWidget(h_label)
                mgr.toolbar.addWidget(h_scroll)

            except Exception as maximize_err:
                pass

            plt.show()

            # Open the matching data-table window for the same channels
            # and date/time range used in this graph.
            self._open_channel_data_table(df1, df2, active_channels, file_path)

            df4 = pd.read_csv(filtered_file_path, header=None)
            split_columns = df4[1].str.split(" ", expand=True)
            df4 = pd.concat([df4.drop(columns=[1]), split_columns], axis=1)

            df4 = df4.drop(0)
            cols = df4.columns.tolist()
            new_cols = cols[-2:] + cols[:-2]
            df4 = df4[new_cols]
            df4.to_csv(filtered_file_path, index=False, header=False)

            df5 = pd.read_csv(filtered_file_path, header=None)
            df5 = df5.drop([df5.columns[1], df5.columns[3], df5.columns[4]], axis=1)
            df5.to_csv(filtered_file_path, index=False, header=False)
        else:
            df = pd.read_csv(file_path, header=None)
            df_str = pd.read_csv(file_path, header=None, dtype=str)
            df_str = df_str.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            time_str1 = self.start_time
            time_str2 = self.end_time
            date_str1 = self.start_date
            date_str2 = self.end_date

            start_dt_filter = pd.to_datetime(date_str1 + " " + time_str1, format="%d-%m-%Y %H:%M:%S")
            end_dt_filter = pd.to_datetime(date_str2 + " " + time_str2, format="%d-%m-%Y %H:%M:%S")
            row_dt = pd.to_datetime(df[0] + " " + df[1], format="%d-%m-%Y %H:%M:%S", errors="coerce")

            df1 = []
            for i in range(len(df)):
                if pd.notna(row_dt.iloc[i]) and start_dt_filter <= row_dt.iloc[i] <= end_dt_filter:
                    df1.append(df.iloc[i, :])

            # This is the fallback path taken when the primary filter above
            # found zero matching rows. Re-filtering the exact same file
            # with the exact same date/time range will deterministically
            # come up empty again -- previously it silently fell through
            # into ~600 lines of duplicate graph-building code and popped
            # up a blank, empty "Featured Graph" window with no error or
            # explanation. Tell the user instead of showing them nothing.
            if not df1:
                QMessageBox.warning(
                    self,
                    "No Data Found",
                    f"No readings were found between {date_str1} {time_str1} "
                    f"and {date_str2} {time_str2} in this CSV. Please choose "
                    f"a different date/time range.",
                )
                return

            df1 = pd.DataFrame(df1)
            df2 = pd.DataFrame(df1.iloc[:, 2 : df1.shape[1]])

            df1[1] = pd.to_datetime(df1[0] + " " + df1[1], format="%d-%m-%Y %H:%M:%S")
            df3 = pd.DataFrame(df1.iloc[:, 1].apply(self.time_str_to_float))

            filtered_file_path = file_path.replace(".csv", "_filtered.csv")
            filtered_df = pd.concat([df1[0], df1[1], df2], axis=1)
            filtered_df.to_csv(filtered_file_path, index=False, header=None)

            plt.figure(figsize=(19, 9.5), tight_layout=True)
            plt.gcf().canvas.manager.set_window_title(f"Sigma Controls | Graph - {file_path.split('/')[-1]}")

            lines = []
            bright_colors = [
                "red",
                "green",
                "blue",
                "orange",
                "purple",
                "pink",
                "cyan",
                "magenta",
                "yellow",
                "lime",
            ]
            active_channels = []

            # Channels that actually have data in this CSV/date range.
            available_channels = [
                f"CH{i + 1}" for i, col in enumerate(df2.columns) if df2[col].any() != 0
            ]
            # Ask which of those to include -- independent of the live
            # logging CH checkboxes, so an active logging session with 8
            # channels is never touched by generating a graph for fewer
            # (or more) channels from an old CSV.
            graph_selection = self._prompt_graph_channels(available_channels)
            if graph_selection is None:
                # Dialog was cancelled / closed via X -- open nothing.
                return

            for i, col in enumerate(df2.columns):
                ch_name = f"CH{i + 1}"
                channel_enabled = graph_selection.get(ch_name, True)

                if channel_enabled and df2[col].any() != 0:
                    color = bright_colors[i % len(bright_colors)]
                    (line,) = plt.plot(
                        df1[1], df2[col], label=_format_channel_label(ch_name), color=color
                    )
                    lines.append(line)
                    active_channels.append(ch_name)

            from matplotlib.dates import AutoDateLocator, AutoDateFormatter

            # min/max ticks keeps the gridline COUNT roughly constant
            # whether the data spans 10 readings or 30,000. Raised from
            # 6-10 -> 10-18: the old range read as "very few ticks" on a
            # maximized industrial-monitor-sized window.
            locator = AutoDateLocator(minticks=3, maxticks=10)
            ax = plt.gca()
            ax.set_facecolor((0.9, 0.98, 0.9))
            ax.xaxis.set_major_locator(locator)

            formatter = AutoDateFormatter(locator)
            formatter.scaled[1 / (24 * 60 * 60)] = "%H:%M:%S\n%d-%m-%Y"
            formatter.scaled[1 / (24 * 60)] = "%H:%M:%S\n%d-%m-%Y"
            formatter.scaled[1 / 24] = "%H:%M\n%d-%m-%Y"
            formatter.scaled[1] = "%d-%m-%Y"
            formatter.scaled[30] = "%m-%Y"
            formatter.scaled[365] = "%Y"
            ax.xaxis.set_major_formatter(formatter)

            # Same dynamic tick-density adjustment as the replay graph, so
            # a resized window doesn't overlap 2-line date/time labels.
            def _adjust_xtick_density(event=None):
                try:
                    fig_width_px = ax.figure.get_size_inches()[0] * ax.figure.dpi
                    new_max = max(3, min(10, int(fig_width_px // 120)))
                    new_locator = AutoDateLocator(minticks=3, maxticks=new_max)
                    ax.xaxis.set_major_locator(new_locator)
                    ax.figure.canvas.draw_idle()
                except Exception:
                    pass

            plt.gcf().canvas.mpl_connect("resize_event", _adjust_xtick_density)
            _adjust_xtick_density()

            plt.xlabel(
                "Date & Time (hh:mm:ss)", fontsize=16, color="#00A0E3", labelpad=6
            )
            plt.ylabel(
                str(self.graph_y_axis),
                fontsize=16,
                color="#00A0E3",
                labelpad=10,
            )
            plt.rcParams["axes.titlesize"] = 20
            plt.rcParams["axes.titlepad"] = 12
            plt.title("Featured Graph", fontsize=20, color="#00A0E3", pad=12)

            from matplotlib.ticker import AutoMinorLocator as _AutoMinorLocatorX

            # Explicit per-axis grid control (avoids matplotlib's implicit
            # visible-toggle quirk when mixing ax.grid()/ax.yaxis.grid() calls).
            ax.xaxis.grid(True, which="major", color=(0.4, 0.4, 0.4, 0.6), linestyle="-", linewidth=0.8)
            ax.xaxis.set_minor_locator(_AutoMinorLocatorX(4))  # denser minor gridlines (was 2)
            ax.xaxis.grid(True, which="minor", color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6)
            ax.yaxis.grid(True, which="major", color=(0.4, 0.4, 0.4, 0.6), linestyle="-", linewidth=0.8)

            # ── Single source of truth for the actual plotted span ──
            start_dt = pd.to_datetime(
                self.start_date + " " + self.start_time, format="%d-%m-%Y %H:%M:%S"
            )
            end_dt = pd.to_datetime(
                self.end_date + " " + self.end_time, format="%d-%m-%Y %H:%M:%S"
            )
            total_minutes = max(1, int((end_dt - start_dt).total_seconds() / 60))
            # ── Start / Stop markers on X-axis ──

            ax.axvline(
                x=start_dt,
                color="green",
                linewidth=1.5,
                linestyle="--",
                zorder=5,
                label="Start",
                alpha=0.7,
            )
            ax.axvline(
                x=end_dt,
                color="red",
                linewidth=1.5,
                linestyle="--",
                zorder=5,
                label="Stop",
                alpha=0.7,
            )

            ax.text(
                start_dt,
                ax.get_ylim()[0],
                f"START\n{self.start_time}\n{self.start_date}",
                color="green",
                fontsize=10,
                va="top",
                ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=1),
            )

            ax.text(
                end_dt,
                ax.get_ylim()[0],
                f"STOP\n{self.end_time}\n{self.end_date}",
                color="red",
                fontsize=10,
                va="top",
                ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=1),
            )

            from matplotlib.ticker import AutoMinorLocator

            ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=14, min_n_ticks=10))
            ax.yaxis.set_minor_locator(AutoMinorLocator(4))  # denser minor gridlines (was 2)
            ax.yaxis.grid(
                True, which="minor", color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6
            )
            ax.tick_params(which="major", width=1, length=7)
            ax.tick_params(which="minor", width=0.8, length=4)

            (crosshair,) = plt.plot([], [], "r--", visible=False)
            coords_text = plt.text(
                0.95,
                0.95,
                "",
                transform=plt.gca().transAxes,
                ha="right",
                va="top",
                fontsize=12,
                color="black",
            )

            # ----- X,Y Data Tips -------
            def on_hover(event):
                if event.inaxes == plt.gca():
                    x, y = event.xdata, event.ydata
                    if x is not None:
                        x_timestamp = pd.Timestamp(x, unit="s")
                        index = (df1[1] - x_timestamp).abs().idxmin()
                        nearest_timestamp = df1.iloc[index, 1].strftime("%H:%M:%S")
                        crosshair.set_data(
                            [df1.iloc[index, 1], df1.iloc[index, 1]],
                            [plt.gca().get_ylim()[0], plt.gca().get_ylim()[1]],
                        )
                        coords_text.set_text(
                            f"Time: {nearest_timestamp}, {self.graph_y_axis}: {y:.2f}"
                        )
                        # crosshair.set_visible(True)
                        coords_text.set_visible(True)
                    else:
                        crosshair.set_visible(False)
                        coords_text.set_visible(False)
                else:
                    crosshair.set_visible(False)
                    coords_text.set_visible(False)

                plt.gcf().canvas.draw()

            plt.gcf().canvas.mpl_connect("motion_notify_event", on_hover)

            # ── Permanent Markers (max 5) ──
            # Left-click  = place marker
            # Right-click = delete nearest marker
            # Drag        = move annotation box anywhere on graph
            import matplotlib.dates as mdates
            from PyQt5.QtWidgets import (
                QDialog, QVBoxLayout, QHBoxLayout,
                QCheckBox, QPushButton, QLabel, QFrame, QScrollArea, QWidget
            )

            MAX_MARKERS   = 5
            placed_markers = []
            _show_msg  = self.show_message
            _icon_path = get_app_icon_svg()
            _y_label   = self.graph_y_axis
            # 5 distinct colors — one per marker slot
            MARKER_COLORS = ["#1565C0", "#7B1FA2", "#00695C", "#E65100", "#B71C1C"]
            MARKER_BG     = ["#E3F2FD", "#F3E5F5", "#E0F2F1", "#FFF3E0", "#FFEBEE"]
            _drag = {"active": False, "entry": None, "ox": 0, "oy": 0}

            # ── helpers ──────────────────────────────────────────────────────

            def _row_pos_from_idx(label_idx):
                """Convert df1 label-index to integer position in df2."""
                try:
                    return df2.index.get_loc(label_idx)
                except Exception:
                    return 0

            def _ch_values_at(nearest_idx):
                result = {}
                try:
                    dt = df1.loc[nearest_idx, 1]
                    date_part = dt.strftime("%d-%m-%Y")
                    time_part = dt.strftime("%H:%M:%S")
                    match = df_str[(df_str[0] == date_part) & (df_str[1] == time_part)]
                    if not match.empty:
                        row = match.iloc[0]
                        for col_i, col in enumerate(df2.columns):
                            lbl = f"CH{col_i + 1}"
                            if lbl in active_channels:
                                csv_col = col_i + 2
                                val = str(row.iloc[csv_col]).strip()
                                if val and val.lower() != "nan":
                                    try:
                                        result[lbl] = f"{float(val):.2f}"
                                    except Exception:
                                        result[lbl] = val
                except Exception:
                    pass
                return result

            def _overlapping_groups(ch_vals):
                keys = list(ch_vals.keys())
                visited = set()
                groups = []
                for i in range(len(keys)):
                    if keys[i] in visited:
                        continue
                    grp = [keys[i]]
                    visited.add(keys[i])
                    try:
                        vi = float(ch_vals[keys[i]])
                    except Exception:
                        continue
                    for j in range(i + 1, len(keys)):
                        if keys[j] in visited:
                            continue
                        try:
                            vj = float(ch_vals[keys[j]])
                        except Exception:
                            continue

                        if abs(vi - vj) < 0.001:
                            grp.append(keys[j])
                            visited.add(keys[j])
                    groups.append(grp)
                return [g for g in groups if len(g) > 1]

            def _make_label(num, sel_vals, time_s, date_s):
                lines_t = []

                # Bold title
                lines_t.append(rf"$\bf{{M{num}\ \ \ {date_s}\ \ \ {time_s}}}$")

                # Separator
                lines_t.append("─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─")

                # Bold channel names only
                for ch, v in sel_vals.items():
                    lines_t.append(
                        rf"$\bf{{{ch}}}$: {v} {_y_label}"
                    )

                return "\n".join(lines_t)

            def _place_marker(nearest_dt, label_idx, sel_vals):
                num   = len(placed_markers) + 1
                color = MARKER_COLORS[(num - 1) % len(MARKER_COLORS)]
                bg    = MARKER_BG[(num - 1) % len(MARKER_BG)]
                time_s = nearest_dt.strftime("%H:%M:%S")
                date_s = nearest_dt.strftime("%d-%m-%Y")
                text   = _make_label(num, sel_vals, time_s, date_s)

                vline = ax.axvline(
                    x=nearest_dt, color=color, linewidth=1.8,
                    linestyle=(0, (6, 3)), alpha=0.9, zorder=6
                )

                # Number label on the vline at top
                y_lo, y_hi = ax.get_ylim()
                num_txt = ax.text(
                    nearest_dt, y_hi - (y_hi - y_lo) * 0.03,
                    f" M{num} ", fontsize=8, color="white",
                    fontweight="bold", va="top", ha="center",
                    bbox=dict(boxstyle="round,pad=0.2", fc=color, ec="none", alpha=0.95),
                    zorder=10,
                )

                # Annotation box — use offset points so no Timestamp in xyann
                ann_x_disp, ann_y_disp = ax.transData.transform(
                    (mdates.date2num(nearest_dt), y_lo + (y_hi - y_lo) * 0.72)
                )
                ann = ax.annotate(
                    text,
                    xy=(nearest_dt, y_lo + (y_hi - y_lo) * 0.72),
                    xytext=(ann_x_disp + 8, ann_y_disp),
                    textcoords="figure pixels",
                    fontsize=8.5,
                    color="#111111",
                    fontfamily="monospace",
                    bbox=dict(
                        boxstyle="round,pad=0.55",
                        fc=bg, ec=color,
                        linewidth=2.0, alpha=0.95,
                    ),
                    zorder=9,
                    annotation_clip=False,
                    arrowprops=dict(
                        arrowstyle="-",
                        color=color, lw=1.2, alpha=0.6,
                    ),
                )

                entry = {
                    "vline": vline, "annotation": ann, "num_txt": num_txt,
                    "color": color, "dt": nearest_dt, "idx": label_idx, "num": num,
                }
                placed_markers.append(entry)
                plt.gcf().canvas.draw_idle()

            def _remove_marker(entry):
                for k in ("vline", "annotation", "num_txt"):
                    try:
                        entry[k].remove()
                    except Exception:
                        pass
                if entry in placed_markers:
                    placed_markers.remove(entry)
                plt.gcf().canvas.draw_idle()

            def _ask_channels(ch_vals, time_s, date_s, overlap_groups):
                """Dialog shown only when channels truly overlap. Shows all channels,
                highlights the overlapping ones so user knows why they're being asked."""
                dlg = QDialog()
                dlg.setWindowTitle("Select Channels for Marker")
                dlg.setWindowIcon(QIcon(_icon_path))
                dlg.setMinimumWidth(480)
                dlg.setStyleSheet("""
                    QDialog      { background:#1a1a2e; }
                    QLabel#hdr   { color:#90CAF9; font:bold 11pt 'Segoe UI';
                                   padding:6px 4px 2px 4px; }
                    QLabel#sub   { color:#9E9E9E; font:9pt 'Segoe UI';
                                   padding:0 4px 4px 4px; }
                    QLabel#ts    { color:#FFFFFF; font:bold 9pt 'Segoe UI';
                                   background:#283593; border-radius:4px;
                                   padding:4px 8px; margin:4px; }
                    QScrollArea  { border:none; background:transparent; }
                    QWidget#scroll_inner { background:transparent; }
                    QCheckBox    { color:#EEEEEE; font:9pt 'Segoe UI';
                                   padding:4px 8px; border-radius:4px; }
                    QCheckBox:hover { background:#2a2a4a; }
                    QCheckBox::indicator { width:15px; height:15px; }
                    QPushButton  { background:#1565C0; color:white; border:none;
                                   border-radius:6px; padding:7px 22px;
                                   font:bold 9pt 'Segoe UI'; }
                    QPushButton:hover    { background:#1976D2; }
                    QPushButton#cancel   { background:#37474F; }
                    QPushButton#cancel:hover { background:#546E7A; }
                    QFrame#sep   { color:#2d2d5e; }
                """)

                root = QVBoxLayout(dlg)
                root.setSpacing(4)
                root.setContentsMargins(14, 14, 14, 14)

                hdr = QLabel("Channel Selection")
                hdr.setObjectName("hdr")
                root.addWidget(hdr)

                if overlap_groups:
                    msg = (
                        "Multiple channels overlap at this time point.\n"
                        "Choose which channels to display in the marker:"
                    )
                else:
                    msg = (
                        "Select the channel(s) to include in this marker:"
                    )

                sub = QLabel(msg)
                sub.setObjectName("sub")
                sub.setWordWrap(True)
                root.addWidget(sub)

                ts_lbl = QLabel(f"  \u25cf  {date_s}   {time_s}")
                ts_lbl.setObjectName("ts")
                root.addWidget(ts_lbl)

                sep = QFrame(); sep.setFrameShape(QFrame.HLine); sep.setObjectName("sep")
                root.addWidget(sep)

                # scrollable channel list
                scroll = QScrollArea(); scroll.setWidgetResizable(True)
                inner  = QWidget(); inner.setObjectName("scroll_inner")
                vbox   = QVBoxLayout(inner)
                vbox.setSpacing(2); vbox.setContentsMargins(4, 4, 4, 4)
                scroll.setWidget(inner)
                root.addWidget(scroll)

                overlap_chs = {ch for g in overlap_groups for ch in g}
                checkboxes  = {}
                ch_colors   = {
                    ch: bright_colors[i % len(bright_colors)]
                    for i, ch in enumerate(active_channels)
                }

                for ch, val in ch_vals.items():
                    is_overlap = (
                        len(overlap_groups) > 0 and
                        ch in overlap_chs
                    )
                    cb = QCheckBox(f"{ch}:  {ch_vals[ch]} {_y_label}"
                                   + ("  ⚠ overlap" if is_overlap else ""))
                    cb.setChecked(True)
                    line_col = ch_colors.get(ch, "#ffffff")
                    cb.setStyleSheet(
                        f"QCheckBox {{ color:#EEEEEE; border-left:4px solid {line_col};"
                        f" padding-left:8px; background:{'#1e1e3a' if is_overlap else 'transparent'};"
                        f" border-radius:3px; }}"
                    )
                    checkboxes[ch] = cb
                    vbox.addWidget(cb)

                sep2 = QFrame(); sep2.setFrameShape(QFrame.HLine); sep2.setObjectName("sep")
                root.addWidget(sep2)

                btn_row = QHBoxLayout()
                ok_btn  = QPushButton("Add Marker")
                cl_btn  = QPushButton("Cancel"); cl_btn.setObjectName("cancel")
                ok_btn.clicked.connect(dlg.accept)
                cl_btn.clicked.connect(dlg.reject)
                btn_row.addStretch()
                btn_row.addWidget(ok_btn)
                btn_row.addWidget(cl_btn)
                root.addLayout(btn_row)

                if dlg.exec_() != QDialog.Accepted:
                    return None
                sel = {ch: v for ch, v in ch_vals.items()
                       if ch in checkboxes and checkboxes[ch].isChecked()}
                return sel if sel else None

            # ── drag support (replaces broken ann.draggable) ─────────────────

            def _ann_hit(ann, mouse_x, mouse_y):
                """Return True if mouse display coords are inside annotation bbox."""
                try:
                    renderer = plt.gcf().canvas.get_renderer()
                    bb = ann.get_window_extent(renderer)
                    return bb.contains(mouse_x, mouse_y)
                except Exception:
                    return False

            def on_press(event):
                if event.inaxes != ax:
                    return

                # ── right-click: delete nearest marker ───────────────────────
                if event.button == 3:
                    if not placed_markers:
                        return
                    raw_dt = mdates.num2date(event.xdata).replace(tzinfo=None)
                    x_ts   = pd.Timestamp(raw_dt)
                    best   = min(placed_markers,
                                 key=lambda m: abs((m["dt"] - x_ts).total_seconds()))
                    _remove_marker(best)
                    return

                if event.button != 1:
                    return

                # ── check if clicking on an annotation box (start drag) ───────
                for entry in placed_markers:
                    if _ann_hit(entry["annotation"], event.x, event.y):
                        _drag["active"] = True
                        _drag["entry"]  = entry
                        ann = entry["annotation"]
                        _drag["ox"] = event.x - ann.xyann[0]
                        _drag["oy"] = event.y - ann.xyann[1]
                        return

                # ── place new marker ─────────────────────────────────────────
                if len(placed_markers) >= MAX_MARKERS:
                    _show_msg(
                        "Markers",
                        f"Maximum {MAX_MARKERS} markers reached.\n"
                        "Right-click near any marker to delete it.",
                        "#ff4c4c",
                    )
                    return

                raw_dt     = mdates.num2date(event.xdata).replace(tzinfo=None)
                x_ts       = pd.Timestamp(raw_dt)
                label_idx  = (df1[1] - x_ts).abs().idxmin()
                nearest_dt = df1.loc[label_idx, 1]
                time_s     = nearest_dt.strftime("%H:%M:%S")
                date_s     = nearest_dt.strftime("%d-%m-%Y")

                ch_vals = _ch_values_at(label_idx)
                if not ch_vals:
                    return

                groups = _overlapping_groups(ch_vals)
                overlap_g = [g for g in groups if len(g) > 1]

                # Always ask when more than one channel is active
                if len(active_channels) > 1:
                    sel_vals = _ask_channels(
                        ch_vals,
                        time_s,
                        date_s,
                        overlap_g,          # empty list when there is no overlap
                    )
                    if sel_vals is None:
                        return
                else:
                    sel_vals = ch_vals

                _place_marker(nearest_dt, label_idx, sel_vals)

            def on_motion(event):
                if not _drag["active"] or event.inaxes != ax:
                    return
                ann = _drag["entry"]["annotation"]
                ann.xyann = (event.x - _drag["ox"], event.y - _drag["oy"])
                plt.gcf().canvas.draw_idle()

            def on_release(event):
                _drag["active"] = False
                _drag["entry"]  = None

            plt.gcf().canvas.mpl_connect("button_press_event",   on_press)
            plt.gcf().canvas.mpl_connect("motion_notify_event",  on_motion)
            plt.gcf().canvas.mpl_connect("button_release_event", on_release)

            base_filename = os.path.splitext(os.path.basename(file_path))[0]
            if active_channels:
                # Original legend style; re-ordered for row-major visual:
                # CH01..CH12 / CH13..CH24
                _sorted_pairs = sorted(
                    zip(lines, active_channels),
                    key=lambda p: int(re.sub(r"\D", "", str(p[1])) or 0),
                )
                _s_lines = [p[0] for p in _sorted_pairs]
                _s_labels = [_format_channel_label(p[1]) for p in _sorted_pairs]
                _ncol = min(len(_s_lines), 12)
                _nrows = (len(_s_lines) + _ncol - 1) // _ncol if _ncol else 1
                _rm_lines, _rm_labels = [], []
                for _col in range(_ncol):
                    for _row in range(_nrows):
                        _idx = _row * _ncol + _col
                        if _idx < len(_s_lines):
                            _rm_lines.append(_s_lines[_idx])
                            _rm_labels.append(_s_labels[_idx])
                plt.legend(
                    handles=_rm_lines,
                    labels=_rm_labels,
                    loc="upper center",
                    bbox_to_anchor=(0.5, -0.1),
                    ncol=_ncol,
                    handlelength=2.5,
                )

            def on_close(event):
                today_date = datetime.date.today().strftime("%d-%m-%Y")
                plt.savefig(graph_file_path)

            plt.gcf().canvas.mpl_connect("close_event", on_close)

            img = plt.imread(get_app_icon_png())
            imagebox = OffsetImage(img, zoom=0.2, alpha=0.65)
            ab = AnnotationBbox(
                imagebox,
                (0.99, 1.14),
                xycoords="axes fraction",
                frameon=False,
                box_alignment=(1, 1),
            )
            ax.add_artist(ab)

            # plt.text(
            #     0.93,
            #     1.06,
            #     " Sigma Controls",
            #     transform=ax.transAxes,
            #     fontsize=20,
            #     ha="right",
            #     va="top",
            #     color="grey",
            #     alpha=0.5,
            # )
            plt.text(
                0.995,
                1.03,
                "Controls",
                transform=ax.transAxes,
                fontsize=14,
                ha="right",
                va="top",
                color="#00A0E3",  # matches Sigma icon fill color exactly
                alpha=0.65,
            )

            plt.tight_layout()

            # Force minor ticks on so the minor gridline locators below
            # actually have tick positions to draw gridlines at.
            ax.minorticks_on()

            # Open the graph maximized to fill the screen.
            try:
                mgr = plt.get_current_fig_manager()
                mgr.window.showMaximized()

                # User-configurable minor gridline DENSITY, as scroll bars
                # (not a checkbox) added to the toolbar row directly below
                # the window's title bar -- one for vertical gridlines
                # (minor X ticks) and one for horizontal gridlines (minor Y
                # ticks), each 0-10 subdivisions per major interval.
                from PyQt5.QtWidgets import QScrollBar as _QScrollBar, QLabel as _QLabel
                from matplotlib.ticker import AutoMinorLocator as _AutoMinorLocatorGrid

                DEFAULT_MINOR_DIV = 5

                v_label = _QLabel(f"  V-Grid: {DEFAULT_MINOR_DIV} ")
                v_scroll = _QScrollBar(Qt.Horizontal)
                v_scroll.setRange(0, 10)
                v_scroll.setValue(DEFAULT_MINOR_DIV)
                v_scroll.setFixedWidth(120)

                h_label = _QLabel(f"  H-Grid: {DEFAULT_MINOR_DIV} ")
                h_scroll = _QScrollBar(Qt.Horizontal)
                h_scroll.setRange(0, 10)
                h_scroll.setValue(DEFAULT_MINOR_DIV)
                h_scroll.setFixedWidth(120)

                def _set_vertical_minor(n):
                    # Vertical gridlines come from the X axis's minor ticks.
                    v_label.setText(f"  V-Grid: {n} ")
                    if n <= 0:
                        ax.xaxis.grid(False, which="minor")
                    else:
                        ax.xaxis.set_minor_locator(_AutoMinorLocatorGrid(n + 1))
                        ax.xaxis.grid(
                            True, which="minor",
                            color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6,
                        )
                    ax.figure.canvas.draw_idle()

                def _set_horizontal_minor(n):
                    # Horizontal gridlines come from the Y axis's minor ticks.
                    h_label.setText(f"  H-Grid: {n} ")
                    if n <= 0:
                        ax.yaxis.grid(False, which="minor")
                    else:
                        ax.yaxis.set_minor_locator(_AutoMinorLocatorGrid(n + 1))
                        ax.yaxis.grid(
                            True, which="minor",
                            color=(0.5, 0.5, 0.5, 0.4), linestyle=":", linewidth=0.6,
                        )
                    ax.figure.canvas.draw_idle()

                v_scroll.valueChanged.connect(_set_vertical_minor)
                h_scroll.valueChanged.connect(_set_horizontal_minor)

                mgr.toolbar.addWidget(v_label)
                mgr.toolbar.addWidget(v_scroll)
                mgr.toolbar.addWidget(h_label)
                mgr.toolbar.addWidget(h_scroll)

            except Exception as maximize_err:
                pass

            plt.show()

            # Open the matching data-table window for the same channels
            # and date/time range used in this graph.
            self._open_channel_data_table(df1, df2, active_channels, file_path)

            df4 = pd.read_csv(filtered_file_path, header=None)
            split_columns = df4[1].str.split(" ", expand=True)
            df4 = pd.concat([df4.drop(columns=[1]), split_columns], axis=1)

            df4 = df4.drop(0)
            cols = df4.columns.tolist()
            new_cols = cols[-2:] + cols[:-2]
            df4 = df4[new_cols]
            df4.to_csv(filtered_file_path, index=False, header=False)

            df5 = pd.read_csv(filtered_file_path, header=None)
            df5 = df5.drop([df5.columns[1], df5.columns[3], df5.columns[4]], axis=1)
            df5.to_csv(filtered_file_path, index=False, header=False)

    # --------- Print btn for (generate PDF) ------------
    def print_button(self):
        write_event("ADMIN", "PDF", "Report generated")
        self.load_config()
        file_path = self.csv_filepath
        file_name = os.path.basename(file_path).strip(".csv")

        file_path = self.csv_filepath
        file_name = os.path.basename(file_path).strip(".csv")
        if file_path:
            base_directory_path = file_path.replace(f"{file_name}.csv", "")
            # Each Print click gets its own fresh output folder
            # (file_name_1, file_name_2, ...) instead of dumping every
            # PDF/CSV into the same folder as the source CSV -- repeated
            # prints no longer overwrite each other's output, and each
            # run's files are easy to find together.
            n = 1
            while True:
                candidate = os.path.join(base_directory_path, f"{file_name}_{n}")
                if not os.path.exists(candidate):
                    break
                n += 1
            directory_path = candidate
            os.makedirs(directory_path, exist_ok=True)

            graph_file_path = os.path.join(directory_path, f"{file_name}_graph.png")
            pdf_file_path = os.path.join(directory_path, f"{file_name}_graph.pdf")
            filtered_csv_file_path = os.path.join(
                directory_path, f"{file_name}_filtered.csv"
            )

            # The graph PNG is only ever generated when the interactive
            # Submit replay window is closed (its on_close handler saves
            # it into base_directory_path -- the plain CSV folder, not
            # this new per-print subfolder). Copy it across so this
            # folder is self-contained, instead of pdf.image() failing
            # with FileNotFoundError because it's looking in a folder
            # that graph.png was never actually written to.
            base_graph_png = os.path.join(base_directory_path, f"{file_name}_graph.png")
            if os.path.exists(base_graph_png):
                try:
                    shutil.copy2(base_graph_png, graph_file_path)
                except Exception as e:
                    self.show_message(
                        "Print",
                        f"Could not copy the graph image into the output "
                        f"folder:\n{e}",
                        "#ff4c4c",
                    )
                    return
            else:
                self.show_message(
                    "Print",
                    "No graph image found yet. Please click Submit and "
                    "close the graph window first (this generates the "
                    "graph image), then click Print again.",
                    "#ff4c4c",
                )
                return

            # Same story as the graph PNG -- the filtered CSV is only
            # ever generated by submit_button (into base_directory_path,
            # the plain CSV folder), never by print_button itself. This
            # is what create_csv_pdf() below reads from to build the
            # per-channel CSV PDFs, so without copying it into the new
            # subfolder those PDFs (and the filtered CSV itself) end up
            # silently missing from every print's output folder.
            base_filtered_csv = os.path.join(
                base_directory_path, f"{file_name}_filtered.csv"
            )
            if os.path.exists(base_filtered_csv):
                try:
                    shutil.copy2(base_filtered_csv, filtered_csv_file_path)
                except Exception as e:
                    self.show_message(
                        "Print",
                        f"Could not copy the filtered CSV into the output "
                        f"folder:\n{e}",
                        "#ff4c4c",
                    )
                    return
            else:
                self.show_message(
                    "Print",
                    "No filtered CSV found yet. Please click Submit and "
                    "close the graph window first (this generates it), "
                    "then click Print again.",
                    "#ff4c4c",
                )
                return

        file_path = self.csv_filepath
        letter_path = self.letterhead_file
        header = self.ui.textEdit.toPlainText()

        # First PDF (landscape, for graph)
        pdf = FPDF(format="A4", unit="mm", orientation="landscape")
        pdf.add_page()

        # Page margins (mm) -- tight so letterhead/graph go edge-to-edge
        # without overlapping each other or the page edge.
        _m = 5  # left/right margin
        _gap = 1.2  # vertical gap between sections
        # Graph must own at least 70% of the page height so the plot is
        # the focus; letterhead stays readable but secondary.
        MIN_GRAPH_H = pdf.h * 0.70  # ~147 mm on A4 landscape (210 mm)
        # Hard cap on letterhead height on THIS pdf only (table pdf is separate)
        MAX_LETTER_H_GRAPH = 38  # mm — full-width banner, not dominant

        notes_reserve = 16 if header.strip() else 0
        top_budget = 2 + MAX_LETTER_H_GRAPH + _gap + notes_reserve + _gap + 2
        # If notes are long, still protect the 70% graph floor
        if pdf.h - top_budget < MIN_GRAPH_H:
            MAX_LETTER_H_GRAPH = max(28, pdf.h - MIN_GRAPH_H - notes_reserve - 2 * _gap - 4)

        if os.path.exists(letter_path):
            fitted_letter_path, lw_px, lh_px = self.prepare_letterhead_image(letter_path)
            max_letter_w = pdf.w - 2 * _m
            # Full page width, height capped so graph keeps >= 70%
            letter_w = max_letter_w
            natural_h = max_letter_w * (self.LETTERHEAD_BOX_H / float(self.LETTERHEAD_BOX_W))
            letter_h = min(natural_h, MAX_LETTER_H_GRAPH)
            letterhead_y = 2
            letter_x = _m
            pdf.image(fitted_letter_path, x=letter_x, y=letterhead_y, w=letter_w, h=letter_h)
            content_y = letterhead_y + letter_h + _gap
        else:
            content_y = 4

        if header.strip():
            company_name = ""  # Change done here
            pdf.set_font("Helvetica", "B", 16)
            company_width = pdf.get_string_width(company_name)
            box_width = pdf.w - 2 * _m - company_width

            pdf.set_xy(_m, content_y)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(box_width, 4.0, txt=header, border=1, align="L")
            graph_y = pdf.get_y() + _gap
        else:
            pdf.set_text_color(0, 0, 0)
            graph_y = content_y

        # Graph fills ALL remaining space — guaranteed >= ~70% page height
        bottom_margin = 2
        max_w = pdf.w - 2 * _m
        max_h = pdf.h - graph_y - bottom_margin
        if max_h < MIN_GRAPH_H:
            max_h = MIN_GRAPH_H
        try:
            draw_w = max_w
            draw_h = max_h
            draw_x = _m
            pdf.image(graph_file_path, x=draw_x, y=graph_y, w=draw_w, h=draw_h)
        except Exception:
            pdf.image(graph_file_path, x=_m, y=graph_y, w=max_w)

        pdf.output(pdf_file_path)
        write_event("ADMIN", "PDF", pdf_file_path)

        # Function to create CSV PDFs for specified channel ranges
        def create_csv_pdf(start_col, end_col, pdf_suffix):
            header = self.ui.textEdit.toPlainText()
            new_pdf_path = os.path.join(
                directory_path, f"{file_name}_csv_{pdf_suffix}.pdf"
            )
            pdf = FPDF(format="A4", unit="mm", orientation="portrait")
            pdf.add_page()

            if os.path.exists(letter_path):
                fitted_letter_path, lw_px, lh_px = self.prepare_letterhead_image(letter_path)
                # Fixed 980x200 box; smaller images are centered on white.
                # Use top of page (y=3) so the banner gets full vertical room.
                _m = 5
                max_letter_w = pdf.w - 2 * _m
                letter_w = max_letter_w
                letter_h = max_letter_w * (self.LETTERHEAD_BOX_H / float(self.LETTERHEAD_BOX_W))
                page_max_h = 70  # leave room for notes + title + table
                if letter_h > page_max_h:
                    letter_h = page_max_h
                    letter_w = letter_h * (self.LETTERHEAD_BOX_W / float(self.LETTERHEAD_BOX_H))
                letterhead_y = 3
                letter_x = _m + (max_letter_w - letter_w) / 2.0
                pdf.image(fitted_letter_path, x=letter_x, y=letterhead_y, w=letter_w, h=letter_h)
                content_y = letterhead_y + letter_h + 2
            else:
                content_y = 10

            # Layout (top → bottom, no overlaps):
            #   letterhead
            #   notes box (left, narrow)     +  Sigma icon / Controls (right)
            #   company name  |  Table Record
            #   data table
            notes_x = 10
            notes_w = 165  # leaves ~25mm clear on the right for the icon
            icon_x = 182
            icon_h = 11

            # Notes / header box
            pdf.set_xy(notes_x, content_y)
            pdf.set_font("Times", size=12)
            if header.strip():
                pdf.multi_cell(
                    notes_w,
                    5,
                    txt=header,
                    border=1,
                    align="L",
                )
            notes_bottom = pdf.get_y()

            # Sigma icon + "Controls" top-aligned with the notes box, clear of it
            icon_path = get_app_icon_png()
            icon_y = content_y
            if os.path.exists(icon_path):
                pdf.image(icon_path, x=icon_x, y=icon_y, w=icon_h, h=icon_h)

            pdf.set_font("Helvetica", "B", 9)
            pdf.set_text_color(0, 160, 227)
            controls_label_y = icon_y + icon_h + 0.4
            pdf.set_xy(icon_x - 1, controls_label_y)
            pdf.cell(icon_h + 4, 3.5, txt="Controls", ln=False, align="C")
            pdf.set_text_color(0, 0, 0)
            icon_block_bottom = controls_label_y + 4

            # Company name + "Table Record" clearly BELOW notes box (and icon)
            title_y = max(notes_bottom, icon_block_bottom) + 3
            company_name = getattr(self, "company_name", "").strip()

            pdf.set_font("Helvetica", "B", 12)
            pdf.set_xy(10, title_y)
            pdf.set_text_color(191, 191, 191)
            pdf.cell(70, 8, company_name, 0, 0, "L")

            pdf.set_xy((pdf.w / 2) - 30, title_y)
            pdf.set_text_color(0, 160, 227)
            pdf.cell(60, 8, "Table Record", 0, 1, "C")
            pdf.set_text_color(0, 0, 0)

            date_time_width = 25
            column_width = 17.5

            with open(filtered_csv_file_path, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)

                non_empty_cols = [0, 1]
                for i in range(start_col, min(end_col, len(rows[0]))):
                    ch_name = f"CH{i - 1}"
                    # Only include a channel if it has data AND it was left
                    # checked in the graph's channel-selection dialog (same
                    # selection used for the Featured Graph, so the table
                    # matches what was plotted).
                    channel_enabled = self._graph_channel_selection.get(ch_name, True)
                    if channel_enabled and any(row[i].strip() for row in rows):
                        non_empty_cols.append(i)

                if len(non_empty_cols) > 2:
                    # Table starts cleanly below the title row
                    table_start_y = title_y + 10
                    pdf.set_y(table_start_y)
                    headers = ["Date", "Time"] + [
                        f"CH{str(i - 1).zfill(2)}" for i in non_empty_cols if i >= 2
                    ]

                    pdf.set_xy(10, pdf.get_y())
                    pdf.set_font("Helvetica", "B", 12)
                    for i, header in enumerate(headers):
                        width = date_time_width if i < 2 else column_width
                        pdf.cell(width, 10, header, 1, 0, "C")
                    pdf.ln()

                    pdf.set_font("Helvetica", size=12)
                    for row in rows:
                        for i, col_index in enumerate(non_empty_cols):
                            width = date_time_width if i < 2 else column_width
                            pdf.cell(
                                width,
                                10,
                                row[col_index] if col_index < len(row) else "",
                                1,
                            )
                        pdf.ln()

                    pdf.set_font("Helvetica", "B", 12)
                    total_width = date_time_width * 2 + column_width * (
                        len(headers) - 2
                    )
                    pdf.cell(total_width, 0, "", "T")
                    pdf.output(new_pdf_path)
                    write_event("ADMIN", "PDF", pdf_file_path)

        # Define channel ranges and create PDFs
        channel_ranges = [(2, 10, "CH01-08"), (10, 18, "CH09-16"), (18, 26, "CH17-24")]

        for start_col, end_col, suffix in channel_ranges:
            create_csv_pdf(start_col, end_col, suffix)

        self.show_message("Print", "PDF Documents Created Successfully!", "#02c702")


# ---------- Communication Thread ------------


class Worker(QThread):
    update_signal = pyqtSignal(int, object)  # slave_num, registers (None = fail)
    error_signal = pyqtSignal(int, str)  # slave_num, error message
    comm_status_signal = pyqtSignal(str)  # "connected" | "reconnecting" | "lost"
    crashed_signal = pyqtSignal(str)  # unhandled exception message

    # How many consecutive fails before showing a message (avoids spam)
    FAIL_THRESHOLD = 3

    def __init__(
        self, com, baud, log_time, slave_configs, parity="N", stopbits=1, databits=8
    ):
        super().__init__()
        self.com = com
        self.baud = baud
        self.log_time = log_time
        self.slave_configs = slave_configs
        self.parity = parity
        self.stopbits = stopbits
        self.databits = databits
        self.running = True
        self.fail_counts = {sc["num"]: 0 for sc in slave_configs}
        self.com_connected = False
        self.com_fail_count = 0

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    config = json.load(f)
                self.log_time = float(config.get("log_time", 2.0))
            except (json.JSONDecodeError, ValueError, OSError):
                # config.json can be caught mid-write by the GUI thread's
                # save_config() (checkbox toggles etc.) since that write
                # truncates the file before json.dump() finishes. Rather
                # than letting that transient empty/partial read kill this
                # polling thread, just keep the previously known log_time
                # and try again next loop.
                pass

    def reconnect_client(self):
        try:
            if hasattr(self, "client"):
                try:
                    self.client.close()
                except:
                    pass

            self.client = ModbusSerialClient(
                port=self.com,
                timeout=0.2,
                baudrate=int(self.baud),
                bytesize=self.databits,
                parity=self.parity,
                stopbits=self.stopbits,
            )

            if self.client.connect():
                if not self.com_connected:
                    self.comm_status_signal.emit("connected")

                self.com_connected = True
                self.com_fail_count = 0
                return True

        except Exception as e:
            pass

        self.com_connected = False
        self.comm_status_signal.emit("reconnecting")
        return False

    def run(self):
        """Thin crash-safe wrapper. A QThread's unhandled exception does
        NOT crash the app -- it just silently kills this thread, so
        polling/logging stops with no visible error at all (this is what
        caused the "logging just stops after N readings" bug). Catch
        anything that escapes the real loop and tell the GUI about it via
        crashed_signal instead of failing invisibly."""
        try:
            self._run_loop()
        except Exception as e:
            self.comm_status_signal.emit("lost")
            self.crashed_signal.emit(str(e))
        finally:
            try:
                if self.client:
                    self.client.close()
            except Exception:
                pass

    def _run_loop(self):
        self.client = None
        self.reconnect_client()

        while self.running:
            if not self.com_connected:
                self.reconnect_client()

                self.msleep(1000)
                continue

            if not self.client or not self.client.is_socket_open():
                if self.com_connected:
                    self.comm_status_signal.emit("lost")
                self.com_connected = False
                self.reconnect_client()
                self.msleep(1000)
                continue
            self.load_config()

            for sc in self.slave_configs:
                if not self.running:
                    break

                slave_num = sc["num"]
                slave_id = sc["slave_id"]
                address = sc["address"]

                rr = None
                for reg_count in [24, 16, 8, 4, 2, 1]:
                    try:
                        test_rr = self.client.read_holding_registers(
                            address=int(address), count=reg_count, device_id=slave_id
                        )

                        if test_rr and not test_rr.isError() and test_rr.registers:
                            rr = test_rr
                            self.com_fail_count = 0
                            if not self.com_connected:
                                self.comm_status_signal.emit("connected")
                            self.com_connected = True
                            break

                    except Exception as e:
                        self.com_fail_count += 1
                        try:
                            self.client.close()
                        except:
                            pass
                        time.sleep(0.05)
                        try:
                            self.client.connect()
                        except:
                            pass
                        if self.com_fail_count >= 10:
                            self.com_connected = False
                            self.comm_status_signal.emit("lost")
                        pass

                if rr and not rr.isError() and rr.registers:
                    regs = list(rr.registers)
                    regs += [0] * (24 - len(regs))

                    if self.fail_counts[slave_num] >= self.FAIL_THRESHOLD:
                        self.error_signal.emit(slave_num, "")

                    self.fail_counts[slave_num] = 0
                    self.update_signal.emit(slave_num, regs)

                else:
                    self.fail_counts[slave_num] += 1
                    try:
                        self.client.close()
                    except:
                        pass
                    time.sleep(0.05)
                    try:
                        self.client.connect()
                    except:
                        pass
                    self.update_signal.emit(slave_num, None)
                    if self.fail_counts[slave_num] == self.FAIL_THRESHOLD:
                        self.error_signal.emit(
                            slave_num, f"Slave ID-{slave_num}: No response"
                        )

                # Small gap between slaves to avoid bus collision
                # 20ms is enough for RS-485 turnaround at any baud rate
                self.msleep(50)

            # No sleep at end of loop — go straight back to polling
            # LCD update rate = (read_time + 20ms) × num_slaves ≈ nearly live

    def stop(self):
        self.running = False
        self.wait()

# ------------ CSV Writer ---------------
class csvWriter(QObject):
    update_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.state = False
        self.file_path = None  # path set externally by MainWindow

    def write(self, data):
        if not self.file_path:
            return
        with open(self.file_path, "a", newline="") as f:
            csv.writer(f).writerow(data)
        self.update_signal.emit(data)

    def start(self, file_path):
        self.file_path = file_path
        self.state = True
        if not os.path.exists(self.file_path):
            open(self.file_path, "w").close()

    def stop(self):
        self.state = False
        self.file_path = None


# ------- Main execution ----------
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.center()
    sys.exit(app.exec_())


# Sigma Controls , Odhav , Ahmedabad
# IN - 000 HT
# Graph Report 00 - 00 - 0000x