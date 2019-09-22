from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = 5350

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "reboot" in self.path:
            self.send_response(200)
            self.end_headers()
            os.system("reboot now") 
        elif "shutdown" in self.path:
            self.send_response(200)
            self.end_headers()
            os.system("shutdown now") 
        else:
            self.send_response(200)
            self.end_headers()

httpd = HTTPServer(("", PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
