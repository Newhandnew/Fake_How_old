##import BaseHTTPServer
##
##class handler(BaseHTTPServer.BaseHTTPRequestHandler): pass
##handler.do_GET = lambda x: x.wfile.write('Hello world')
##BaseHTTPServer.HTTPServer(('', 8000), handler).serve_forever()
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

import cgi
import os
import facedetect

class StoreHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['content-length'])
        print length
        if length > 10000000:
            print "file to big"
            read = 0
            while read < length:
                read += len(self.rfile.read(min(66556, length - read)))
            self.respond("file to big")
            return
        else:
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                         })
            data = form['file'].file.read()
            open("test.jpg", "wb").write(data)
            #call facedetect
            facedetect.facedetect()
            #show result
            img = open("result.png", "rb")
            self.imgrespond(img.read())
            img.close()
            

    def do_GET(self):
        response = """
        <html><body>
        <form enctype="multipart/form-data" method="post">
        <p>File: <input type="file" name="file"></p>
        <p><input type="submit" value="Upload"></p>
        </form>
        </body></html>
        """        

        self.respond(response)

    def respond(self, response, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response)  

    def imgrespond(self, response, status=200):
        self.send_response(status)
        self.send_header("Content-type", "image/png")
        #self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response)  

port = int(os.environ.get("PORT", 5000))
server = HTTPServer(('0.0.0.0', port), StoreHandler)
server.serve_forever()
