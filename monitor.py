import time
import requests
from plyer import notification

URL = "https://codeforces.com"
CHECK_INTERVAL = 30

was_up = None

def is_codeforces_up():
    try:
        response = requests.get(URL, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

print("Codeforces Monitor Started...")

while True:
    up = is_codeforces_up()

    if was_up is None:
        was_up = up

    elif up != was_up:
        if up:
            notify("Codeforces is BACK!", "The server is running again.")
            print("Codeforces is BACK!")
        else:
            notify("Codeforces is DOWN!", "The server is not reachable.")
            print("Codeforces is DOWN!")

        was_up = up

    time.sleep(CHECK_INTERVAL)