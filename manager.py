import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class Indexhandler(tornado.web.RequestHandler):
    def get(self):
        # 请求读取参数
        wd = self.get_argument('wd')
        title = self.get_argument('title')
        # 从查询参数中读取URL参数
        wds = self.get_query_arguments('wd')
        print(wds)
        titles = self.get_query_arguments('titles')
        print(titles)
        # 从请求对象中读取参数
        req: HTTPServerRequest = self.request

    def get(self):
        self.write('<h3>我是get请求</h3>')
    def post(self):
        self.write('<h3>我是post请求</h3>')

        self.write('<h3>我的主页</h3>')

class SearchHandler(tornado.web.RequestHandler):
    mapper = {
        'python': '流行AI语言',
        'java': '主流语言',
        'h5': 'html5'
    }
    def get(self):
        html = """
            <h3>搜索%s结果<h3>
            <p>
                %s
            </p>
        """
        wd = self.get_query_arguments('wd')
        result = self.mapper.get(wd)

def make_app():
    return tornado.web.Application([
        ('/', Indexhandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(5400)

    print('starting web server http://localhost:5400')
    tornado.ioloop.IOLoop.current().start()