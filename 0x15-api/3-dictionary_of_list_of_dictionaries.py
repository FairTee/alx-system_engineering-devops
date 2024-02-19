#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
"""

import json
import requests
import sys

if __name__ == "__main__":
    jsonph = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(jsonph)
    employees = response.json()
    print(employees)

    data_dict = {}

    for employee in employees:
        USER_ID = employee.get('id')
        username = employee.get('username')
        x = 'https://jsonplaceholder.typicode.com/users/{}/todos'
        url = x.format(USER_ID)
        response = requests.get(url)
        tasks = response.json()
        data_dict[USER_ID] = []
        for task in tasks:
            data_dict[USER_ID].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            })

    # Write the tasks data to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data_dict, f)
