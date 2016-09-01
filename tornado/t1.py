__author__ = '0138695'
import tornado
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",list_info=[11,22,33])

class LoginHanler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Hello, world")
        self.finish()

application = tornado.web.Application([
    (r'/',MainHandler),
    (r'/login',LoginHanler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()