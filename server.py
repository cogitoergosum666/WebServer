from http.server import BaseHTTPRequestHandler, HTTPServer
import os
#python3已经将BaseHTTPServer合并到http.server

class ServerException(Exception):
    '''服务器内部错误'''
    pass

class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page = '''\
        <html>
        <body>
        <p>Hello, web!BJTUCIT20281274</p>
        </body>
        </html>
    '''

    
    # 处理一个GET请求
    def do_GET(self):
        #self.send_error(404,'test message')#测试出错信息
        try:
            full_path = os.getcwd()+self.path#cwd返回当前路径
            if not os.path.exists(full_path):#如果当前目录下找不到该文件
                self.send_error(888,"'{0}' not found".format(self.path),'测试数据，吉祥如意！')
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
            else:
                #抛出异常：该路径为不知名对象
                raise ServerException("Unknown object '{0}'".format(self.path))
        except Exception as msg:
            self.handle_error(msg)

        # self.send_response(200)
        
        # self.send_header("Content-Type", "text/html")
        # self.send_header("Content-Length", str(len(self.Page)))
        # print(len(self.Page))
        # self.end_headers()
        # self.wfile.write(self.Page.encode('utf-8'))
    def send_content(self,content,status=200):
        self.send_response(status)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def handle_file(self,full_path):
        try:
            with open(full_path,'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"),404)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)

    server.serve_forever()

