import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ["add.png", "delete.png","documento.db","update.png","log.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Registro Documental",
    version="1.0",
    description="Aplicativo de registro de documento",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="tela.py", base=base, icon="PRODOC.png")]
)
