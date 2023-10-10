#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'

"""

import sys
import requests


def get_employee(id):
    # get empoyee data
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    user_data = user_response.json()
    EMPLOYEE_NAME = user_data['name']

    # get todo list for the employee
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/1/todos')
    todos_data = todos_response.json()

    completed_tasks = [task['title']
                       for task in todos_data if task['completed']]
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(todos_data)

    print(
        f'Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for task_title in completed_tasks:
        print(f'\t{task_title}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <id>")
    else:
        id = int(sys.argv[1])
        get_employee(id)
