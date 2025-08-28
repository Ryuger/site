
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="html", **kwargs)
    
    def end_headers(self):
        # Запрещаем кеширование для HTML, CSS, JS и JSON файлов
        if self.path.endswith(('.html', '.css', '.js', '.json')):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        # Добавляем CORS заголовки
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def guess_type(self, path):
        result = super().guess_type(path)
        if len(result) == 2:
            mimetype, encoding = result
        else:
            mimetype = result[0] if result else None
            encoding = result[1] if len(result) > 1 else None
        
        if path.endswith('.js'):
            return 'application/javascript', encoding
        return mimetype, encoding

if __name__ == "__main__":
    port = 5000
    
    # Проверяем существование директории html
    if not os.path.exists('html'):
        print("Ошибка: директория 'html' не найдена!")
        exit(1)
    
    try:
        server = HTTPServer(('0.0.0.0', port), CustomHandler)
        print(f"Сервер запущен на порту {port}")
        print(f"Откройте http://localhost:{port}/ для просмотра index.html")
        print(f"Доступные страницы:")
        print(f"  - http://localhost:{port}/ (index.html)")
        print(f"  - http://localhost:{port}/Update Certex VPN Clients.html")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
    except Exception as e:
        print(f"Ошибка запуска сервера: {e}")
