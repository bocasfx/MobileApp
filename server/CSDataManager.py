import logging
import sqlite3
import sys
import os.path


class CSDataManager():

	records = {}
	index = 0
	connection = None
	cursor = None

	# ----------------------------------------------------------------------------------------

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

	def get_records(self, params):

		offset = None
		count = None
		sort = None

		if (params.has_key('offset')):
			offset = params['offset'][0]

		if (params.has_key('count')):
			count = params['count'][0]

		if (params.has_key('sort')):
			sort = params['sort'][0]

		sql = '							\
			select 						\
				name as name, 			\
				lastname as lastname 	\
				FROM names'

		if (sort is not None):
			sql = sql + ' ORDER BY name ' + str(sort)

		if (count is not None):
			sql = sql + ' LIMIT ' + str(count)

		if (offset is not None):
			sql = sql + ' OFFSET ' + str(offset)

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

	def post_record(self, data):

		if (not data.has_key('name')):
			raise Exception("Missing parameter 'name'.")

		if (not data.has_key('lastname')):
			raise Exception("Missing parameter 'lastname'.")

		name = data['name'][0]
		lastname = data['lastname'][0]

		sql = "INSERT INTO names VALUES (\'" 
		sql += str(name) 
		sql += "\', \'" 
		sql += str(lastname) 
		sql += "\');"

		print 'SQL: ' + sql

		self.cursor.execute(sql)
		self.connection.commit()

		return

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
