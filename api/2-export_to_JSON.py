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

            tasks_list = []
            for todo in todos_data:
                task_info = {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": user_data["username"]
                }
                tasks_list.append(task_info)

            user_id = id
            tasks_dict = {str(user_id): tasks_list}

            print(
                f"Employee {user_data['name']} is done with tasks(
                    {len(tasks_list)}/{len(todos_data)})")
            for task in tasks_list:
                print(f"\t{task['task']} (Completed: {task['completed']})")

            with open(f"{user_id}.json", 'w') as json_file:
                json.dump(tasks_dict, json_file, indent=4)


if __name__ == "__main__":
    get_employee
