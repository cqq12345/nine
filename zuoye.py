#!/usr/bin/env python
import os

import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line, define, options

define("host", default='0.0.0.0', help="主机地址", type=str)
define("port", default=8000, help="主机端⼝", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("hello world")

        self.render('zuoyeeee.html')

class AifeiHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("大熊牛逼")
        # title = self.get_argument('title', 'hsj')
        # content = self.get_argument('content', 'hsj')
        #
        # self.render('zuoyee.html', title=title, content=content)

class TestPostHandler(tornado.web.RequestHandler):
    def get(self):
        name=self.get_argument('name')
        self.wirte("%s dsjh" %name)

class TestPostHandler(tornado.web.RequestHandler):
    def get(self):
        html=
        self.write("%s dansn" % name)
        def post(self):
            pass


class XiongdaHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("胸大牛逼")


def make_app():
    routes = [
        (r'/a', MainHandler),
        (r'/foo', AifeiHandler),
        (r'/bar', XiongdaHandler),

    ]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, 'templates')
    static_path = os.path.join(base_dir, 'statics')
    return tornado.web.Application(routes, template_path=template_path,
                                   static_path=static_path, debug=True)  # debug=True 可以保持连接不断

    # ( 绑定路由，可以 按照正则表达式匹配)


if __name__ == "__main__":
    parse_command_line()

    app = make_app()
    app.listen(8000)
    loop = tornado.ioloop.IOLoop.current()
    loop.start()
