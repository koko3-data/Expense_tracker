from functions import add_expense, view_expense, calculate_total, find_highest_lowest,user_input


while True:
    welcome_quest = user_input()
    if not welcome_quest:
        break
    else:
        expense_list = add_expense(welcome_quest)
        view_expense(expense_list)
        calculate_total()
        find_highest_lowest()
