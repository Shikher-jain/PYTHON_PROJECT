# import os
# import time
# from plyer import notification

# if __name__=="__main__":
# # while True:
# # time.sleep(10)
#     notification.notify(title="water",message="take a sip of water",timeout=3)
#     time.sleep(10)

import time
from plyer import notification

def send_notification():
    notification.notify(
        title="Reminder To Take A Break",
        message="Have a sip of water",
        timeout=15
    )

if __name__ == "__main__":
    interval = 10  # Time interval between notifications in seconds
    while True:
        send_notification()
        time.sleep(interval)
