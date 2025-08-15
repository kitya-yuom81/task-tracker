from storage import load_tasks, save_tasks
from html import render, render_task_rows
from validators import validate_task
from utils import new_id, http_response

def page_index(message: str = ""):
    tasks = load_tasks()
    rows_html = render_task_rows(tasks)
    body = render(
        "index.html",
        rows=rows_html,
        flash=message or ""
    ).encode("utf-8")
    return http_response(body)

def post_add(form: dict):
    title = form.get("title", "").strip()
    ok, err = validate_task(title)
    if not ok:
        return page_index(err)

    tasks = load_tasks()
    tasks.append({
        "id": new_id(),
        "title": title,
        "done": False
    })
    save_tasks(tasks)
    return page_index("Task added.")

def post_toggle(form: dict):
    task_id = form.get("id", "")
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t.get("done", False)
            break
    save_tasks(tasks)
    return page_index("Status updated.")

def post_delete(form: dict):
    task_id = form.get("id", "")
    tasks = [t for t in load_tasks() if t["id"] != task_id]
    save_tasks(tasks)
    return page_index("Task deleted.")
