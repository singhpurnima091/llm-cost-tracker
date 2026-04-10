import json
from datetime import datetime

LOG_FILE = "usage_log.json"

def log_usage(tokens: int, cost: float):
    """
    Store token usage and cost into a JSON file.
    """

    entry = {
        "timestamp": datetime.now().isoformat(),
        "tokens": tokens,
        "cost": cost
    }

    try:
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as file:
        json.dump(data, file, indent=4)