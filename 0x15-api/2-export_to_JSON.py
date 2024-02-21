#!/usr/bin/python3

"""export data in the JSON format."""

import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to retrieve employee information
    response = requests.get(f"{base_url}/users/{employee_id}")
    if response.status_code != 200:
        print("Error: Failed to retrieve employee information")
        return

    employee_data = response.json()
    employee_name = employee_data['name']
    username = employee_data['username']

    # Make a GET request to retrieve employee's TODO list
    response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if response.status_code != 200:
        print("Error: Failed to retrieve employee's TODO list")
        return

    todo_list = response.json()

    # Prepare JSON data
    json_data = {
        str(employee_id): []

    }
    for task in todo_list:
        json_data[str(employee_id)].append({"task": task["title"], "completed":
                                     str(task['completed']).lower(),
                                     "username": username})

    # Export data to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"\nData exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
