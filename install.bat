@echo off
setlocal

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installation in progress...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python-installer.exe'}"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python installed successfully. Please restart your terminal and run this script again.
    exit /b
)

powershell -Command "Set-ExecutionPolicy Unrestricted -Scope Process -Force"

set "PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python3*;%USERPROFILE%\AppData\Local\Programs\Python\Python3*\Scripts"

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

python -m ensurepip
python -m pip install --upgrade pip
pip install -r requirements.txt

venv\Scripts\python.exe -m PyInstaller --onefile --name BaseXSetup.exe setup.py --clean
venv\Scripts\python.exe -m PyInstaller --onefile --name BaseX.exe main.py --clean

echo Compilation successful! There are 2 files in the dist folder: BaseXSetup and BaseX.
echo - First, run Setup and enter your Telegram information.
echo - Then execute BaseX once to create a Telegram link to your account, allowing you to send messages from your computer.

exit /b
