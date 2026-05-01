import http.server
import socketserver
import os

os.chdir('/Users/varrel/Documents/site')

PORT = int(os.environ.get('PORT', 8099))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
