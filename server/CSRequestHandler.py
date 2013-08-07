from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import cgi
import logging.handlers
import json
import sqlite3


class CSRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, *args):
        self.logger = logging.getLogger('http_server.request_handler')
        BaseHTTPRequestHandler.__init__(self, *args)

    # ----------------------------------------------------------------------------------------------

    def do_GET(self):
        
        path = self.path.split('?')
        url = path[0]
        params = {}
        if (len(path) > 1):
          params = urlparse.parse_qs(path[1])
        resource = url.split('/')[-1]
        
        # Reject invalid urls
        if (self.url_is_valid(url) is False):
            self.cs_response(403, 'Invalid URL')
            return

        try:
            # Get records from data manager
            records = self.server.dataManager.get_resource(resource, params)
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
        resource = url.split('/')[-1]
        
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
            self.server.dataManager.post_resource(resource, data)
        except Exception as e:
            self.cs_response(400, 'Bad request: ' + str(e.args[0]), 'text/html')
            return

        self.logger.info('Record has been added successfully')
        
        self.send_response(200)
        self.end_headers()

        return

    # ----------------------------------------------------------------------------------------------
    
    def do_PUT(self):
        self.logger.debug("----- SOMETHING WAS PUT!! ------")
        self.send_response(200)

    # ----------------------------------------------------------------------------------------------
    
    def do_DELETE(self):
        self.logger.debug("----- SOMETHING WAS DELETED!! ------")
        self.send_response(200)

    # ----------------------------------------------------------------------------------------------

    def cs_response(self, code, message, content_type='application/json'):
        self.logger.debug('cs_response: ' + str(code) + ' ' + str(message))
        self.send_response(code, message)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    # ----------------------------------------------------------------------------------------------
    
    def url_is_valid(self, url):
        return {
            '/api/v1/records': True,
            '/api/v1/tests': True
        }.get(url, False)

    # ----------------------------------------------------------------------------------------------

    def ctype_is_valid(self, ctype):
        if (ctype == 'application/json, application/x-www-form-urlencoded'):
            return True
        return False

    # ----------------------------------------------------------------------------------------------

    def log_message(self, format, *args):
        message = ' '.join(map(str, args))
        self.logger.info( message )
        return