import http.server
import socketserver
import os
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Yinghun Online Test at http://127.0.0.1:{PORT}")
    httpd.serve_forever()