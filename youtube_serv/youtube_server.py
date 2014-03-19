import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
import yss
from searchops import Option

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		terms = self.get_arguments('searchterms', None)
		ops = Option()
		ops.q = terms
		ops.max_results = 9
		youtube_json = yss.youtube_search(ops)
		self.write(json.dumps(youtube_json))
class MHandler(tornado.web.RequestHandler):
	def get(request):
		request.render("index.html")
		
        

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/w", MHandler)
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8000, address='192.168.0.103')
    tornado.ioloop.IOLoop.instance().start()
