import json
from pathlib import Path

FILE = Path("tasks.json")

def load():
    return json.loads(FILE.read_text()) if FILE.exists() else []

def save(tasks):
    FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2))

tasks = load()
while True:
    cmd = input("add / list / done / quit: ").strip()
    if cmd == "add":
        tasks.append({"title": input("Tasks:"), "done": False})
    elif cmd == "list":
        for i, t in enumerate(tasks, 1):
            print(i, "✓" if t["done"] else "✗", t["title"])
    elif cmd == "done":
        i = int(input("Number Tasks : ")) - 1
        tasks[i]["done"] = True
    elif cmd == "quit":
        break
    save(tasks)