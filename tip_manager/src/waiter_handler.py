import json

WAITERS_FILE = "../data/waiters.json"

# Load waiters
def load_waiters():
    try:
        with open(WAITERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return ["Sbonelo", "Siya", "Naledi"]

# Save waiters
def save_waiters(waiters):
    with open(WAITERS_FILE, "w") as f:
        json.dump(waiters, f, indent=4)

# Add a new waiter
def add_waiter():
    waiters = load_waiters()
    new_waiter = input("Enter the name of the new waiter: ").strip().title()
    
    if not new_waiter or new_waiter in waiters:
        print("\nWaiter already exists or invalid name.")
        return

    waiters.append(new_waiter)
    save_waiters(waiters)
    print(f"\nWaiter {new_waiter} added successfully!")

# Delete a waiter
def delete_waiter():
    waiters = load_waiters()
    del_waiter = input("Enter the name of the waiter to delete: ").strip().title()
    
    if del_waiter not in waiters:
        print("\nWaiter not found.")
        return

    waiters.remove(del_waiter)
    save_waiters(waiters)
    print(f"\nWaiter {del_waiter} deleted successfully!")

# Manage waiters
def manage_waiters():
    print("\n1. Add waiter\n2. Delete waiter")
    action = input("Choose an action: ")

    if action == "1":
        add_waiter()
    elif action == "2":
        delete_waiter()
    else:
        print("\nInvalid action.")
