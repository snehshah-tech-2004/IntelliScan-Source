# Sigma Controls - IntelliScan

Windows desktop software (PyQt5) for multi-channel temperature scanning and PID controller monitoring.

## Features
- Modbus polling for up to 16 PID slaves
- Live combined graphing, CSV logging, PDF reports
- Registry-based license activation
- Auto-updater

## Run
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python main_3.py

## Build
PyInstaller specs are included (`*.spec`). Installer script: Inno Setup.

## License
Proprietary - see LICENSE.