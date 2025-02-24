#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt update && sudo apt install -y python3 python3-venv python3-pip
fi

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

python3 -m ensurepip
python3 -m pip install --upgrade pip
pip install -r requirements.txt

venv/bin/python3 -m PyInstaller --onefile --name BaseXSetup setup.py --clean
venv/bin/python3 -m PyInstaller --onefile --name BaseX main.py --clean

echo "✔ Compilation successful! There are 2 files in the dist folder: BaseXSetup and BaseX."
echo "- First, run Setup and enter your Telegram information."
echo "- Then execute BaseX once to create a Telegram link to your account, allowing you to send messages from your computer."
