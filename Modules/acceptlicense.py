import os
import sys
from datetime import datetime

LICENSE_FILE = ".license"
LICENSE_PATH = "LICENSE"

def license_text():
    with open(LICENSE_PATH, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content:
            return content

def accept_license():
    if os.path.exists(LICENSE_FILE):
        return

    print(license_text())

    response = input("\nAcceptez-vous les termes de la licence ? (yes/no): ").strip().lower()
    if response == "yes":
        with open(LICENSE_FILE, "w", encoding="utf-8") as f:
            f.write(f"MIT license :\nAccepted on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return True
    elif response == "no":
        return False
        sys.exit(1)
    else:
        return True