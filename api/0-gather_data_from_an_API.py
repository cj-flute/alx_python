#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'

"""
import requests
import sys


def get_employee(id):
    userURL = f'https://jsonplaceholder.typicode.com/users/{id}'
    todoURL = f'https://jsonplaceholder.typicode.com/users/{id}/todos'

    # get empoyee data
    user_response = requests.get(userURL)
    user_data = user_response.json()
    EMPLOYEE_NAME = user_data['name']

    # get todo list for the employee
    todos_response = requests.get(todoURL)
    todos_data = todos_response.json()

    done_tasks = [task['title']
                  for task in todos_data if task['completed']]
    task_not_done = [task['title']
                     for task in todos_data if not task['completed']]

    NUMBER_OF_DONE_TASKS = len(done_tasks)
    NUMBER_OF_TASKS_NOT_DONE = len(task_not_done)
    TOTAL_NUMBER_OF_TASKS = NUMBER_OF_DONE_TASKS + NUMBER_OF_TASKS_NOT_DONE

    print(
        f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for TASK_TITLE in done_tasks:
        print(f'     {TASK_TITLE}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <id>")
    else:
        id = int(sys.argv[1])
        get_employee(id)
