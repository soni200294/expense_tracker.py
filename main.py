import json
import os
from datetime import date

FILE = "expenses.json"


def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    title = input("What did you spend on? ")
    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    category = input("Category (food/travel/shopping/other): ").lower()

    expenses.append({
        "title": title,
        "amount": amount,
        "category": category,
        "date": str(date.today())
    })
    save_expenses(expenses)
    print("Expense added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']} | {e['title']} | ₹{e['amount']} | {e['category']}")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        num = int(input("Enter the number to delete: "))
        removed = expenses.pop(num - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid number.")


def show_summary(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: ₹{total}")
    by_category = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    for cat, amt in by_category.items():
        print(f"  {cat}: ₹{amt}")


def main():
    expenses = load_expenses()
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Summary")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
