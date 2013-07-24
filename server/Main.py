import logging
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from CSDataManager import CSDataManager
import argparse
import re
import urlparse
import cgi
import logging.handlers
import json

 
class CSRequestHandler(BaseHTTPRequestHandler):

	dataManager = CSDataManager()
	logger = logging.getLogger('http_server')
 
	def do_POST(self):
		self.logger.debug('POST hanlder.')
		if re.search('/api/v1/records', self.path) != None:
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if re.search('application/json, application/x-www-form-urlencoded', ctype):
				length = int(self.headers.getheader('content-length'))
				data = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)
				self.dataManager.set_record(data)
				self.logger.info('Record has been added successfully')
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
		self.logger.debug('GET handler.')
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

def main():

	initialize_logger()

	parser = argparse.ArgumentParser(description='HTTP Server')

	parser.add_argument('--port', 		default='8080', 		help='Listening port for HTTP Server', type=int)
	parser.add_argument('--ip', 		default='127.0.0.1', 	help='HTTP Server IP')
	
	args = parser.parse_args()
	
	server_address = (args.ip, args.port)
	httpd = HTTPServer(server_address, CSRequestHandler)
	print 'HTTP Server Running.'
	httpd.serve_forever()

def initialize_logger():
	# create logger with 'spam_application'
	logger = logging.getLogger('http_server')
	logger.setLevel(logging.DEBUG)
	# create file handler which logs even debug messages
	fh = logging.FileHandler('server.log')
	fh.setLevel(logging.DEBUG)
	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)
 
if __name__=='__main__':
	main()
 
	
