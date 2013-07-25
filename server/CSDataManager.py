import logging
import sqlite3
import sys
import os.path


class CSDataManager():

    records = {}
    index = 0
    connection = None
    cursor = None

    def __init__(self):

        self.logger = logging.getLogger('http_server')

        try:
            # self.logger.debug('Connecting to database.')
            self.connection = sqlite3.connect('server.db')
            # self.logger.debug('Database connection established.')
        except Exception as e:
            msg = "Error: Unable to connect to database. " + str(e.args[0])
            print msg
            # self.logger.error(msg)
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
            # self.logger.error(msg)
            sys.exit(1)

    # ----------------------------------------------------------------------------------------

    def get_records(self):
        sql = "SELECT name, lastname FROM names"
        self.cursor.execute(sql)

        records = {}
        idx = 0

        while True:
            row = self.cursor.fetchone()
            if row is None:
                break
            records[idx] = {'name': row[0], 'lastname': row[1]}
            idx += 1

        return records

    # ----------------------------------------------------------------------------------------

    def set_record(self, data):
        # self.logger.debug( "Saving record " + str(self.index) )
        self.records[self.index] = data
        self.index += 1

    # ----------------------------------------------------------------------------------------

    def init_database(self):
        # self.logger.debug('Initializing database.')
        sql = self.read_sql_script('db.sql').split('\n')

        self.cursor.execute('begin')

        for statement in sql:
            # self.logger.debug('Executing statement: ' + str(statement))
            self.cursor.execute(statement)

        self.connection.commit()

        # self.logger.debug('Database initialization complete.')

    # ----------------------------------------------------------------------------------------

    def read_sql_script(self, script_name):
        if (os.path.isfile(script_name) is False):
            msg = 'Unable to find database script: ' + str(script_name)
            print msg
            # self.logger.error(msg)
            sys.exit(1)

        try:
            f = open(script_name)
            with f:
                data = f.read()
                return data
        except IOError as e:
            msg = "Error: Unable to read sql script " + str(script_name) + ". " + str(e.args[0])
            print msg
            # self.logger.error(msg)
            sys.exit(1)
