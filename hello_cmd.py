from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line

define('port', default=4300, type=int, help='设置端口')
class Indexhandler(RequestHandler):
    def get(self):
        word = self.get_argument('wd')
        self.write('获取表单参数%s' % word)
    def post(self):
        word = self.get_argument('wd')
        self.write('获取表单参数%s' % word)

class Loginhandler(RequestHandler):
    def get(self):
        self.write('Login')

class Logouthandler(RequestHandler):
    def get(self):
        self.write('Logout')

if __name__ == '__main__':

    parse_command_line()

    app = Application([
        ('/', Indexhandler),
        ('/login', Loginhandler),
        ('/logout', Logouthandler)
    ])


    app.listen(options.port)

    IOLoop.current().start()
