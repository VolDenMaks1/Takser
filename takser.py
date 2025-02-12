#!/usr/bin/env python3
import os
import sys
import json

# Define the path to the file in ~/.cache/takser/tasks.json
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "takser")
TASKS_FILE = os.path.join(CACHE_DIR, "tasks.json")

# Create the ~/.cache/takser directory if it does not exist
os.makedirs(CACHE_DIR, exist_ok=True)

def load_tasks():
    #Load tasks from the file if it exists, otherwise return an empty list
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    #Save tasks to the file in JSON format
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def strikethrough(text):
    #Format text with strikethrough using ANSI escape codes
    return f"\033[9m{text}\033[0m"

def bold(text):
    #Format text in bold using ANSI escape codes
    return f"\033[1m{text}\033[0m"

def list_tasks(tasks):
    #Display the list of tasks formatted based on their status
    if not tasks:
        return

    max_id_len = max(len(str(task["id"])) for task in tasks)  # Calculate max width for task IDs

    for task in tasks:
        task_id = str(task["id"]).rjust(max_id_len)  # Right-align task IDs for readability
        task_text = task["text"]

        if task["status"] == "done":
            task_text = strikethrough(task_text)  # Apply strikethrough formatting for completed tasks
        elif task["status"] == "in progress":
            task_text = bold(task_text)  # Apply bold formatting for tasks in progress

        print(f"[{task_id}] {task_text}")

def main():
    #Main function to handle task management commands
    tasks = load_tasks()

    if len(sys.argv) <= 1:
        list_tasks(tasks)  # List tasks if no arguments are provided
    elif sys.argv[1] in ("add", "a"):
        new_tasks = sys.argv[2:]
        new_id = max((task["id"] for task in tasks), default=0) + 1  # Generate a new task ID

        for i, text in enumerate(new_tasks):
            tasks.append({"id": new_id + i, "status": "new", "text": text})

        save_tasks(tasks)

    elif sys.argv[1] in ("remove", "rm"):
        if not tasks:
            print("Remove takes at least 1 argument")
            return

        ids_to_remove = set(map(int, sys.argv[2:]))  # Convert arguments to a set of IDs
        tasks = [task for task in tasks if task["id"] not in ids_to_remove]  # Remove tasks with matching IDs

        save_tasks(tasks)

    elif sys.argv[1] in ("sort", "s"):
        if sys.argv[2] in ("id", "i"):
            tasks.sort(key=lambda task: task["id"])  # Sort tasks by ID
        elif sys.argv[2] in ("text", "t"):
            tasks.sort(key=lambda task: task["text"].lower())  # Sort tasks alphabetically (case insensitive)
        elif sys.argv[2] in ("status", "s"):
            tasks.sort(key=lambda task: task["status"])  # Sort tasks by status

        for i, task in enumerate(tasks):
            task["id"] = i + 1  # Reassign task IDs sequentially after sorting

        save_tasks(tasks)

    elif sys.argv[1] in ("done", "d"):
        done_ids = set(map(int, sys.argv[2:]))  # Convert arguments to a set of IDs

        for task in tasks:
            if task["id"] in done_ids:
                task["status"] = "done"  # Mark tasks as done

        save_tasks(tasks)

    elif sys.argv[1] in ("in progress", "ip"):
        progress_ids = set(map(int, sys.argv[2:]))  # Convert arguments to a set of IDs

        for task in tasks:
            if task["id"] in progress_ids:
                task["status"] = "in progress"  # Mark tasks as in progress

        save_tasks(tasks)
    elif sys.argv[1] in ("raw", "r"):
        print(json.dumps(tasks, indent=4))  # Print raw JSON representation of tasks

if __name__ == "__main__":
    main()
