#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress using a REST API
and exports the data in CSV format.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and exports the TODO list progress for a given employee ID in CSV format.
    """
    # API endpoints for employee details and TODO items
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Get employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    USER_ID = employee_data.get('id', 'Unknown')
    USERNAME = employee_data.get('username', 'Unknown')

    # Get TODO items for the employee
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Write data to CSV file
    csv_filename = f'{USER_ID}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write CSV header
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write tasks to CSV
        for task in todo_data:
            TASK_COMPLETED_STATUS = str(task['completed'])
            TASK_TITLE = task['title']
            csv_writer.writerow(
                [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])

    print(f'Data exported to {csv_filename}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
