#!/bin/bash

if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "Python n'est pas installé. Tentative d'installation automatique..."

    if command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv

    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-pip

    elif command -v pacman &> /dev/null; then
        sudo pacman -Sy --noconfirm python python-pip

    elif command -v apk &> /dev/null; then
        sudo apk add --no-cache python3 py3-pip

    elif command -v brew &> /dev/null; then
        brew install python

    else
        echo "Erreur : Impossible d'installer Python automatiquement." >&2
        echo "Veuillez installer Python manuellement depuis https://www.python.org/downloads/" >&2
        exit 1
    fi
fi

if command -v python3 &> /dev/null; then
    PYTHON="python3"
else
    PYTHON="python"
fi

$PYTHON -m pip install --upgrade pip --break-system-packages 2>/dev/null || $PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt --break-system-packages 2>/dev/null || $PYTHON -m pip install -r requirements.txt

$PYTHON script.py