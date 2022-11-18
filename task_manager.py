#=====importing libraries===========
from datetime import datetime, date

#======= Define Functions ========#

# read contents of file and transfer it into a dictionary
def create_dict(filename, user):

    # open tasks file to get number of tasks
    with open(filename, 'r') as f:
        tasks = f.readlines()

    # create list to hold all tasks as dictionaries
    task_list = []

    # loop through all lines, tokenise each sentence in each line
    for i, dict in enumerate(range(0, len(tasks))):
        tokenised = tasks[i].split(', ')

        # strip the newline character 
        tokenised[5] = tokenised[5].strip('\n')

        # create a dictionary for all tasks
        i = {}   

        # check whether to only add specific user tasks or all
        if user == tokenised[0]:
            i['id'] = dict + 1
            i['Task'] = tokenised[1]
            i['Assigned To'] = tokenised[0]
            i['Date Assigned'] = tokenised[3]
            i['Due Date'] = tokenised[4]
            i['Task Complete'] = tokenised[5]
            i['Task Description'] = tokenised[2]

            # append the dictionary for each task
            task_list.append(i)
    

        elif user == 'all':
            i['id'] = dict + 1
            i['Task'] = tokenised[1]
            i['Assigned To'] = tokenised[0]
            i['Date Assigned'] = tokenised[3]
            i['Due Date'] = tokenised[4]
            i['Task Complete'] = tokenised[5]
            i['Task Description'] = tokenised[2]

            # append the dictionary for each task
            task_list.append(i)
    
    return task_list


# take selection from user
def reg_user():

    if username == 'admin':
    # get user input for new username
        new_user = input("\nEnter the new username: \n")

        # check it does not already exist
        if new_user in user_dict:
            print("\nThis username is already in use\n")
            
        # get user input for new password
        else:
            new_pass = input("\nEnter the new password: \n")

            # get user to enter password again and check they match
            new_pass_check = input("\nEnter the password again to check for match: \n")

            if new_pass != new_pass_check:
                print("\nThe passwords do not match\n")
                
            else:
                # append 'a' new user details to user.txt
                with open('user.txt', 'a') as f:
                    f.write('\n' + new_user + ', ' + new_pass)
                    pass
    else:
        print("\nYou have to have administrator privileges to add users.\n")


def add_task():
    # get username
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
    due_date = input("\nEnter the due date of the task: \n")

    # get the completion status of the task
    status = input("\nHas the task been completed? Enter 'yes' or 'no': \n")

    # validate input matches acceptable parameters
    if status.lower() == 'yes':
        pass
    elif status.lower() == 'no':
        pass
    else:
        print("Input error")

        status = input("\nHas the task been completed? Enter 'yes' or 'no': \n")

    # get the current date
    today = date.today()
    today_date = today.strftime("%d %B %Y")
    print(today_date)

    # write the new task to 'tasks.txt'
    with open('tasks.txt', 'a') as t:
        t.write('\n' + user + ', ' + title + ', ' + 
        description + ', ' + str(today_date) + ', ' + due_date + ', ' + status)


def view_all():
    
    # convert all tasks to a list of dictionaries
    all_tasks = create_dict('tasks.txt', 'all')

    # loop through each task
    for i in range(len(all_tasks)):

        # create upper border
        print("\n", ("-" * 100))

        # present data in a readable format
        print(f"Task:\t\t\t\t{all_tasks[i]['id']}\nAssigned To:\t\t\t{all_tasks[i]['Assigned To']}\nDate Assigned:\t\t\t{all_tasks[i]['Date Assigned']}\nDue Date:\t\t\t{all_tasks[i]['Due Date']}\nTask Complete:\t\t\t{all_tasks[i]['Task Complete']}\nTask Description:\n  {all_tasks[i]['Task Description']}")

    # create lower border
    print("-" * 100, '\n')
    

def view_mine(user):

    # create dict of tasks for logged in user
    user_tasks = create_dict('tasks.txt', user)

    # user select to view all or a specific task by number 
    selection = int(input("Select specific tasks by number, or type '0' to view all. Type '-1' to return to menu: \n"))

    # if user enters -1, quit to main menu
    while selection != -1:

        # show user all of their tasks
        if selection == 0:
            for i in range(len(user_tasks)):
                print(f"\nTask:\t\t\t\t{user_tasks[i]['id']}\nAssigned To:\t\t\t{user_tasks[i]['Assigned To']}\nDate Assigned:\t\t\t{user_tasks[i]['Date Assigned']}\nDue Date:\t\t\t{user_tasks[i]['Due Date']}\nTask Complete:\t\t\t{user_tasks[i]['Task Complete']}\nTask Description:\n  {user_tasks[i]['Task Description']}\n")

        # exit the selection loop                               
        elif selection == -1:
            break

        # validation check
        elif selection > len(user_tasks):
            print("\nError. selection not recognised.\n")

        # print the selected task
        else:
            print(f"\nTask:\t\t\t\t{user_tasks[selection-1]['id']}\nAssigned To:\t\t\t{user_tasks[selection-1]['Assigned To']}\nDate Assigned:\t\t\t{user_tasks[selection-1]['Date Assigned']}\nDue Date:\t\t\t{user_tasks[selection-1]['Due Date']}\nTask Complete:\t\t\t{user_tasks[selection-1]['Task Complete']}\nTask Description:\n  {user_tasks[selection-1]['Task Description']}\n")

            # get task for potential editing by user
            selected = user_tasks[selection-1]
        break

    # get input from user to edit task if desired
    edit = input("Would you like to edit the task? Type 'yes' or 'no': ")

    while edit.lower().strip() != 'yes' or edit != 'no':
        print("\nError. Input not recognised.\n\n")
        edit = input("Would you like to edit the task? Type 'yes' or 'no': ")

        if edit == 'yes':
            field = input("\nWould you like to edit the user field or the due date field? Type 'user' or 'date': \n")

            while field.lower() != 'data' or field.lower() != 'user':
                print("\nError. Input not recognised\n")

                field = input("\nWould you like to edit the user field or the due date field? Type 'user' or 'date': \n")

                ###### works but need to write to output file in a way that doesnt lose other data #####
                #### need to hold the entire tasks.txt in memory and update the entire thing ####
                if field == 'user':
                    new_user = input("\nEnter the new username: \n")
                    selected['Assigned To'] = new_user
                    print(selected)
                    break
                    

                elif field == 'date':
                    new_date = input("\nEnter the new due date: \n")
                    selected['Due Date'] = new_date
                    break
                break
            break
                    
        
        elif edit == 'no':
            break



#====Login Section====

# create dictionary to store usernames and passwords
user_dict = {}

# open credentials text file
with open('user.txt', 'r') as f:
    contents = f.readlines()

# loop through all lines, tokenise the username and password
for i in range(0, len(contents)):
    tokenised = contents[i].split()

    # strip the comma from username and store as key value pairs in dictionary
    user_dict[tokenised[0].strip(",")] = tokenised[1]

# ask user for username
username = input("Enter your username: \n")

# check username exists in the dictionary
while username.lower() not in user_dict:
    print("Your username is not recognised")

    username = input("Enter your username: \n")

# ask user for password
password = input("Enter your password: \n")

# check user password against dictionary
while password.lower() != user_dict[username]:
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

        reg_user()

    # add new task
    elif menu == 'a':

        add_task()

    elif menu == 'va':

        view_all()

    elif menu == 'vm':
        
        view_mine(username)
            
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

    # error handling
    else:
        print("\nYou have made a wrong choice, Please Try again\n")