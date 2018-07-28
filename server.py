#!/usr/bin/python
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from os import curdir, sep


class MessageHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        # 1. How long was the message? (Use the Content-Length header.)

        # 2. Read the correct amount of data from the request.

        # 3. Extract the "message" field from the request data.

        # Send the "message" field back as the response.

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        try:
            sendReply = False
            if self.path.endswith('.html'):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith('.jpg'):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith('.gif'):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith('.js'):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith('.css'):
                mimetype = 'text/css'
                sendReply = True
            if sendReply == True:
                f = open(curdir + sep + self.path)
                print(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read().encode())
                f.close()
            return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

if __name__ == '__main__':
    try:
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, MessageHandler)
        print ('Started httpserver on port 8000')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(' received, shutting down the web server')
        httpd.socket.close()


			