#!/usr/bin/python3
""" API REST """

import requests
import csv
from sys import argv


def get_employee(id=None):
    if len(argv) > 1:
        try:
            id = int(argv[1])
        except ValueError:
            return

    if isinstance(id, int):
        base = "https://jsonplaceholder.typicode.com"
        user = requests.get(f"{base}/users/{id}").json()
        to_dos = requests.get(f"{base}/todos/?userId={id}").json()

        if user and to_dos:
            user_id = user["id"]
            username = user["username"]

            csv_filename = f"{user_id}.csv"

            with open(csv_filename, mode="w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
                csv.writer.writerow(["USER_ID", "USERNAME",
                                     "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for task in to_dos:
                    task_completed = task["completed"]
                    task_title = task["title"]
                    csv_writer.writerow([user_id, username,
                                         str(task_completed), task_title])

            print(f"Exported data to {csv_filename}")


if __name__ == "__main__":
    get_employee()
