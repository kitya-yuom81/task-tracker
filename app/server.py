from http.server import HTTPServer, BaseHTTPRequestHandler
from utils import parse_form, http_response
# from  .
import routes

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            status, headers, body = routes.page_index()
            self._send(status, headers, body)
        else:
            self._send(*http_response(b"Not found", 404, "text/plain; charset=utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""
        form = parse_form(body)

        if self.path == "/add":
            res = routes.post_add(form)
        elif self.path == "/toggle":
            res = routes.post_toggle(form)
        elif self.path == "/delete":
            res = routes.post_delete(form)
        else:
            res = http_response(b"Not found", 404, "text/plain; charset=utf-8")

        self._send(*res)

    def _send(self, status, headers, body):
        self.send_response(status)
        for k, v in headers:
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

def run(host="127.0.0.1", port=8000):
    httpd = HTTPServer((host, port), Handler)
    print(f"Serving on http://{host}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
