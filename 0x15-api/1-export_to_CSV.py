#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import sys
import requests
import csv


def fetch_todo_progress(employee_id):
    # Fetching data from the API
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Extracting relevant information
    employee_name = ""
    tasks = []

    for todo in todos:
        if not employee_name:
            employee_name = todo['userId']
        tasks.append([employee_name, todo['completed'], todo['title']])

    # Writing data to CSV file
    filename = f"{employee_name}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME',
                         'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        writer.writerows(tasks)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_progress(employee_id)
