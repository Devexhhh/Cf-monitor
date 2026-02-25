import time
import requests
from datetime import datetime

URL = "https://codeforces.com"
CHECK_INTERVAL = 30

last_status = None


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_codeforces_up():
    try:
        response = requests.get(URL, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def log(message):
    print(f"[{get_current_time()}] {message}")


log("Codeforces Monitor Started")

while True:
    current_status = is_codeforces_up()

    if current_status:
        log("CURRENT STATUS: UP")
    else:
        log("CURRENT STATUS: DOWN")

    if last_status is None:
        last_status = current_status

    elif current_status != last_status:
        if current_status:
            log("STATUS CHANGE DETECTED: Codeforces is BACK UP")
        else:
            log("STATUS CHANGE DETECTED: Codeforces is DOWN")

        last_status = current_status

    time.sleep(CHECK_INTERVAL)