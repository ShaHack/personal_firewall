import json
import os
import ipaddress
import datetime

RULES_FILE = "rules.json"
LOG_FILE = "logs.txt"


def initialize():
    if not os.path.exists(RULES_FILE):
        with open(RULES_FILE, "w") as f:
            json.dump({"blocked_ips": []}, f, indent=4)


def load_rules():
    with open(RULES_FILE, "r") as f:
        return json.load(f)


def save_rules(data):
    with open(RULES_FILE, "w") as f:
        json.dump(data, f, indent=4)


def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.datetime.now()}] {message}\n")


def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def block_ip():
    data = load_rules()

    ip = input("Enter IP Address: ")

    if not valid_ip(ip):
        print("Invalid IP Address.")
        write_log(f"Invalid IP entered: {ip}")
        return

    if ip in data["blocked_ips"]:
        print("IP is already blocked.")
        return

    data["blocked_ips"].append(ip)
    save_rules(data)

    write_log(f"Blocked IP: {ip}")
    print("IP blocked successfully.")


def block_ip_gui(ip):
    data = load_rules()

    if not valid_ip(ip):
        return

    if ip in data["blocked_ips"]:
        return

    data["blocked_ips"].append(ip)
    save_rules(data)

    write_log(f"Blocked IP: {ip}")

def unblock_ip():
    data = load_rules()

    ip = input("Enter IP Address: ")

    if ip in data["blocked_ips"]:
        data["blocked_ips"].remove(ip)
        save_rules(data)
        write_log(f"Unblocked IP: {ip}")
        print("IP unblocked successfully.")
    else:
        print("IP not found.")


def view_ips():
    data = load_rules()

    print("\nBlocked IP Addresses")
    print("----------------------")

    if len(data["blocked_ips"]) == 0:
        print("No blocked IPs.")
    else:
        for ip in data["blocked_ips"]:
            print(ip)


def view_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return

    with open(LOG_FILE, "r") as log:
        print("\n===== LOGS =====")
        print(log.read())


initialize()

while True:
    def main():
        initialize()

    while True:

        print("\n==============================")
        print("     PERSONAL FIREWALL")
        print("==============================")
        print("1. Block IP")
        print("2. Unblock IP")
        print("3. View Blocked IPs")
        print("4. View Logs")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            block_ip()

        elif choice == "2":
            unblock_ip()

        elif choice == "3":
            view_ips()

        elif choice == "4":
            view_logs()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()