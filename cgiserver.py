#!/usr/bin/env python3

from http.server import CGIHTTPRequestHandler, HTTPServer

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default
server = HTTPServer(('localhost', 8080), handler)
server.serve_forever()