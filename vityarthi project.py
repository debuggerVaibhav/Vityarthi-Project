import datetime

# A list of dictionaries to store our expenses: [{'desc': 'Grocery', 'amount': 50.50}]
expenses = []

def add_expense(description: str, amount: float):
    """Adds a new expense entry to the list."""
    try:
        # Ensure the amount is a positive number
        if amount <= 0:
            print("❌ Amount must be positive.")
            return

        expense_record = {
            'date': datetime.date.today().strftime("%Y-%m-%d"),
            'description': description,
            'amount': amount
        }
        expenses.append(expense_record)
        print(f"✅ Added: {description} (${amount:.2f})")
    except ValueError:
        print("❌ Invalid amount provided.")

def view_expenses():
    """Prints all recorded expenses."""
    if not expenses:
        print("\n💰 No expenses recorded yet.")
        return

    print("\n--- Expense Report ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. [{exp['date']}] {exp['description']:<20} | ${exp['amount']:>8.2f}")
    print("----------------------")

def calculate_total():
    """Calculates and prints the total sum of all expenses."""
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n💵 Total Expenses: ${total:.2f}")
    return total

# --- Main Application Loop ---

if __name__ == "__main__":
    print("Welcome to the Console Expense Tracker!")

    # Example expenses to start with (optional)
    add_expense("Coffee", 4.50)
    add_expense("Lunch with client", 25.00)

    # Simple interactive menu
    while True:
        print("\nActions: (1) Add, (2) View, (3) Total, (4) Exit")
        choice = input("Enter action number: ").strip()

        if choice == '1':
            desc = input("Enter description: ").strip()
            # Basic validation to prevent empty description
            if not desc:
                print("Description cannot be empty.")
                continue

            try:
                amt = float(input("Enter amount ($): "))
                add_expense(desc, amt)
            except ValueError:
                print("Invalid input. Please enter a number for the amount.")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            calculate_total()

        elif choice == '4':
            print("Goodbye! Thank you for tracking your spending.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")