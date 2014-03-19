from controller import Control
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json



#MEDIA_DIR = filehandler.readFile() 
CON = Control()
CON.start()
print "controls have been ran. IT IS ALIVE!!"



class MainHandler(tornado.web.RequestHandler):
    def get(request):
        class a:
            pass
        a.name = "Rylan"
        a.age = 1
        request.render("index.html", ry=a)
 
        
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
        CON.playsong("C:\\users\\rylan\\Music\\x.mp3")
        self.write_message("C:\\users\\rylan\\Music\\x.mp3")
        for i in range(10000):
        	print i
        CON.stop()

 
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
