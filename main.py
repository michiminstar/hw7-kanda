#!/usr/bin/env python
import urllib2
from flask import request, Flask
from google.appengine.api import urlfetch

app = Flask(__name__)

@app.route('/')
def index():
	return 'Type "convert?message=" to the url and add some words at the end.'
	
@app.route('/convert')
def convert():
	message = request.args.get('message')
	return 'awesome ' + message + ' !'

@app.route('/show')
def show():
	print 'Welcome'
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

# @app.route('/getword')
# def getword():
# 	pos = request.args.get('message')
# 	params = {
# 		'noun1':'dog'
# 	}
# 	return pos+ message

