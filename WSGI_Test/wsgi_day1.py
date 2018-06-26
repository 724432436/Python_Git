from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<b>hello world!</b>']

server = make_server('',8080,application)
print('port 8080 is start.....')
server.serve_forever()