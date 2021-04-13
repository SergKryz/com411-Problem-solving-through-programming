def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    welcome = "Welcome to Solar Record managment system !!!" 

    print(len(welcome)//2* "-"  + welcome + len(welcome)//2* "-") # printing 'welcome' message
