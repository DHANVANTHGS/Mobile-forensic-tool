import os
import platform
import subprocess
import sys
import urllib.request
import zipfile
import shutil

def check():
    def is_adb_installed():
        try:
            subprocess.run(['adb', 'version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except FileNotFoundError:
            return False

    def install_adb_linux():
        try:
            subprocess.check_call(['sudo', 'apt', 'update'])
            subprocess.check_call(['sudo', 'apt', 'install', '-y', 'adb'])
        except Exception as e:
            print(f"ADB installation failed on Linux: {e}")
            sys.exit(1)

    def install_adb_mac():
        try:
            subprocess.check_call(['brew', 'install', 'android-platform-tools'])
        except Exception as e:
            print("Homebrew is not installed or adb failed to install.")
            print("Please install Homebrew from https://brew.sh/ and rerun this script.")
            sys.exit(1)

    def install_adb_windows():
        url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
        zip_path = 'platform-tools.zip'
        extract_path = os.path.join(os.getcwd(), 'platform-tools')

        print("[*] Downloading ADB platform-tools for Windows...")
        urllib.request.urlretrieve(url, zip_path)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall()

        os.remove(zip_path)

        adb_path = os.path.join(extract_path)
        os.environ["PATH"] += os.pathsep + adb_path

        # Optional: Permanently add to PATH
        print(f"[*] ADB extracted to: {adb_path}")
        print("[*] Please add the above directory to your system PATH manually for global access.")
        print("[*] Or you can run using full path:", os.path.join(adb_path, 'adb.exe'))

    def install_adb():
        if is_adb_installed():
            print("[+] ADB is already installed.")
            return

        os_type = platform.system()

        if os_type == 'Linux':
            print("[*] Detected Linux. Installing ADB via apt...")
            install_adb_linux()

        elif os_type == 'Darwin':
            print("[*] Detected macOS. Installing ADB via Homebrew...")
            install_adb_mac()

        elif os_type == 'Windows':
            print("[*] Detected Windows. Downloading platform-tools...")
            install_adb_windows()

        else:
            print(f"Unsupported OS: {os_type}")
            sys.exit(1)

        if is_adb_installed():
            print("[+] ADB installed successfully.")
        else:
            print("[-] ADB installation failed. Please install it manually.")

    
    install_adb()

check()