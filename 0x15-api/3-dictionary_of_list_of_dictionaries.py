#!/usr/bin/python3

"""export data in the JSON format for all users."""

import json
import requests


def get_all_employees_todo():
    # Define the base URL of the API
    userurl = "https://jsonplaceholder.typicode.com/users"
    todourl = "https://jsonplaceholder.typicode.com/todos"

    # Make a GET request to retrieve all users
    response = requests.get(userurl)
    if response.status_code != 200:
        print("Error: Failed to retrieve employee information")
        return {}

    users = response.json()

    # Prepare JSON data
    json_data = {}
    for user in users:
        # Make a GET request to retrieve employee's TODO list
        response = requests.get(todourl)
        if response.status_code != 200:
            print(f"Error: Failed to retrieve TODO list for user {user['id']}")
            continue

        todo_list = response.json()

        # Add user's tasks to JSON data
        json_data[str(user['id'])] = []
        for task in todo_list:
            json_data[str(user['id'])].append({
                "username": user['username'],
                "task": task['title'],
                "completed": str(task['completed']).lower()
            })

    return json_data


def export_todo_to_json(json_data):
    # Export data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"\nData exported to {json_filename}")


if __name__ == "__main__":
    json_data = get_all_employees_todo()
    if json_data:
        export_todo_to_json(json_data)
    else:
        print("No data to export.")

