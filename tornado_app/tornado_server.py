from controller import Control
from util import splitstr
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json



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
        response = splitstr.split(message)
        instruc = response.get('instruction') 
        terms = response.get('terms')
        youtube_d = {}
        if int(instruc) == 0:
            for i in CON.getson(terms):
                title = i[0]
                videoUrl = "http://www.youtube.com/embed/" + i[1]
                thumbnail = i[2]
                youtube_d.update({'type': 0, 'title':title, 'videoUrl':videoUrl, 'thumbnail':thumbnail})
                self.write_message(json.dumps(youtube_d))

               
           
                


            
        
       


 
    def on_close(self):
      print 'connection closed'

    

 
 
application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/ws', WSHandler),
    (r'/pause', PauseHandler)
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
