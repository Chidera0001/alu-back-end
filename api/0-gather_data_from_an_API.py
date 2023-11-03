#!/usr/bin/python3

import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_employee_todo_progress(employee_id):
    """
    Fetch and display TODO list progress for a given employee.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    # Make a GET request to the API endpoint for the specified employee
    response = requests.get(f"{BASE_URL}/todos?userId={employee_id}")

    if response.status_code == 200:
        todos = response.json()

        # Count the number of completed and total tasks
        completed_tasks = [todo for todo in todos if todo.get('completed')]
        total_tasks = len(todos)

        # Get the employee's name
        user_response = requests.get(f"{BASE_URL}/users/{employee_id}")
        employee_name = user_response.json().get('name')

        # Display the progress information
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        print(f"{employee_name}: {len(completed_tasks)}/{total_tasks}")

        # Display the titles of completed tasks
        for todo in completed_tasks:
            print(f"\t{todo.get('title')}")

    else:
        print(f"Failed to fetch data for employee ID {employee_id}. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for the employee ID.")

