import time
import requests
from datetime import datetime

URL = "https://codeforces.com/api/problemset.problems"
CHECK_INTERVAL = 30

last_status = None

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
})


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_up():
    try:
        response = session.get(URL, timeout=15)

        print(f"[DEBUG] Status Code: {response.status_code}")

        if response.status_code == 200 and response.json()["status"] == "OK":
            return True

        return False

    except Exception as e:
        print(f"[DEBUG] Error: {e}")
        return False


def log(msg):
    print(f"[{now()}] {msg}")


log("Monitor Started")

while True:

    current_status = is_up()

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