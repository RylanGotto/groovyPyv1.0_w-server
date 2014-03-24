from controller import Control
from util import splitstr
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
from util import local_search


# MEDIA_DIR = filehandler.readFile()
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
        x = {'type': 'ignore', 'data': ''}
        print message
        if int(ins['type']) == 0:
            for i in CON.getson(ins['data']):
                videos.append({'title': i[0], 'thumbnail': i[1], 'url': i[2]})
            mp3s = [local_search.search_filenames(
                ins['data'], "C:\\users\\rylan\\music")]
            x.update(
                {'type': 'search_response', 'data': {'youtube': videos, 'mp3': mp3s}})
           
        elif int(ins['type']) == 1:
            print ins['data']

        elif int(ins['type']) == 2:
            if ins['data'][:1].lower() == 'c':
                print ins['data']
                CON.playsong(ins['data'])
            else:
                x.update({'type': 'url_change', 'data': ins['data']})
        elif int(ins['type']) == 8:
            if CON.isPaused() == 1:
                CON.unpause()
            else:
                CON.pause()
                
        elif int(ins['type']) == 9:
            CON.stop()
        self.write_message(x)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r'/ws', WSHandler)
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
