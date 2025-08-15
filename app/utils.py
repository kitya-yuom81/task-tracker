import time
import urllib.parse

def new_id() -> str:
    # simple unique-ish ID based on timestamp
    return hex(int(time.time() * 1_000_000))[2:]

def parse_form(body_bytes: bytes) -> dict:
    data = urllib.parse.parse_qs(body_bytes.decode("utf-8"), keep_blank_values=True)
    # flatten single values
    return {k: v[0] if isinstance(v, list) and v else "" for k, v in data.items()}

def http_response(body: bytes, status: int = 200, content_type: str = "text/html; charset=utf-8"):
    headers = [
        ("Content-Type", content_type),
        ("Content-Length", str(len(body))),
        ("Cache-Control", "no-store"),
    ]
    return status, headers, body
