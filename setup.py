"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['flukeapp.py']
DATA_FILES = [
 './resources/Fluke-Flac.icns']
OPTIONS = {'argv_emulation': True,
 'iconfile': './resources/Fluke.icns',
 'plist': {'CFBundleDocumentTypes': [{'CFBundleTypeExtensions': ['flac'],
                                      'CFBundleTypeIconFile': 'Fluke-Flac.icns',
                                      'CFBundleTypeMIMETypes': ['audio/flac',
                                                                'audio/x-flac'],
                                      'CFBundleTypeName': 'FLAC Audio File',
                                      'CFBundleTypeOSTypes': ['flac'],
                                      'CFBundleTypeRole': 'Editor'}],
           'CFBundleIconFile': 'Fluke.icns',
           'CFBundleIdentifier': 'com.kichenko.fluke',
           'CFBundleInfoDictionaryVersion': '6.0',
           'CFBundleName': 'Fluke',
           'CFBundlePackageType': 'APPL',
           'CFBundleShortVersionString': '0.2.4',
           'IsDroppable': True,
           'NSHumanReadableCopyright': '(C)2009 Dmitry Kichenko. Distributed under GPLv3'}}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
