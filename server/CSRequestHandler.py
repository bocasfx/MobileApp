from BaseHTTPServer import BaseHTTPRequestHandler
from CSDataManager import CSDataManager
import urlparse
import cgi
# import logging.handlers
import json
import sqlite3


class CSRequestHandler(BaseHTTPRequestHandler):

	dataManager = CSDataManager()
	# logger = logging.getLogger('http_server')

	# ----------------------------------------------------------------------------------------------

	def do_GET(self):
		
		path = self.path.split('?')
		url = path[0]
		params = urlparse.parse_qs(path[1])
		
		# Reject invalid urls
		if (self.url_is_valid(url) is False):
			self.cs_response(403, 'Invalid URL')
			return

		try:
			# Get records from data manager
			records = self.dataManager.get_records(params)
		except sqlite3.Error as e:
			self.cs_response(500, 'Internal server error: ' + str(e.args[0]), 'text/html')
			return

		# Status 200 OK
		self.cs_response(200, '', 'text/html')
		self.wfile.write(json.dumps(records))
		return

	# ----------------------------------------------------------------------------------------------

	def do_POST(self):

		path = self.path.split('?')
		url = path[0]
		
		# Reject invalid urls
		if (self.url_is_valid(url) is False):
			self.cs_response(403, 'Invalid URL')
			return
		
		# Get content type
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

		# Validate content type
		if (self.ctype_is_valid(ctype) is False):
			self.cs_response(415, 'Unsupported Media Type')
			return

		# POST the data
		length = int(self.headers.getheader('content-length'))
		data = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)

		try:
			self.dataManager.post_record(data)
		except Exception as e:
			self.cs_response(400, 'Bad request: ' + str(e.args[0]), 'text/html')
			return

		# self.logger.info('Record has been added successfully')
		

		self.send_response(200)
		self.end_headers()

		return

	# ----------------------------------------------------------------------------------------------
	
	def do_PUT(self):
		print "----- SOMETHING WAS PUT!! ------"
		print self.headers
		length = int(self.headers['Content-Length'])
		content = self.rfile.read(length)
		self.send_response(200)
		print content

	# ----------------------------------------------------------------------------------------------
	
	def do_DELETE(self):
		pass

	# ----------------------------------------------------------------------------------------------

	def cs_response(self, code, message, content_type='application/json'):
		# self.logger.debug('cs_response: ' + str(code) + ' ' + str(message))
		self.send_response(code, message)
		self.send_header('Content-Type', content_type)
		self.end_headers()

	# ----------------------------------------------------------------------------------------------
	
	def url_is_valid(self, url):
		return {
			'/api/v1/records' : True
		}.get(url, False)

	# ----------------------------------------------------------------------------------------------

	def ctype_is_valid(self, ctype):
		return {
			'application/json, application/x-www-form-urlencoded' : True
		}.get(ctype, False)