
expenses= {}
while True:
    entry_quest = input("Will you like to create an expense tracker (y/n): ")
    if entry_quest == "n":
        break
    else:
        ask_user = input("Enter your expense list e.g Travelling,Clothing,Printing,Groceries : ").lower().split(",")
        user_input = [item.strip() for item in ask_user]

        for item in user_input:
           cost = float(input(f"Enter cost of {item} : "))
           expenses[item] = cost

        for item, cost in expenses.items():
            print(f"{item.capitalize()} : {cost}")

        total_expense = 0
        for item, cost in expenses.items():
            total_expense += cost
        print(f"Total Expense = {total_expense}")
            # for index,item in enumerate (item_cost,start =1):
        #     print(f"{index} {item_cost}")

        if expenses:
            highest_expense = max(expenses.values())
            highest_desc = max(expenses.keys())
            lowest_expense = min(expenses.values())
            lowest_desc = min(expenses.keys())
            print(f"Highest Expense = {highest_desc.capitalize()} - {highest_expense}")
            print(f"Lowest Expense = {lowest_desc.capitalize()} - {lowest_expense}")


