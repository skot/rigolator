from setuptools import setup

APP = ['pyscoper.py']
DATA_FILES = [] 
OPTIONS = {
    'argv_emulation': False,
    'arch': 'arm64',
    'packages': ['PIL', 'tkinter'],
    'site_packages': False,
    'iconfile': 'rigolator_icon.png',
    'plist': {
        'CFBundleName': 'Rigolator',
        'CFBundleDisplayName': 'Rigolator',
        'CFBundleGetInfoString': "Rigol Oscilloscope Screenshot Tool",
        'CFBundleIdentifier': "com.yourname.rigolator",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHighResolutionCapable': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
)
