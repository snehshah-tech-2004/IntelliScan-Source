import subprocess
import hashlib
import winreg

REG_PATH = r"SOFTWARE\Sigma_Controls_IntelliScan\Fingerprint"
VALUE_NAME = "Sigma_Controls_IntelliScan_License_Key"

# ruff: noqa: E402,F403,F405,F541,E722,F841


def get_motherboard_uuid():
    try:
        result = subprocess.check_output(
            "wmic csproduct get uuid", shell=True, timeout=5
        ).decode(errors="ignore")

        lines = [x.strip() for x in result.splitlines() if x.strip()]
        return lines[1]

    except:
        return ""


def get_disk_serial():
    try:
        result = subprocess.check_output(
            "wmic diskdrive get serialnumber", shell=True, timeout=5
        ).decode(errors="ignore")

        lines = [x.strip() for x in result.splitlines() if x.strip()]
        return lines[1]

    except:
        return ""


def get_machine_hash():
    uuid = get_motherboard_uuid()
    disk = get_disk_serial()

    if not uuid or not disk:
        return None

    raw = f"{uuid}|{disk}"

    return hashlib.sha256(raw.encode()).hexdigest()


def read_registry():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            REG_PATH,
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_64KEY,
        )

        value, _ = winreg.QueryValueEx(key, VALUE_NAME)

        winreg.CloseKey(key)

        return value

    except:
        return None


def validate_machine():
    registry_hash = read_registry()

    if registry_hash is None:
        return False

    current_hash = get_machine_hash()

    if current_hash is None:
        return False

    return current_hash == registry_hash
