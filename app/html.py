from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

def read_template(name: str) -> str:
    with open(TEMPLATES / name, "r", encoding="utf-8") as f:
        return f.read()

def render(template_name: str, **ctx) -> str:
    # VERY tiny placeholder renderer: {{key}} replacements only
    html = read_template(template_name)
    for k, v in ctx.items():
        html = html.replace("{{" + k + "}}", str(v))
    return html

def render_task_rows(tasks: list[dict]) -> str:
    row_tpl = read_template("components/task_row.html")
    rows = []
    for t in tasks:
        r = row_tpl
        for k, v in t.items():
            r = r.replace("{{" + k + "}}", str(v))
        # extra computed
        r = r.replace("{{checked}}", "checked" if t.get("done") else "")
        r = r.replace("{{strike}}", "line-through opacity-60" if t.get("done") else "")
        rows.append(r)
    return "\n".join(rows)
