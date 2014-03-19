import re
import requests


def get_from_tube(search_terms):
	form_field = {'s':search_terms}
	response = requests.get("http://iamrylangotto.com:8000/results", params = form_field)
	output  = re.compile('<p>(.*?)</p>', re.DOTALL |  re.IGNORECASE).findall(response.text)
	urls = []
	for i in output:
		url = "http://www.youtube.com/embed/%s"%(i)
		urls.append(url)
	return urls