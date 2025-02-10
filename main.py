import os
import sys
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE,"r", encoding = "utf-8") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding= "utf-8") as file:
        json.dump(tasks, file, indent = 4)

def strikethrough(text):
    return f"\033[9m{text}\033[0m"

def bold(text):
    return f"\033[1m{text}\033[0m"



def list(tasks):
    
    if len(tasks) == 0:
        return
    
    max_id_len = max(len(str(task["id"])) for task in tasks)


    for task in tasks:
        task_id = str(task["id"]).rjust(max_id_len)
        task_text = task["text"]

        if task["status"] == "done":
            task_text = strikethrough(task_text)
        
        if task["status"] == "in progress":
            task_text = bold(task_text)

        print(f"[{task_id}] {task_text}")


def main():

    tasks = load_tasks()

    if len(sys.argv) <= 1:
        list(tasks)
        # print(json.dumps(tasks, indent=4))
    elif sys.argv[1] in ("add", "a"):

        new_tasks = sys.argv[2:]
        new_id = max((task["id"] for task in tasks), default=0) + 1

        for i, text in enumerate(new_tasks):
            tasks.append({"id": new_id + i, "status": "new", "text": text})

        save_tasks(tasks)

    elif sys.argv[1] in ("remove", "rm"):
        if len(tasks) == 0:
            print("Remove takes at least 1 argument")
            return

        ids_to_remove = set(map(int, sys.argv[2:]))

        tasks = [task for task in tasks if task["id"] not in ids_to_remove]

        save_tasks(tasks)

    elif sys.argv[1] in ("sort", "s"):
        
        if sys.argv[2] in ("id", "i"):
            tasks.sort(key=lambda task: task["id"])
        elif sys.argv[2] in ("text", "t"):
            tasks.sort(key=lambda task: task["text"].lower())
        elif sys.argv[2] in ("status", "s"):
            tasks.sort(key=lambda task: task["status"])
        
        for i, task in enumerate(tasks):
            task["id"] = i + 1

        save_tasks(tasks)

    elif sys.argv[1] in ("done", "d"):
        done_ids = set(map(int, sys.argv[2:]))

        for task in tasks:
            if task["id"] in done_ids:
                task["status"] = "done"
        
        save_tasks(tasks)

    
    elif sys.argv[1] in ("in progress", "ip"):
        done_ids = set(map(int, sys.argv[2:]))

        for task in tasks:
            if task["id"] in done_ids:
                task["status"] = "in progress"
        
        save_tasks(tasks)

if __name__ == "__main__":
    main()
