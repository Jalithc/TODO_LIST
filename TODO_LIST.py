from tabulate import tabulate
import sys

todo_list = []

def display_menu():
    print("SIMPLE TODO LIST")
    print("1. Display the todo list")
    print("2. Add items todo list")
    print("3. Mark items as completed")
    print("4. Delete items from todo list")
    print("5. Exit")

def display_list():
    headers = ["Task Number", "Task Name", "Task Status"]
    table_data = []

    for i, item in enumerate(todo_list, start=1):
        task_name = item[0]
        task_status = "Done" if item[1] else "Not completed"
        table_data.append([i, task_name, task_status])

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def add_item(task):
    todo_list.append(task)

def complete_task(task_number):
    task = todo_list[task_number - 1]
    completed_task = (task[0], True)
    todo_list[task_number - 1] = completed_task

def delete_task(task_name):
    for task in todo_list:
        if task[0] == task_name:
            todo_list.remove(task)

while True:
    display_menu()
    choice = int(input("What's your choice: "))
    if choice == 1:
        display_list()
    elif choice == 2:
        item_name = input("Enter the task name: ")
        is_completed = False
        task = (item_name, is_completed)
        add_item(task)
    elif choice == 3:
        task_number = int(input("Enter task number to complete: "))
        complete_task(task_number)
    elif choice == 4:
        task_name = input("Enter the task name to delete: ")
        delete_task(task_name)
    elif choice == 5:
        sys.exit()
