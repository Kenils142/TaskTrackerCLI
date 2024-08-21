import os
import json
import sys

from datetime import datetime

FILE_NAME = "tasks.json"


# Handles Fetching list of tasks from json file
def get_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as data:
            tasks = json.load(data)
    else:
        return []
    return tasks


# Handles creation of new tasks
def add_task(description):
    
    # Vailidating params
    if len(description) > 20:
        print("Description Max Length: 20 Characters.")
        return 
    
    creation_date = datetime.now().strftime('%a %d %b %Y, %I:%M %p')
    tasks = get_tasks()

    new_task = {
        'id' : len(tasks) + 1,
        'description': description,
        'status': 'incomplete',
        'createdAt': creation_date,
        'updatedAt': creation_date 
    }

    # Writing list of tasks to File
    with open(FILE_NAME, "w") as file:
        tasks.append(new_task)
        json.dump(tasks, file, indent=4)

    # Logging Output to CLI
    print("Task added successfully.")


# Handles Updating of tasks
def update_task(id, description):

    # Validating description
    if len(description) > 20:
        print("Description Max Length: 20 Characters.")
        return 
    
    update_time = datetime.now().strftime('%a %d %b %Y, %I:%M %p')
    tasks = get_tasks()

    # Validating id
    try:
        id = int(id)
    except ValueError:
        print(f"No task with id {id}.")
        
    if id <= 0 or len(tasks) < id:
        print(f"No task with id {id}.")
        return

    # Performing update
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = update_time
    
    # Storing the Update
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

    # Logging update to CLI
    print("Task updated successfully.")


# Handles deletion of tasks
def delete_task(id):
    tasks = get_tasks()
    tasks_len = len(tasks)

    # Validating id
    try:
        id = int(id)
    except ValueError:
        print(f"No task with id {id}.")
        
    if id <= 0 or len(tasks) < id:
        print(f"No task with id {id}.")
        return
    
    # Changing ids of tasks.
    if id < len(tasks):
        for i in range(id, tasks_len):
            tasks[i]["id"]=i
    
    # Deleting task
    description = tasks[id-1]["description"]
    status = tasks[id-1]["status"]
    tasks.pop(id-1)

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

    # Logging to CLI
    print("Task deleted successfully.")


# Handles changing status of task
def update_status(id, status):
    possible_status = ["incomplete", "in-progress", "done"]
    
    # Validating status
    if status not in possible_status:
        print("Valid status: 'incomplete, 'in-progress' or 'done'.") 
        return 
    
    update_time = datetime.now().strftime('%a %d %b %Y, %I:%M %p')
    tasks = get_tasks()

    # Validating id
    try:
        id = int(id)
    except ValueError:
        print(f"No task with id {id}.")
        
    if id <= 0 or len(tasks) < id:
        print(f"No task with id {id}.")
        return

    # Performing update
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = update_time
    
    # Storing the Update
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

    # Logging update to CLI
    print("Status updated successfully.")
   

# Handles Listing all 
def list_tasks(list_type="all"):
    list_types = ["all", "incomplete", "in-progress", "done"]

    if list_type not in list_types:
        print("Valid Options for listing tasks: 'all', 'incomplete', 'in-progress' or 'done'.")
        return
    
    tasks = get_tasks()
    if list_type == "all":
        all = True
    else:
        all = False

    exists = False 

    # Logging task list to CLI
    for task in tasks:
        if all or task["status"] == list_type:
            exists = True
            print(f"ID: {task["id"]}\nDescription: {task["description"]}\nStatus: {task["status"]}\n" +
                f"Created At: {task["createdAt"]}\nUpdated At: {task["updatedAt"]}\n")
      
    if exists == False:
        if all == True:
            print("There are no tasks in tracker.")
        else:
            print(f"There are no tasks which are marked as {list_type}.\n")
    

# Handling CLI commands

help_str = """Task Tacker CLI, version 1.0.0
Help Menu.

Note that in this CLI Application | is equal to OR.
so if you see --help | -h it means either you can use --help or -h.
Any of the two will work. 

Angle bracket (< >) are for you to understand that you need to provide some input there 
you dont have to write those brackets, they arent part of command.


To add task to tracker use command:
task-cli.py --add | -a <"task-description">

To update task description of a task, use command:
task-cli.py --update | -u <task-id> <"new-description">

To delete a task from the tracker, use command:
task-cli.py --delete | -d <task-id>

To change status of a task, use command:
task-cli.py --mark-as | -m <"incomplete" | "in-progress" | "done">

To view all the tasks in traker, use command:
task-cli.py --list | -l

To view tasks based on their status, use command:
task-cli.py --list | -l <"incomplete" | "in-progress" | "done">
"""

if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print("No Arguments found, please use 'task-cli.py --help for help.")
    else:
        match sys.argv[1:]:
            case ["--add" | "-a", description]:
                add_task(description)
            case ["--update" | "-u", id, description]:
                update_task(id, description)
            case ["--delete" | "-d", id]:
                delete_task(id)
            case ["--mark-as" | "-m", id, status]:
                update_status(id, status)
            case ["--list" | "-l"]:
                list_tasks()
            case ["--list" | "-l", list_type]:
                    list_tasks(list_type)
            case ["--help" | "-h"]:
                print(help_str)
            case _:
                print("Invalid Arguments, please use 'task-cli.py --help | -h' for help.")
