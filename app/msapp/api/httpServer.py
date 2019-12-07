import logging
from http.server import HTTPServer

from msapp.api import RequestHandler

class HttpServer:
    PORT = 8001

    def __init__(self):
        self._l = logging.getLogger(__name__)
        server = ('', HttpServer.PORT)
        self._httpd = HTTPServer(server, RequestHandler)

    def blockingRunner(self):
        self._httpd.serve_forever()
        # This method will never return.
