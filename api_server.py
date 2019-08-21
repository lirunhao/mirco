import json
import uuid

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler
from tornado.options import options, define, parse_command_line


class LoginHandler(RequestHandler):
    users = [{
        'id': 1,
        'name': 'Ryon',
        'pwd': '123',
        'last_login_device': 'ios12.4'
    }]

    def get(self):
        # 读取json数据
        bytes = self.request.body
        print(bytes)
        print(self.request.headers.get('Content-Type'))

        # 从请求头中读取请求上传的数据类型（body的数据类型）
        content_type = self.request.headers.get('Content-Type')
        if content_type.startswith('application/json'):
            # self.write('upload json ok')
            json_str = bytes.decode('utf-8')
            # 反序列化
            json_data = json.loads(json_str)


            resp_data = {}
            login_user = None
            # 查询用户名和口令是否正确
            for user in self.users:
                if user['name'] == json_data['name']:
                    if user['pwd'] == json_data['pwd']:
                        login_user = user
                        break

            if login_user:
                resp_data['msg'] = 'success'
                resp_data['token'] = uuid.uuid4().hex
            else:
                resp_data['msg'] = '查无此用户'

            self.write(resp_data) # write()函数可接收str, dict, list
            self.set_header('Content-Type', 'application/json')
        else:
            self.write('upload data 必须是json格式')

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


def make_app():
    return Application(
        handlers=[
        ('/user', LoginHandler),
    ],
    default_host=options.h)

if __name__ == '__main__':
    # 定义命令行参数
    define('p', default=8000, type=int, help='绑定的port端口')
    define('h', default='localhost', type=str, help='绑定主机ip')
    # 解析命令行参数
    parse_command_line()

    app = make_app()
    app.listen(options.p)
    print('Runnig http://%s:%s' % (options.h, options.p))

    IOLoop.current().start()