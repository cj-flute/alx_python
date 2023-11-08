import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url)
    tasks = response.json()

    user_tasks = {}
    for task in tasks:
        task_data = {
            "username": task["userId"],
            "task": task["title"],
            "completed": task["completed"]
        }
        if task["userId"] not in user_tasks:
            user_tasks[task["userId"]] = []
        user_tasks[task["userId"]].append(task_data)

    with open(f"{user_id}.json", "w") as outfile:
        json.dump(user_tasks, outfile)
