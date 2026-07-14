import datetime

def write_log(message):
    now = datetime.datetime.now()
    with open("logs.txt", "a") as log:
        log.write(f"[{now}] {message}\n")