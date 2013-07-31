import logging
import logging.handlers
from CSDataManagerImpl import CSDataManagerImpl
from BaseHTTPServer import HTTPServer
from CSRequestHandler import CSRequestHandler
import argparse


class CSHTTPServer(HTTPServer):
    """this class is necessary to allow passing the CSDataManager object into
       the RequestHandlerClass"""
    def __init__(self, server_address, RequestHandlerClass, dataManager):
        HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.dataManager = dataManager


def initialize_logger(log_level='error'):
    
    max_bytes = 5242880
    backup_count = 5
    log_name = 'server.log'

    logger = logging.getLogger('http_server')
    logger.setLevel(logging.DEBUG)
    
    fileHandler = logging.handlers.RotatingFileHandler(log_name, maxBytes=max_bytes, backupCount=backup_count)

    level = {
        'error': logging.ERROR,
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN
    }.get(log_level, logging.DEBUG)

    fileHandler.setLevel(level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fileHandler)

# ----------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='HTTP server')

    parser.add_argument('--port',
        default='8080',
        help='Listening port for HTTP server',
        type=int)

    parser.add_argument('--ip',
        default='127.0.0.1',
        help='HTTP server IP')

    parser.add_argument('--loglevel',
        default='error',
        help='Sets the log level. Options are "error", "warn", "info", "debug"')

    args = parser.parse_args()

    initialize_logger(args.loglevel)

    dataManager = CSDataManagerImpl()

    server_address = (args.ip, args.port)
    httpd = CSHTTPServer(server_address, CSRequestHandler, dataManager)
    print 'HTTP server running...'
    httpd.serve_forever()

# ----------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
