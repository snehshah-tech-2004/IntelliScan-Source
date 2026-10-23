# Sigma Controls IntelliScan

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-41CD52)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6)
![Version](https://img.shields.io/badge/Version-1.4.0-00A0E3)
![License](https://img.shields.io/badge/License-Proprietary-red)

Windows desktop software for multi-channel temperature scanning and PID controller monitoring over Modbus RTU, built for industrial use by **Sigma Controls**.

> **Private repository.** Proprietary software. See [LICENSE](LICENSE).

## Screenshots

| Main screen | Live graph |
|---|---|
| <img src="Software%20Manual%20Docs/images/Main%20Screen.png" width="420"> | <img src="Software%20Manual%20Docs/images/Live%20Graph.png" width="420"> |
| **Live table** | **PDF report** |
| <img src="Software%20Manual%20Docs/images/Live%20Table.png" width="420"> | <img src="Software%20Manual%20Docs/images/PDF%20Graph.png" width="420"> |

## Features

- **Modbus RTU polling** over serial (RS-485) with multi-slave support (up to 16 PID slaves) and CH01-CH24 channel selection
- **Live monitoring:** real-time graph (pyqtgraph), live table, last-10 view, combined multi-slave graphing with PV/SV series
- **Data logging:** CSV files plus a SQLite database (`Scanner_DB`) with sensor and event logs
- **CSV replay** of past recordings
- **PDF reports:** graph and table reports with custom letterhead and header text
- **Login** with per-user credentials
- **License activation** tied to a machine fingerprint (Windows registry), with license-limited slave IDs
- **Auto-updater** that checks a hosted `latest.json` and downloads new releases
- **Built-in HTML user manual** (`Software Manual Docs/`)

## Tech stack

| Area | Library |
|---|---|
| GUI | PyQt5 |
| Plotting | pyqtgraph, matplotlib |
| Modbus | pymodbus 3.11, pyserial |
| Data | pandas, numpy, sqlite3 |
| Reports | fpdf (1.7.2), Pillow |
| Licensing | getmac, winreg |
| Updates | requests |
| Packaging | PyInstaller, Inno Setup |

## Project structure

~~~
main_3.py            Main application window and logic
ui_2.py              Generated UI layout (Qt Designer)
login.py             Login dialog
id_sett.py           Slave ID settings dialog
db_manager.py        SQLite logging (sensor and event logs)
fingerprint.py       Machine fingerprint and license activation
license_check.py     License validation helpers
updater.py           Standalone auto-updater
ico.qrc / ico_rc.py  Qt resources (icons)
icons/               UI icons
Software Manual Docs/  HTML user manual
docs/                Architecture diagram
*.spec               PyInstaller build specs
version.json         Current version metadata
config.example.json  Example runtime config
~~~

## Getting started

Requirements: Windows, Python 3.11.

~~~powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe main_3.py
~~~

Not included in the repo (kept out on purpose):

- `credentials.json`: login users. Copy it from a working install.
- `config.json`: created automatically on first run (see `config.example.json`).
- `Scanner_DB/` and `Scanner_Files/`: created at runtime.
- The license key generator (separate private tool).

## Build

~~~powershell
pip install pyinstaller
pyinstaller "Sigma Controls - IntelliScan v1.4.spec"
pyinstaller "Sigma Controls - IntelliScan Updater.spec"
pyinstaller "Sigma Controls License Installer.spec"
~~~

The installer is built with Inno Setup using `installer/Setup_IntelliScan.iss` (the paths inside point to the original build machine and need adjusting).

## Release and update flow

1. Update `version.json` and the version in the spec file.
2. Build with PyInstaller, then package the installer zip.
3. Commit, then tag: `git tag -a vX.Y -m "IntelliScan vX.Y"` and `git push origin vX.Y`.
4. Publish the zip as a GitHub Release and update `latest.json` in the public update repo `Sigma-Controls-IntelliScan` (served via GitHub Pages).

The updater reads `latest.json` from that public repo. **Do not rename or move it**, or installed apps stop updating.

## Notes

- Windows only (uses `winreg`).
- Keep `fpdf==1.7.2`. The PDF code uses the old `fpdf` API, not `fpdf2`.
- `pymodbus` calls use the `device_id=` keyword, which needs pymodbus 3.10 or newer.
- No secrets in git. Never commit `credentials.json`, `config.json` or the license generator.

## License

Copyright (c) 2026 Sigma Controls. All rights reserved. See [LICENSE](LICENSE).