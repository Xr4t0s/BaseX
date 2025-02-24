@echo off
setlocal

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installation in progress...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python-installer.exe'}" >nul 2>&1
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 >nul 2>&1
    del python-installer.exe >nul 2>&1
    echo Python installed successfully. Please restart your terminal and run this script again.
    exit /b
)

powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force" >nul 2>&1

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv >nul 2>&1
)

call venv\Scripts\activate.bat >nul 2>&1

python -m ensurepip >nul 2>&1
python -m pip install --upgrade pip >nul 2>&1

if exist requirements.txt (
    pip install -r requirements.txt >nul 2>&1
)

echo Compiling BaseXSetup...
venv\Scripts\python.exe -m PyInstaller --onefile --noconfirm --name BaseXSetup.exe setup.py --clean >nul 2>&1

echo Compiling BaseX...
venv\Scripts\python.exe -m PyInstaller --onefile --noconfirm --name BaseX.exe main.py --clean >nul 2>&1

echo.
echo Compilation successful! The following files were created in the "dist" folder:
echo - BaseXSetup.exe (Run this first and enter your Telegram information).
echo - BaseX.exe (Run this to create the Telegram link to your account).
echo.
exit /b
