import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"


def add_expense():
    category = input("Category (food, travel, shopping, etc.): ").strip().lower()
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    note = input("Note (optional): ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date.today(), category, amount, note])
    print("Expense saved.")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses yet.")
        return
    print("\nDate | Category | Amount | Note")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} | {row[1]} | Rs.{row[2]} | {row[3]}")


def show_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses yet.")
        return
    totals = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            totals[category] = totals.get(category, 0) + amount

    print("\nSpending by category:")
    for category, total in totals.items():
        print(f"{category}: Rs.{total:.2f}")
    print(f"Total spent: Rs.{sum(totals.values()):.2f}")


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Show summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()
