def validate_task(title: str) -> tuple[bool, str]:
    title = (title or "").strip()
    if not title:
        return False, "Title is required."
    if len(title) > 100:
        return False, "Title is too long (max 100)."
    return True, ""
