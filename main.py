import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Загружаем вопросы из JSON-файла
with open("PM04.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

# Обработчик HTTP-запросов
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/questions":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(QUESTIONS).encode("utf-8"))
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