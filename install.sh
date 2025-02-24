#!/bin/bash

set -e

if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt update -qq > /dev/null 2>&1
    sudo apt install -y python3 python3-venv python3-pip > /dev/null 2>&1
fi

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv > /dev/null 2>&1
fi

source venv/bin/activate > /dev/null 2>&1

python3 -m ensurepip > /dev/null 2>&1
python3 -m pip install --upgrade pip > /dev/null 2>&1

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt > /dev/null 2>&1
fi

echo "Compiling BaseXSetup..."
venv/bin/python3 -m PyInstaller --onefile --noconfirm --name BaseXSetup setup.py --clean > /dev/null 2>&1

echo "Compiling BaseX..."
venv/bin/python3 -m PyInstaller --onefile --noconfirm --name BaseX main.py --clean > /dev/null 2>&1

echo ""
echo "✔ Compilation successful! The following files were created in the 'dist' folder:"
echo "- BaseXSetup (Run this first and enter your Telegram information)."
echo "- BaseX (Run this to create the Telegram link to your account)."
echo ""
