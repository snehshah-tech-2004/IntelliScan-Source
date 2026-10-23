# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['fingerprint.py'],
    pathex=[],
    binaries=[],
    datas=[('SIGMA_ICON.svg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'pyqtgraph', 'pymodbus', 'mplcursors', 'scipy', 'sklearn', 'tensorflow', 'torch', 'torchvision', 'torchaudio', 'jupyter', 'jupyterlab', 'PyQt6'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Sigma Controls License Installer',
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
    uac_admin=True,
    icon=['SIGMA_ICON.ico'],
)
