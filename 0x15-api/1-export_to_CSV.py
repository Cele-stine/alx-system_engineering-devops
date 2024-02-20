#!/usr/bin/python3
"""Using a REST API for a given employee ID, returns info about his/her TODO
list progress"""

import csv
import requests
import sys


def get_todo_list_progress(employee_id):

    url = "https://jsonplaceholder.typicode.com"

    # GET eployee info
    response = requests.get(f"{url}/users/{employee_id}")
    if response.status_code != 200:
        print("Error: could not retrive data")
        return

    employee_data = response.json()
    name = employee_data['name']

    # GET employee todo list
    response = requests.get(f"{url}/todos?userId={employee_id}")
    if response.status_code != 200:
        print("Error: could not retrive todo list")
        return

    todo_list = response.json()

    D_TKS = sum(1 for task in todo_list if task['completed'])

    TASKS = len(todo_list)

    # iprint titles of completed tasks
    for task in todo_list:
        if task['completed']:
            print(f"     {task['title']}")
    # write data to a CSV file
    username = employee_data['username']
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            csv_writer.writerow([employee_id, username, str(task['completed']).lower(), task['title']])
    print(f"\nData exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        sys.exit(1)

    get_todo_list_progress(employee_id)
