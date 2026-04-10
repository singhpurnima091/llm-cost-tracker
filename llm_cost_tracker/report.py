import json

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