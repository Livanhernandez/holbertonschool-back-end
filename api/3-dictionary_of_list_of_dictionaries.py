#!/usr/bin/python3
""" API REST """

import json
import requests
from sys import argv


api_users_url = 'https://jsonplaceholder.typicode.com/users'
api_todos_url = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(api_users_url)
users = response.json()

users_id = []
for user in users:
    users_id.append(user["id"])

json_dict = {}

for employee_id in users_id:
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)

    employee_name = response.json()["username"]

    api_url2 = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    response = requests.get(api_url2)

    tasks = response.json()

    json_dict[employee_id] = []
    for task in tasks:
        json_format = {
            "username": employee_name,
            "task": task["title"],
            "completed": task["completed"]
        }
        json_dict[employee_id].append(json_format)

with open("todo_all_employees.json", 'w')as json_file:
    json.dump(json_dict, json_file)
