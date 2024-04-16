#!/usr/bin/python3
""" API REST """

import json
import requests
from sys import argv


def get_employee(id=None):
    """ Retrieves info about the employee's tasks"""

    if len(argv) > 1:
        try:
            id = int(argv[1])
        except ValueError:
            pass
            return

    if isinstance(id, int):
        user_response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{id}")
        todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/?userId={id}")

        if todos_response.status_code == 200 and \
                user_response.status_code == 200:
            user_data = json.loads(user_response.text)
            todos_data = json.loads(todos_response.text)

            total_tasks = len(todos_data)
            tasks_completed = 0
            titles_completed = []

            for todo in todos_data:
                if todo['completed'] is True:
                    tasks_completed += 1
                    titles_completed.append(todo['title'])

            print(
                f"Employee {user_data['name']} is done with tasks(
                    {len(tasks_completed)}/{len(total_tasks)})")
            for title in titles_completed:
                print(f"\t {title}")

            json_dict = {user_data['id']: []}
            for task in todos_data:
                task_info = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': user_data['username']
                }

            with open(f"{user_data}.json", 'w') as json_file:
                json.dump(json_dict, json_file)


if __name__ == "__main__":
    get_employee
