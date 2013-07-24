from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import threading
import argparse
import re
import urlparse
import cgi
import logging
import json
from DataManager import DataManager
 
class HTTPRequestHandler(BaseHTTPRequestHandler):

	dataManager = DataManager()
 
	def do_POST(self):
		logging.debug('POST hanlder.')
		if re.search('/api/v1/records', self.path) != None:
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if re.search('application/json, application/x-www-form-urlencoded', ctype):
				length = int(self.headers.getheader('content-length'))
				data = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)
				self.dataManager.set_record(data)
				logging.info('Record has been added successfully')
			else:
				data = {}
 
			self.send_response(200)
			self.end_headers()
		else:
			self.send_response(403)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()
 
		return
 
	def do_GET(self):
		logging.debug('GET handler.')
		if None != re.search('/api/v1/records', self.path):
			records = self.dataManager.get_records()
			if ( records != {} ):
				self.send_response(200)
				self.send_header('Content-Type', 'text/html')
				self.end_headers()
				self.wfile.write(json.dumps(records))
			else:
				self.send_response(400, 'Bad Request: record does not exist')
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
		else:
			self.send_response(403)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()
 
		return
 
 
if __name__=='__main__':
	logging.basicConfig(filename='example.log',level=logging.DEBUG)
	parser = argparse.ArgumentParser(description='HTTP Server')
	parser.add_argument('port', type=int, help='Listening port for HTTP Server')
	parser.add_argument('ip', help='HTTP Server IP')
	args = parser.parse_args()


	server_address = (args.ip, args.port)
	httpd = HTTPServer(server_address, HTTPRequestHandler)
	print 'HTTP Server Running...........'
	httpd.serve_forever()
 
	
