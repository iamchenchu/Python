
def main():
    name = input("Please enter your name: ")
    income = int(input("Please enter your salary: "))

    expenses = ["rent", "food", "utilities", "transport", "clothing", "other", "enternainment"]
    total_expenses = 0

    for expense in expenses:
        total_expenses += int(input(f"Please enter your {expense} expenses: "))

    savings = income - total_expenses
    savings_percent = (savings / income) * 100

    print(f"Hello {name}, your savings are {savings} and your savings percent is {savings_percent}%")

if __name__ == "__main__":
    main()
