import sys
from cx_Freeze import setup, Executable
from PyQt4 import QtGui, QtCore

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
includes = ["atexit"] 
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Mini Tor Browser",
        version = "0.1",
        description = "A minimalist web browser that connects through TOR",
        options = {"build_exe": {"includes": includes}},
        executables = [Executable("webBrowser.py", base=base)])
