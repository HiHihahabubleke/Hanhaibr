import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

ALLOWED_FILES = {"PM03.json", "PM04.json"}

# Обработчик HTTP-запросов
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/questions"):
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)
            filename = params.get("file", ["PM04.json"])[0]

            if filename not in ALLOWED_FILES:
                self.send_response(400)
                self.end_headers()
                return

            try:
                with open(filename, "r", encoding="utf-8") as f:
                    questions = json.load(f)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(questions).encode("utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        else:
            super().do_GET()

# Запуск сервера
def run_server():
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), MyHandler)
    print(f"Сервер запущен на http://{host}:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
