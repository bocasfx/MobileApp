import logging
import sqlite3
import sys
import os.path


class CSDataManager():

    records = {}
    index = 0
    connection = None
    cursor = None
    logger = logging.getLogger('http_server.data_manager')
    sql_descriptor = None

    # ----------------------------------------------------------------------------------------

    def __init__(self, *args):

        try:
            self.logger.debug('Connecting to database.')
            self.connection = sqlite3.connect('server.db')
            self.logger.debug('Database connection established.')
        except Exception as e:
            msg = "Error: Unable to connect to database. " + str(e.args[0])
            print msg
            self.logger.error(msg)
            sys.exit(1)

        try:
            self.cursor = self.connection.cursor()

            sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='init';"
            self.cursor.execute(sql)
            if (self.cursor.fetchone() is None):
                self.init_database()
        except Exception as e:
            self.connection.close()
            msg = "Error: Unable to initialize data manager. " + str(e.args[0])
            print msg
            self.logger.error(msg)
            sys.exit(1)

    # ----------------------------------------------------------------------------------------

    def get_resource(self, resource, params):

        raise Exception("Method must be overriden")

    # ----------------------------------------------------------------------------------------

    def post_resource(self, resource, data):

        raise Exception("Method must be overriden")

    # ----------------------------------------------------------------------------------------

    def init_database(self):
        self.logger.debug('Initializing database.')
        sql = self.load_file('sql/create_db.sql').split('\n')

        self.cursor.execute('begin')

        for statement in sql:
            self.logger.debug('Executing statement: ' + str(statement))
            self.cursor.execute(statement)

        self.connection.commit()

        self.logger.debug('Database initialization complete.')

    # ----------------------------------------------------------------------------------------

    def load_file(self, file_name):
        if (os.path.isfile(file_name) is False):
            msg = 'Unable to find database script: ' + str(file_name)
            print msg
            self.logger.error(msg)
            sys.exit(1)

        try:
            f = open(file_name)
            with f:
                data = f.read()
                return data
        except IOError as e:
            msg = "Error: Unable to read sql script " + str(file_name) + ". " + str(e.args[0])
            print msg
            self.logger.error(msg)
            sys.exit(1)
