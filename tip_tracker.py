import json
from datetime import datetime, timedelta

# Constants
FILEPATH = "tips.json"
WAITERS_FILE = "waiters.json"

# Load waiters
try:
    with open(WAITERS_FILE, "r") as f:
        waiters = json.load(f)
except FileNotFoundError:
    waiters = ["sbonelo", "siya", "naledi"]

# Save waiters

def save_waiters():
    with open(WAITERS_FILE, "w") as f:
        json.dump(waiters, f, indent=4)

# Get tip input
def get_tip(waiter):
    try:
        tip = float(input(f"\nEnter {waiter}'s daily tip: R"))
        return round(tip, 2)
    except ValueError:
        print("Invalid tip amount. Please enter a valid number.")
        return None

# Save tips to a JSON file
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

# View tips in a formatted manner
def view_tips():
    try:
        with open(FILEPATH, "r") as f:
            data = json.load(f)

        print("\n--- Tips Report ---")
        for entry in data:
            print(f"Waiter: {entry['waiter']}, Tip: R{entry['tip']:.2f}, Date: {entry['date']}")
    except FileNotFoundError:
        print("\nNo tips recorded yet.")

# Add or delete waiters
def manage_waiters():
    print("\n1. Add waiter\n2. Delete waiter")
    action = input("Choose an action: ")

    if action == "1":
        new_waiter = input("Enter the name of the new waiter: ").strip().title()
        if new_waiter and new_waiter not in waiters:
            waiters.append(new_waiter)
            save_waiters()
            print(f"\nWaiter {new_waiter} added successfully!")
        else:
            print("\nWaiter already exists or invalid name.")
    elif action == "2":
        del_waiter = input("Enter the name of the waiter to delete: ").strip().title()
        if del_waiter in waiters:
            waiters.remove(del_waiter)
            save_waiters()
            print(f"\nWaiter {del_waiter} deleted successfully!")
        else:
            print("\nWaiter not found.")
    else:
        print("\nInvalid action.")

# Weekly summary
def weekly_summary():
    try:
        with open(FILEPATH, "r") as f:
            data = json.load(f)

        summary = {}
        current_date = datetime.now()
        week_start = current_date - timedelta(days=current_date.weekday())  # Monday of the current week
        week_end = week_start + timedelta(days=6)  # Sunday of the current week

        for entry in data:
            entry_date = datetime.strptime(entry['date'], "%Y-%m-%d %H:%M:%S")
            if week_start <= entry_date <= week_end:
                waiter = entry['waiter']
                tip = entry['tip']
                summary[waiter] = summary.get(waiter, 0) + tip

        print("\n--- Weekly Summary ---")
        for waiter, total in summary.items():
            print(f"Waiter: {waiter}, Total Tips: R{total:.2f}")

        if current_date.weekday() != 6:
            print("\nNote: The week is not yet complete. This summary includes tips up to today.")
    except FileNotFoundError:
        print("\nNo tips recorded yet.")

# Main menu
def main():
    while True:
        print("\n1. Add tip\n2. View tips\n3. Weekly summary\n4. Manage waiters\n5. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            waiter = input("Enter waiter name: ").strip()
            if waiter in waiters:
                tip = get_tip(waiter)
                if tip is not None:
                    save_tips(waiter, tip)
            else:
                print("\nWaiter not found.")

        elif choice == "2":
            view_tips()

        elif choice == "3":
            weekly_summary()

        elif choice == "4":
            manage_waiters()

        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
