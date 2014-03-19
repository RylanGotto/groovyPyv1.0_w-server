import os
import json
from django.http import *
from django.shortcuts import render
from utilities import filehandler
from controller import Control
from utilities import local_search
from utilities import get_tube


#clearstatic.clearStatic() 
MEDIA_DIR = filehandler.readFile() 
Con = Control()
Con.start()
print "controls ran"

def my_homepage_view(request):
    return render(request, 'default.html')

def homepage(request):
		global Con
		audio = local_search.get_filepaths(MEDIA_DIR)
   	 	return render(request, 'searchForm.html', {'al':audio})


def musicSet(request):
	x = 0
	return render(request, 'musicSet.html', {'x':x})


	
def ajax2(request):
	global MEDIA_DIR, Con
	response_dict = {}        
	MEDIA_DIR = request.POST['filep']     
	filehandler.writeFile(MEDIA_DIR)    
	response = "Media Directory saved as '" + MEDIA_DIR + "'" 
	Con.loadDB(MEDIA_DIR)                      
	response_dict.update({'server_response': response })                                                               
	return HttpResponse(json.dumps(response_dict), content_type='application/javascript')


def ajax3(request):
	global Con
	response_dict = {}        
	fp = request.POST['filep'] 
	Con.playsong(fp)
	response = "Media Directory saved as '" + fp + "'"             
	response_dict.update({'server_response': response })                                                               
	return HttpResponse(json.dumps(response_dict), content_type='application/javascript')

def ajax4(request):
	global Con
	Con.pause()

def ajax5(request):
	global Con
	Con.unpause()                                                             


def ajax6(request):
	response_dict = {}        
	fp = request.POST['filep'] 
	xx = get_tube.get_from_tube(fp)
	response_dict = [{'iframe':xx[0]}]                                           
	return HttpResponse(json.dumps(response_dict), content_type='application/javascript')