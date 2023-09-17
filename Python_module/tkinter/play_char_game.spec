# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(
    ['play_char_game.py'],
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
    name='play_char_game',
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
    bundle_identifier='lele.play_char_game.app'
)

app = BUNDLE(exe,
             name='play_char_game.app',
             icon=None,
             bundle_identifier='lele.play_char_game.app')
