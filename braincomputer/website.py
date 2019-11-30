import functools
import http.server
import re

class Website:
    my_handlers = {}

    def route(self, path):
        def decorator(f):
            Website.my_handlers[path] = f
            @functools.wraps(f)
            def wrapper(*args):
                return f(*args)
            return wrapper
        return decorator

    def run(self, address):
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                status_code, content = 404, ""
                try:
                    if self.path in Website.my_handlers:
                        current_handler = Website.my_handlers[self.path]
                        status_code = current_handler()[0]
                        content = current_handler()[1]
                    else:
                        for regex, handler in Website.my_handlers.items():
                            if self.path == "/" or self.path.startswith('/users/'):
                                match = re.match(regex, self.path)
                                if match:
                                    status_code = handler(*match.groups())[0]
                                    content = handler(*match.groups())[1]
                except Exception as e:
                    self.send_response(404)
                    raise e
                finally:
                    self.send_response(status_code)
                    self.end_headers()
                    self.wfile.write(bytes(content, 'utf-8'))

        httpd_server = http.server.HTTPServer(address, Handler)
        httpd_server.serve_forever()


