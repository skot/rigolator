from setuptools import setup

APP = ['pyscoper.py']
DATA_FILES = [] 
OPTIONS = {
    'argv_emulation': False,  # Changed from True to False
    'packages': ['PIL', 'tkinter'],
    'excludes': ['setuptools', 'pkg_resources', 'packaging'],
    'site_packages': True,
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
    setup_requires=['py2app'],
)