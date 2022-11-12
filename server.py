# Python 3 server example
import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket


config = ('0.0.0.0', 8080)
# My ISP doesn't support IPV6 :(
# config = ('::', 8080)
# class HTTPServerV6(HTTPServer):
#     address_family = socket.AF_INET6


class server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        try:
            conn = http.client.HTTPConnection('ifconfig.me')
            conn.request('GET', '/ip')
            self.wfile.write(conn.getresponse().read())
        except Exception as e:
            print(e)
        finally:
            conn.close()

if __name__ == "__main__":        
    # webServer = HTTPServerV6(config, MyServer)
    web_server = HTTPServer(config, server)
    print('Server started http://%s:%s' % config)

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
