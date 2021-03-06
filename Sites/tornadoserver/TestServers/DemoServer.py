#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     DemoServer.py
#
#     https://www.tornadoweb.org
#
#     Testing available parameters on the url page call.
#     This example server shows how different paths (detected by regular expressions)
#     are connected to different handlers, ranging from a simple request, reading a static 
#     html page file, getting specific URL arguments (http://localhost:8886/query/aaa?n=100)
#     or disassembling the URL path by regular expressions.
#     This means that "parts" of the site can use different handlers than other parts.
#
#     http://localhost:8889
#     http://localhost:8889/blog
#     http://localhost:8889/query?n=100
#     http://localhost:8889/query/aaa?n=100
#     http://localhost:8889/resource/1234
#     http://localhost:8889/resource/abcd-200/xyz-100

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

PORT = 8889

class BasicRequestHandler(RequestHandler):
    def get(self):
        self.write('Hello, world')

"""
class StaticRequestHandler(RequestHandler):
    def get(self):
        self.render('templates_html/index.html')

class QueryRequestHandler(RequestHandler):
    def get(self):
        n = self.get_argument('n')
        self.write('Argument is "%s"' % n)

class ResourceRequestHandler(RequestHandler):
    def get(self, id):
        self.write('<h2>Querying path with id "%s"</h2>' % id)

class PathRequestHandler(RequestHandler):
    def get(self, *args):
        for arg in args:
            self.write('<h2>Querying path item "%s"</h2>' % arg)
"""
if __name__ == '__main__':
    requestHandler = [
        ('/', BasicRequestHandler), # http://localhost:8889
        #('/blog', StaticRequestHandler), # http://localhost:8889/blog
        #('/query', QueryRequestHandler), # http://localhost:8889/query?n=100
        #('/query/aaa', QueryRequestHandler), # http://localhost:8889/query/aaa?n=100
        #('/resource/([0-9]+)', ResourceRequestHandler), # http://localhost:8889/resource/1234
        #('/path/([A-Za-z0-9-]+)/([A-Z,a-z,0-9-]+)', PathRequestHandler), # http://localhost:8889/path/aaa/bbb
    ]
    app = Application(requestHandler)
    app.listen(PORT)
    print('Server on port', PORT)
    IOLoop.current().start()
