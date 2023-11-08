#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress using a REST API
and exports the data in JSON format.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and exports the TODO list progress for a given employee ID in JSON format.
    """
    # API endpoints for employee details and TODO items
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Get employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    USER_ID = str(employee_data.get('id', 'Unknown'))
    USERNAME = employee_data.get('username', 'Unknown')

    # Get TODO items for the employee
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare JSON data
    json_data = {USER_ID: []}
    for task in todo_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": USERNAME
        }
        json_data[USER_ID].append(task_data)

    # Write data to JSON file
    json_filename = f'{USER_ID}.json'
    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f'Data exported to {json_filename}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
