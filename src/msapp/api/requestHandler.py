from http.server import BaseHTTPRequestHandler

from msapp.domain.service import RecipeService

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = "Hello World!"
        # Prepare response from recipe service.
        if not '/favicon.ico' == self.path:
            rs = RecipeService()
            resp = rs.serve(self.path)
            response = resp if type(resp) is str and len(resp) > 0 else response
        # Send response to browser.
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
