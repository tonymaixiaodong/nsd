#!/usr/bin/env python
import time

def application (environ, start_response):
  response_body = 'UNIX EPOCH time is now: %s\n' % time.time()
  status = '200 OK'
  response_headers = [('Content-Type', 'text/plain'),
                      ('Content-Length', '1'),
                      ('Content-Length', str(len(response_body)))]
  start_response(status, response_headers)
  return [response_body]
