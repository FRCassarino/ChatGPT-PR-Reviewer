from http.server import HTTPServer
from request_handler import RequestHandler

server = HTTPServer(('localhost', 8000), RequestHandler)
server.serve_forever()


