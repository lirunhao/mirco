from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class Indexhandler(RequestHandler):
    def get(self):
        # 向客户端响应数据
        self.write('<h3>翻滚吧！阿信</h3>')

if __name__ == '__main__':
    # 创建web应用
    app = Application([
        ('/', Indexhandler)
    ])
    # 绑定端口
    app.listen(5500)

    # 启动服务
    print('start http://localhost:%s' % 5500)

    IOLoop.current().start()