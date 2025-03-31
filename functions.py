# add_expense(expense_list): Adds an expense with description and amount.
#
# view_expenses(expense_list): Displays all recorded expenses.
#
# calculate_total(expense_list): Calculates and returns the total expenses.
#
# find_highest_lowest(expense_list): Finds and displays the highest and lowest expenses.


expenses= {}

def user_input():
    entry_quest = input("Will you like to create an expense tracker (y/n): ")
    if entry_quest == "n":
       return []
    if entry_quest == "y":
        ask_user = input("Enter your expense list e.g Travelling,Clothing,Printing,Groceries : ").lower().split(",")
        return ask_user

def add_expense(ask_user):
        expense_list= [item.strip() for item in ask_user]
        return expense_list

def view_expense(expense_list):
        for item in expense_list:
           cost = float(input(f"Enter cost of {item} : "))
           expenses[item] = cost

        for item, cost in expenses.items():
            print(f"{item.capitalize()} : {cost}")

def calculate_total():
        total_expense = 0
        for item, cost in expenses.items():
            total_expense += cost
        print('\033[1;31m' + f"Total Expense = {total_expense}" + '\033[0m')

def find_highest_lowest():
        if expenses:
            highest_expense = max(expenses.values())
            highest_desc = max(expenses, key=expenses.get)
            lowest_expense = min(expenses.values())
            lowest_desc = min(expenses, key=expenses.get)
            print('\033[1;31m' + f"Highest Expense = {highest_desc.capitalize()} - {highest_expense}"+ '\033[0m')
            print('\033[1;31m' + f"Lowest Expense = {lowest_desc.capitalize()} - {lowest_expense}"+ '\033[0m')


