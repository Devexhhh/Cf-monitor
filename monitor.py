import time
import requests
from datetime import datetime

URL = "https://codeforces.com"
CHECK_INTERVAL = 30

last_status = None

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}


def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_codeforces_up():
    try:
        response = requests.get(
            URL,
            headers=headers,
            timeout=10,
            allow_redirects=True
        )

        print(f"[DEBUG] Status Code: {response.status_code}")

        return response.status_code == 200

    except requests.RequestException as e:
        print(f"[DEBUG] Exception: {e}")
        return False


def log(msg):
    print(f"[{get_time()}] {msg}")


log("Monitor Started")

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
            log("STATUS CHANGE: Codeforces is BACK UP")
        else:
            log("STATUS CHANGE: Codeforces is DOWN")

        last_status = current_status

    time.sleep(CHECK_INTERVAL)