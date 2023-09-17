# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(
    ['tkinter16.py'],
    pathex=[],
    binaries=[],
    datas=[('game_music_start.ogg', '.'), ('game_music_mid_forever.mp3', '.'), ('game_music_last.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='tkinter16',
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
    bundle_identifier='lele.tkinter16.app'
)

app = BUNDLE(exe,
             name='tkinter16.app',
             icon=None,
             bundle_identifier='lele.tkinter16.app')
