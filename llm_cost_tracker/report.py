import json
from datetime import datetime
import csv

def export_to_csv():
    try:
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No usage data found.")
        return

    with open("usage_report.csv", "w", newline="") as csvfile:
        fieldnames = ["timestamp", "tokens", "cost"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

    print("✅ Data exported to usage_report.csv")

LOG_FILE = "usage_log.json"

def generate_report():
    """
    Generate usage report from log file.
    """

    try:
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No usage data found.")
        return

    total_tokens = 0
    total_cost = 0

    for entry in data:
        total_tokens += entry["tokens"]
        total_cost += entry["cost"]

    print("----- LLM Usage Report -----")
    print(f"Total Requests: {len(data)}")
    print(f"Total Tokens Used: {total_tokens}")
    print(f"Total Cost: ${total_cost:.6f}")
    from datetime import datetime

def generate_today_report():
    try:
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No usage data found.")
        return

    today = datetime.now().date()

    total_tokens = 0
    total_cost = 0
    count = 0

    for entry in data:
        entry_date = datetime.fromisoformat(entry["timestamp"]).date()

        if entry_date == today:
            total_tokens += entry["tokens"]
            total_cost += entry["cost"]
            count += 1

    print("----- Today's Usage -----")
    print(f"Requests Today: {count}")
    print(f"Tokens Today: {total_tokens}")
    print(f"Cost Today: ${total_cost:.6f}")