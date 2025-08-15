import json
from pathlib import Path
from typing import List, Dict, Any

DATA_PATH= Path (__file__).resolve().parent.parent/ "data"/ "tasks-json"
def load_tasks() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    try:
        with open(DATA_PATH, "r", encoding= "utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return[]
def save_tasks(tasks: List[Dict[str, Any]])-> None:
    DATA_PATH.parent.mkdir(
        parents = True,
        exist_ok= True
    )
    with open(DATA_PATH, "w", encoding="utf-8" as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)





