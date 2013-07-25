import logging
from BaseHTTPServer import HTTPServer
from CSRequestHandler import CSRequestHandler
import argparse


def initialize_logger():
	# create logger with 'spam_application'
	logger = logging.getLogger('http_server')
	logger.setLevel(logging.DEBUG)
	# create file handler which logs even debug messages
	fh = logging.FileHandler('server.log')
	fh.setLevel(logging.DEBUG)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(fh)

# ----------------------------------------------------------------------------------------------

def main():
	initialize_logger()

	parser = argparse.ArgumentParser(description='HTTP server')

	parser.add_argument('--port',
		default='8080',
		help='Listening port for HTTP server',
		type=int)

	parser.add_argument('--ip',
		default='127.0.0.1',
		help='HTTP server IP')

	args = parser.parse_args()
	server_address = (args.ip, args.port)
	httpd = HTTPServer(server_address, CSRequestHandler)
	print 'HTTP server running...'
	httpd.serve_forever()

# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()
