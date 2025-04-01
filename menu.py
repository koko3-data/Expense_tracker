# add_expense(expense_list): Adds an expense with description and amount.
#
# view_expenses(expense_list): Displays all recorded expenses.
#
# calculate_total(expense_list): Calculates and returns the total expenses.
#
# find_highest_lowest(expense_list): Finds and displays the highest and lowest expenses.


expenses= {}



def add_expense():
    entry_quest = input("Will you like to create an expense tracker (y/n): ")
    if entry_quest == "n":
       return []
    if entry_quest == "y":
        ask_user = input("Enter your expense list e.g Travelling,Clothing,Printing,Groceries : ").lower().split(",")
        expense_list= [item.strip() for item in ask_user]
        for  item in expense_list:
            try:
                cost = float(input(f"Enter cost of {item} : "))
                expenses[item] = cost
            except ValueError:
                print("Enter a valid number")
        print("Expenses successfully added")

def view_expense():
    if not expenses:
        print("No recorded expenses")
    else:
        print("View list of recorded expenses:\n ")
        for item ,cost in expenses.items():
            print('\033[1;31m' + f"{item.capitalize()} : {cost}"+ '\033[0m')
    # print(f"View List of recorded expenses:\n {expenses}")

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

def menu():
    while True:
        print("Expense Tracker Menu: ")
        print("1. Add Expense ")
        print("2. View Expense ")
        print("3. Expense Total ")
        print("4. Exit ")
        choice = input("Enter your choice : ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Thank you for your time. Goodbye")
            break
        else:
            print("enter a valid choice")





