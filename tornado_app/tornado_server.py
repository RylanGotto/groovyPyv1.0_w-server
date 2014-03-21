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
        response = splitstr.split(message)
        instruc = response.get('instruction') 
        terms = response.get('terms')
        youtube_d = {}
        localmusic_d = {}
        i = 0
        if int(instruc) == 0:
            for i in CON.getson(terms):
                title = i[0]
                thumbnail = i[1]
                videoUrl = "http://www.youtube.com/embed/" + i[2] 
                youtube_d.update({'type': 0, 'title':title, 'thumbnail':thumbnail, 'videoUrl':videoUrl})
                self.write_message(json.dumps(youtube_d))
            names = local_search.search_filenames(terms, "C:\\users\\rylan\\music")
            for key, value in names.items():
                path = key
                title = value
                localmusic_d.update({'type': 1, 'path':path, 'title2':title})
                self.write_message(json.dumps(localmusic_d))
        if int(instruc) == 1:
            print terms
                


               
           
                


            
        
       


 
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
