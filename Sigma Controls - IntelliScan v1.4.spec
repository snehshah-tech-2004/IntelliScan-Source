# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('SIGMA_ICON.svg', '.'), ('SIGMA_cache.png', '.'), ('license_check.py', '.'), ('updater.py', '.'), ('id_sett.py', '.'), ('login.py', '.'), ('ui_2.py', '.'), ('ico_rc.py', '.'), ('db_manager.py', '.')]
binaries = []
hiddenimports = ['license_check', 'updater', 'id_sett', 'db_manager', 'login', 'ui_2', 'pyqtgraph', 'matplotlib', 'pymodbus', 'mplcursors', 'getmac']
tmp_ret = collect_all('matplotlib')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('pyqtgraph')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main_3.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['keras', 'tensorflow', 'torch', 'torchvision', 'torchaudio', 'sklearn', 'PyQt6', 'jupyter', 'jupyterlab', 'astropy', 'altair', 'docker', 'gTTS', 'pytesseract', 'ultralytics', 'twilio'],
    noarchive=False,
    optimize=2,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('O', None, 'OPTION'), ('O', None, 'OPTION')],
    name='Sigma Controls - IntelliScan v1.4',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['SIGMA_ICON.ico'],
)
