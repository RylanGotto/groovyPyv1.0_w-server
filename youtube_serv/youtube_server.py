import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
import yss
from searchops import Option
import requests

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		terms = self.get_arguments('searchterms', None)
		pay = {'q':terms, 'part':'snippet', 'type':'video', 'key':"AIzaSyAA9qq8WQv7m_l3uwmejZfc1BqPAqjOdeM"}
		youtube_json = requests.get("https://www.googleapis.com/youtube/v3/search", params=pay).json()
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
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()




