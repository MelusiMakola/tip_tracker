import json
from datetime import datetime, timedelta

FILEPATH = "../data/tips.json"

# Save tips to JSON
def save_tips(waiter, tip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"waiter": waiter, "tip": tip, "date": timestamp}

    try:
        with open(FILEPATH, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(FILEPATH, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nTip saved successfully for {waiter}!")

# View recorded tips
def view_tips():
    try:
        with open(FILEPATH, "r") as f:
            data = json.load(f)

        if not data:
            print("\nNo tips recorded yet.")
            return

        print("\n--- Tips Report ---")
        for entry in data:
            print(f"Waiter: {entry['waiter']}, Tip: R{entry['tip']:.2f}, Date: {entry['date']}")

    except FileNotFoundError:
        print("\nNo tips recorded yet.")

# Generate weekly summary
def weekly_summary():
    try:
        with open(FILEPATH, "r") as f:
            data = json.load(f)

        summary = {}
        current_date = datetime.now()
        week_start = current_date - timedelta(days=current_date.weekday())  # Monday of current week
        week_end = week_start + timedelta(days=6)  # Sunday of current week

        for entry in data:
            entry_date = datetime.strptime(entry['date'], "%Y-%m-%d %H:%M:%S")
            if week_start <= entry_date <= week_end:
                waiter = entry['waiter']
                tip = entry['tip']
                summary[waiter] = summary.get(waiter, 0) + tip

        if not summary:
            print("\nNo tips recorded this week.")
            return

        print("\n--- Weekly Summary ---")
        for waiter, total in summary.items():
            print(f"Waiter: {waiter}, Total Tips: R{total:.2f}")

    except FileNotFoundError:
        print("\nNo tips recorded yet.")
