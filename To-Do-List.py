# This program add and removes tasks from the list. Its simply a to-do-list application
# The function below just gets the user's name and says 'Hello'

def get_user_name(name):
    print(f"Hello {name}") 
    return 
greet = get_user_name(input(f"What is your name?:"))

# This function adds accepts or adds 20 tasks to the list at a time
def Add_To_List(task_list,task):
    print(f"Item has been added: {task}")
    task_list.append(task) # Adds tasks to the task_list
    return 

task_list = [] # Stores the tasks added to to the list
def add_task(task_list):
    for _ in range(20): # Only collects 20 tasks 
        task_list.append(input('Add task: ')) # 
        print(f"You have successfully added: {task_list}")
        prompt = input('Do you want to add more task to your list? (yes/no): ') # Here just prompts the user to add task to list
        if prompt.lower() == 'yes': # we get a positive/negative response from the user then move forward to adding the task to the list
            continue
        elif prompt.lower() == 'no':
            make_sure = input('Are you sure (y/n): ')
        if make_sure.lower() == 'n':
            continue
        else:
            make_sure.lower() == 'y'
            break
    else:
        prompt.lower() != 'yes' or 'no'
        raise Exception('Must indicate YES or NO')
    return 

list_of_item = add_task(task_list)
print(f"Hello, these are your tasks: {task_list}")
# The function below is used to remove tasks from the list


def remove_task(task_list):
    for _ in range(20): # Iterates 20 times prompting user to remove task at will
        prompt = input('Do you want to remove an item from the list? (y/n): ')
        if prompt.lower() == 'y':
            task_list.remove(input('Enter item to be removed: '))# Simply removes the task from the list
            print(f'Task has been from removed from: {task_list}')
            if len(task_list) == 0:# Checks if the list is empty or not, by checking if the length of the list is zero which means 'empty'
                print('The list is now empty!')
            else:
                print(task_list)    
        elif prompt.lower() == 'n':
            make_sure = input('Are you sure (y/n): ')
            if make_sure.lower() == 'n':
                continue
            else:
                make_sure.lower() == 'y'
                break
    if len(task_list) == 0:
        print('The list is empty!')
    else:
        print(task_list)    

    return task_list

remove_task(task_list)
print(f'These are the tasks on your current list: {task_list}')

