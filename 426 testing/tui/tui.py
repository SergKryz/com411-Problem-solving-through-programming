def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    welcome = "Welcome to Solar Record managment system !!!"  # Welcoming message

    print((len(welcome) // 2 * "-" )+ welcome + (len(welcome) // 2 * "-"))  # printing 'welcome' message


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # TODO: Your code here
   
    print("Choose from main menu:\n1.Load Data\n2.Process Data\n3.Visualise Data\n4.Save Data\n0.Exit")
    while True:
      operation = int(input())

    
      if operation == 1:
        return operation
      elif operation == 2:
        return operation
      elif operation == 3:
        return operation
      elif operation == 4:
        return operation
      elif operation == 0:
        return operation
      return f"{operation} is invalid option!"

      

def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here
    ops=menu()
    
    if ops==1:
      operation="Loading data"
    elif ops==2:
      operation="Processing data"
    elif ops==3:
      operation="Visualization"
    elif ops==4:
      operation="Saving data"
    elif ops==0:
      operation="Exiting"
  
    print(f"{operation} has started.")
    return ops
    

def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here
    ops=started()

    if ops== 1:
        operation = "Loading data"
    elif ops == 2:
        operation = "Processing data"
    elif ops == 3:
        operation = "Visualization"
    elif ops == 4:
        operation = "Saving data" 
    elif ops == 0:
        operation = "Exiting"

    print(f"{operation} has completed.")

