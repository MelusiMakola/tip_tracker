from tip_handler import save_tips, view_tips, weekly_summary
from waiter_handler import manage_waiters, load_waiters

# Get tip input
def get_tip(waiter):
    try:
        tip = float(input(f"\nEnter {waiter}'s daily tip: R"))
        return round(tip, 2)
    except ValueError:
        print("Invalid tip amount. Please enter a valid number.")
        return None

# Main menu
def main():
    waiters = load_waiters()
    
    while True:
        print("\n1. Add tip\n2. View tips\n3. Weekly summary\n4. Manage waiters\n5. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            waiter = input("Enter waiter name: ").strip().title()
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
