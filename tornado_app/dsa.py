from controller import Control
from util import splitstr
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
import local_search



#MEDIA_DIR = filehandler.readFile() 
CON = Control()
CON.start()
print "Will not work with Internet Explorer use Chrome, or maybe firefox"



class MainHandler(tornado.web.RequestHandler):
    def get(request):
        request.render("index.html")
 
        
class PauseHandler(tornado.web.RequestHandler):
	def get(self):
		print "pause"
		if CON.isPaused() == 1:
			CON.unpause()
		else:
			CON.pause()
    
        
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "connected"
      
    def on_message(self, message):
    	ins = json.loads(message)
    	videos = []
    	mp3s = []
    	x = {}
    	if int(ins['type']) == 0:
	    	for i in CON.getson(ins['data']):
	        	videos.append({'title':i[0],'thumbnail':i[1],'url':i[2]})
			x.update({'type':'search_response', 'data':videos})
            self.write_message("hello")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/ws', WSHandler)
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()