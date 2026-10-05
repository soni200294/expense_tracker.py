import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file. Return an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    """Save the expenses list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    """Ask the user for expense details and add them."""
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    category = input("Enter category (Food, Travel, Bills, etc.): ").strip().title()
    description = input("Enter description: ").strip()

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category if category else "Other",
        "description": description,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    """Show all expenses in a table."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n{:<4} {:<12} {:<10} {:<12} {}".format(
        "No.", "Date", "Amount", "Category", "Description"))
    print("-" * 60)
    for i, e in enumerate(expenses, start=1):
        print("{:<4} {:<12} {:<10.2f} {:<12} {}".format(
            i, e["date"], e["amount"], e["category"], e["description"]))


def show_total(expenses):
    """Show total spending and a breakdown by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: {total:.2f}")

    by_category = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]

    print("\nSpending by category:")
    for category, amount in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:<12} {amount:.2f}")


def delete_expense(expenses):
    """Delete an expense by its number."""
    view_expenses(expenses)
    if not expenses:
        return
    try:
        number = int(input("\nEnter the expense number to delete: "))
    except ValueError:
        print("Invalid number.")
        return

    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['description']} ({removed['amount']:.2f})")
    else:
        print("Number out of range.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Show total and category summary")
        print("4. Delete an expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
