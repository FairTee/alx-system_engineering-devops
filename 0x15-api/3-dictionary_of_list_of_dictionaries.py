#!/usr/bin/python3

import sys
import requests
import json


def fetch_todo_progress():
    # Fetching data from the API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    # Organizing tasks by user ID
    tasks_by_user = {}
    for todo in todos:
        user_id = str(todo['userId'])
        task_info = {"username": user_id, "task": todo['title'],
                     "completed": todo['completed']}
        if user_id in tasks_by_user:
            tasks_by_user[user_id].append(task_info)
        else:
            tasks_by_user[user_id] = [task_info]

    # Writing data to JSON file
    with open("todo_all_employees.json", mode='w') as file:
        json.dump(tasks_by_user, file)

    print("Data exported to todo_all_employees.json")


if __name__ == "__main__":
    fetch_todo_progress()
