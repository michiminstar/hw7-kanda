#!/usr/bin/env python
# code U
import urllib2
from flask import request, Flask
from google.appengine.api import urlfetch

app = Flask(__name__)




@app.route('/show')
def show():
	url = "http://step-test-krispop.appspot.com/"
	try:
	  result = urlfetch.fetch(url)
	  return result.content
	except urllib2.URLError, e:
	  handleError(e)	

#	message = request.args.get('message')
#	url = request.url_root + "convert?message=" + message
#	print(url)
#	response = requests.get(url).content
#	print(response)
#	return response.decode()

@app.route('/convert')
def convert():
	print "Hello!"
	message = request.args.get('message')
	return 'awesome ' + message + ' !'

