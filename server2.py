
from http.server import BaseHTTPRequestHandler, HTTPServer
#python3已经将BaseHTTPServer合并到http.server
class MyRequestHandler(BaseHTTPRequestHandler):
    # def send_error(code,message = None, explain = None):
    #     pass
    def printname():
        print("server2 activating")

def run(server_class=HTTPServer, handler_class=MyRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    #myhandler  = MyRequestHandler()
    #handler_class.send_error(server_class.RequestHandlerClass, code = 404)
    httpd.serve_forever()


def main():
    print('main')
    run()
if __name__ == '__main__':
    main()