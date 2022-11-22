#=====importing libraries===========
from datetime import date, timedelta

#======= Define Functions ========#

# create a dictionary of all users
def user_dict(filename):

    # create dictionary to store usernames and passwords
    user_dict = {}

    # open the user.txt file to retreive credentials
    with open(filename, 'r') as f:
        contents = f.readlines()

    # loop through all lines, tokenise the username and password
    for i in range(0, len(contents)):
        tokenised = contents[i].split()

        # strip the comma from username and store as key value pairs in dictionary
        user_dict[tokenised[0].strip(",")] = tokenised[1]

    # return the dictionary of users
    return user_dict



# create a dictionary of all the tasks in the task.txt file
def all_tasks(filename):
    
    # open tasks.txt text file and save each line as an element in the list 'tasks'
    with open(filename, 'r') as f:
        tasks = f.readlines()

    # 'task_list' will be a list of dictionaries 
    task_list = []

    # loop through each task in the list, creating a dictionary for each one -
    # append the created dictionary to 'task_list'
    for i in range(len(tasks)):
        tokenised = tasks[i].split(', ')

        # strip the newline character from the final word in each line
        tokenised[5] = tokenised[5].strip('\n')

        # create a dictionary for each task, each loop
        i = {}   

        i['Task'] = tokenised[1]
        i['Assigned To'] = tokenised[0]
        i['Date Assigned'] = tokenised[3]
        i['Due Date'] = tokenised[4]
        i['Task Complete'] = tokenised[5]
        i['Task Description'] = tokenised[2]

        # append the dictionary for each task to 'task__list'
        task_list.append(i)

    return task_list


# function to write a new user to the user.txt file from user input
def reg_user(user_dict):

    if username == 'admin':
    # get user input for new username
        new_user = input("\nEnter the new username: \n")

        # check username does not already exist
        if new_user in user_dict:
            print("\nThis username is already in use\n")
            
        # get user input for new password
        else:
            new_pass = input("\nEnter the new password: \n")

            # get user to enter password again and check they match
            new_pass_check = input("\nEnter the password again to check for match: \n")

            while new_pass != new_pass_check:
                print("\nThe passwords do not match. Try again: \n")

                new_pass_check = input("\nEnter the password again to check for match: \n")
                
            else:
                # append 'a' new user details to user.txt
                with open('user.txt', 'a') as f:
                    f.write('\n' + new_user + ', ' + new_pass)
                    pass
    else:
        print("\nYou have to have administrator privileges to add users.\n")

    return

# function to add a new task to tasks.txt from user iput
def add_task(user_dict):

    # get username to add as owner of the new task
    user = input("\nEnter the username associated with the task you wish to add: \n")

    # check user exists
    while user not in user_dict:
        print("\nThe user you entered does not exist!")

        user = input("\nEnter the username associated with the task you wish to add: \n")

    # get title
    title = input("\nEnter the title of the task you wish to add: \n")

    # get description
    description = input("\nEnter a description of the task: \n")

    # get the due date of the task
    num_days = input("\nEnter the number of days you have to complete the task: \n")

    # get the completion status of the task
    status = input("\nHas the task been completed? Enter 'yes' or 'no': \n")

    # validate input matches acceptable parameters
    if status.lower() == 'yes':
        pass
    elif status.lower() == 'no':
        pass
    else:
        print("Input error")

        # get task status to add to new task
        status = input("\nHas the task been completed? Enter 'yes' or 'no': \n")

    # get the current date
    today = date.today()
    today_date = today.strftime("%d %B %Y")
    print(today_date)

    # calculate the due date from the num days user input
    due_date = today + timedelta(days=int(num_days))
    # convert due_date to the correct format
    due_date = due_date.strftime("%d %B %Y")

    # write the new task to 'tasks.txt'
    with open('tasks.txt', 'a') as t:
        t.write('\n' + user + ', ' + title + ', ' + 
        description + ', ' + today_date + ', ' + due_date + ', ' + status)

    return


# function to view all tasks, taking the list of task dictionaries as a parameter
def view_all(task_list):

    # loop through each task dictionary in 'task_list'
    for i in range(len(task_list)):

        # create upper border
        print("\n", ("-" * 100))

        # present data in a readable format
        print(f"Assigned To:\t\t\t{task_list[i]['Assigned To']}\nDate Assigned:\t\t\t{task_list[i]['Date Assigned']}\nDue Date:\t\t\t{task_list[i]['Due Date']}\nTask Complete:\t\t\t{task_list[i]['Task Complete']}\nTask Description:\n  {task_list[i]['Task Description']}")

    # create lower border
    print("-" * 100, '\n')

    return 


# function to show tasks for a specific user. Takes username and the list of task dictionaries as input
def view_mine(user, task_list):

    # to count all tasks associated with current user
    count = 1

    # create a dictionary of indices that maps the index of each user task in the task_list with its sequential number in the dictionary
    indices = {}

    # loop over all tasks checking owner of task matches logged in user
    for i in range(len(task_list)):
        # if task owner matches current user -
        # - save the data as: {count: i} where i is the index of the task in 'task_list'
        if task_list[i]['Assigned To'] == user:
            indices[count] = i
            count += 1
        pass

    # ask user to select to view all tasks, or a specific task by the user input number  
    selection = int(input("Select specific tasks by number, or type '0' to view all. Type '-1' to return to menu: \n"))

    # if user enters -1, quit to main menu
    if selection == -1:
        return

    # show all tasks for the logged in user
    elif selection == 0:

        # print tasks in readable consistent format
        printAllTasks(task_list, indices)
        
    # validation check that user selection is not higher than the number of tasks
    elif selection > count:
        print("\nError. Selection not recognised.\n")

    # print the selected task in readable consistent format
    else:

        # print task in readable format
        printTask(task_list, indices, selection)

        # ask user if the task is complete
        complete = input("\nIs this task complete? Enter 'yes' or 'no': \n")

        # if task not completed, set 'Task Complete' to 'no'
        if complete.lower() == 'yes':
            task_list[indices[selection]]['Task Complete'] = complete

            # writ echanges to file
            writeChanges('test.txt', task_list)
        
        elif complete.lower() == 'no':

            # get input from user to edit task if desired
            edit = input("Would you like to edit the task? Type 'yes' or 'no': ")

            if edit == 'yes':
                field = input("\nWould you like to edit the user field or the due date field? Type 'user' or 'date': \n")

                if field.lower() != 'date' and field.lower() != 'user':
                    print("\nError. Input not recognised\n")

                    field = input("\nWould you like to edit the user field or the due date field? Type 'user' or 'date': \n")

                elif field == 'user':
                    new_user = input("\nEnter the new username: \n")

                    task_list[indices[selection]]['Assigned To'] = new_user                
                    
                elif field == 'date':
                    new_date = input("\nEnter the new due date: \n")
                    
                    # access the 'Due Date' value from the task at the user selected index 
                    task_list[indices[selection]]['Due Date'] = new_date

                # write changes to file
                writeChanges('test.txt', task_list)
        
            elif edit == 'no':
                print('\n\nOkay, exiting back to main menu.....\n')

            else:
                print("\nError. Input not recognised.\n\n")

            # write changes to file
            writeChanges('test.txt', task_list)

        else:
            print("\nError. Input not recognised.\n")

    return

# function to print task in readable format, takes list of task dictionaries, index dictionary and user selection (integer)
def printTask(task_list, indices, selection):
    
    # print out the task in readable form
    print(f"\nAssigned To:\t\t\t{task_list[indices[selection]]['Assigned To']}\nDate Assigned:\t\t\t{task_list[indices[selection]]['Date Assigned']}\nDue Date:\t\t\t{task_list[indices[selection]]['Due Date']}\nTask Complete:\t\t\t{task_list[indices[selection]]['Task Complete']}\nTask Description:\n  {task_list[indices[selection]]['Task Description']}\n")


# function to print all tasks for specific user
def printAllTasks(task_list, indices):
    # print tasks in readable consistent format
    for i in indices.values():
        print(f"\nAssigned To:\t\t\t{task_list[i]['Assigned To']}\nDate Assigned:\t\t\t{task_list[i]['Date Assigned']}\nDue Date:\t\t\t{task_list[i]['Due Date']}\nTask Complete:\t\t\t{task_list[i]['Task Complete']}\nTask Description:\n  {task_list[i]['Task Description']}\n")


# function to write changes to file
def writeChanges(filename, task_list):
    
    # write the amended task dictionaries to 'tasks.txt'
    # execute logic inside 'with' so as to be able to write each line without closing the file
    with open('test.txt', 'w') as f:
        # loop through each task dictionary in 'task_list'
        for i in task_list:
            # create list to append elements in the correct order before writing to 'tasks.txt'
            buffer = []
            buffer.append(i['Assigned To'])
            buffer.append(i['Task'])
            buffer.append(i['Task Description'])
            buffer.append(i['Date Assigned'])
            buffer.append(i['Due Date'])
            buffer.append(i['Task Complete'])
            
            # loop through the reorganised task, writing it to the tasks.txt file
            for j in buffer:
                f.write(j + ', ')
            
            # after the final element in the task, create a newline
            f.write('\n')


# function to generate reports. Takes in task list and user dictionary
def generateReports(task_list, users):
    
    # task_overview.txt:
        # get total number of tasks
        total_tasks = len(task_list)

        # get total number of completed and incomplete tasks
        tasks_complete = 0
        tasks_incomplete = 0

        for i in task_list:
            if i['Task Complete'] == 'yes':
                tasks_complete += 1

            # get total number of incomplete tasks
            else:
                tasks_incomplete += 1
        
        # get total number of tasks that are incomplete and past their due date
        # get todays date
        today = date.today()
        today_date = today.strftime("%d %B %Y")

        # count all past due tasks
        past_due = 0
        for i in task_list:
            # compare dates to find past due tasks
            if today_date > i['Due Date']:
                past_due += 1
        
        # debugging
        print(f"\n\nPast due: {past_due}\nTasks Complete: {tasks_complete}\nTasks incomplete: {tasks_incomplete}\n\n")
            
        # get the percentage of incomplete tasks
        print(f"Percentage of incomplete tasks: {round((tasks_incomplete / total_tasks) * 100, 2)}%")

        # get the percentage of tasks that are overdue
        print(f"Percentage of tasks overdue: {round((past_due / total_tasks) * 100, 2)}%")

        # write to task_overview.txt:
        with open('task_overview.txt', 'w') as f:
            f.write(f"\n\nPast due: {past_due}\nTasks Complete: {tasks_complete}\nTasks incomplete: {tasks_incomplete}\n\n")


    # user_overview.txt:
        # total number of users registered
        total_users = len(users)

        # total number of tasks
        total_tasks = len(task_list)

        # total tasks for each user
        # create a dictionary that holds the username as key and the number of related tasks as value
        user_task_dict = {}
        
        for i in task_list:
            user = i['Assigned To']
            if user not in user_task_dict:
                count = 1
                user_task_dict[user] = count
            elif user == i['Assigned To']:
                count += 1
                user_task_dict[user] = count
        # print(f"Tasks per user: {user_task_dict}")

        # for key, val in user_task_dict.items():
        #     print(f"{key} has a total of {val} tasks.")


        # percentage of tasks assigned to each user
        for key, val in user_task_dict.items():
            percent = (val/len(task_list)*100)
            # print(f"{key} has {percent}% of the total assigned tasks.")

        # percentage of tasks assigned to each user that are completed
        user_complete_dict = {}
        count = 1
        for i in task_list:
            user = i['Assigned To']
            
            if user not in user_complete_dict:
                if i['Task Complete'] == 'yes':
                    user_complete_dict[user] = count
                    
            elif user == i['Assigned To']:
                if i['Task Complete'] == 'yes':
                    count += 1
                    user_complete_dict[user] = count

        print(user_complete_dict)
                
        for key, val in user_complete_dict.items():
            percent_complete = round((val/user_task_dict[key])*100, 2)
            print(f"{key} has completed {val} tasks.\n")

            print(f"{key} has completed {percent_complete}% of tasks assigned.")

        # percentage of incomplete tasks for each user

        # percentage of overdue tasks for each user



#====Login Section====

# get user dictionary from 
users = user_dict('user.txt')

# ask user for username
username = input("Enter your username: \n")

# check username exists in the dictionary
while username.lower() not in users:
    print("Your username is not recognised")

    username = input("Enter your username: \n")

# ask user for password
password = input("Enter your password: \n")

# check user password against dictionary
while password.lower() != users[username]:
    print("Your password is not recognised")
    
    password = input("Enter your password: \n")


while True:

    if username.lower() == 'admin':
        menu = input('''Select one of the following options below\n:
                    s - show stats
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - view my task
                    gr - generate reports
                    e - Exit
: ''').lower()

    else:
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following options below\n:
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        e - Exit
    : ''').lower()
    

    # add new user if admin
    if menu == 'r':

        # get latest user dictionary
        users = user_dict('user.txt')

        reg_user(users)

    # add new task
    elif menu == 'a':

        # get latest user dictionary
        users = user_dict('user.txt')

        add_task(users)

    elif menu == 'va':

        # get latest task dictionary
        tasks = all_tasks('tasks.txt')

        view_all(tasks)

    elif menu == 'vm':

        # get latest task dictionary
        tasks = all_tasks('tasks.txt')
        
        view_mine(username, tasks)
            
    # exit the program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # display total users and total tasks
    elif menu == 's':

        # get total number of tasks
        with open('tasks.txt', 'r') as t:
            num_tasks = len(t.readlines())

        # get total number of users
        with open('user.txt', 'r') as u:
            num_users = len(u.readlines())

        print(f"\nThere are {num_tasks} tasks.")
        print(f"\nThere are {num_users} users.\n")


    # generate reports to 2 files
    elif menu == 'gr':

        # get all tasks
        task_list = all_tasks('tasks.txt')

        # get all users
        users = user_dict('user.txt')

        generateReports(task_list, users)


    # error handling
    else:
        print("\nYou have made a wrong choice, Please Try again\n")