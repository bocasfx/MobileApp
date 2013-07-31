import logging
import sqlite3
import sys
import os.path
import xml.etree.ElementTree as ET
from CSDict import CSDict


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

		try:
			self.sql_descriptor = self.parse_sql_descriptor('./sql/sql_descriptor.xml')
		except Exception as e:
			msg = "Error: Unable to parse SQL descriptor. " + str(e.args[0])
			print msg
			self.logger.error(msg)
			sys.exit(1)

	# ----------------------------------------------------------------------------------------

	def get_resource(self, resource, params):

		offset = None
		count = None
		sort = None
		orderby = None

		if (params == ""):
			return {}

		if (params.has_key('offset')):
			offset = params['offset'][0]

		if (params.has_key('count')):
			count = params['count'][0]

		if (params.has_key('sort')):
			sort = params['sort'][0]

		if (params.has_key('orderby')):
			orderby = params['orderby'][0]

		get_descriptor = self.sql_descriptor.get(resource).get('get')
		sql = get_descriptor.get('sql')
		fields = get_descriptor.get('fields').split(' ')

		if (sort is not None and orderby is not None):
			sql = sql + ' ORDER BY ' + str(orderby) + ' ' + str(sort)

		if (count is not None):
			sql = sql + ' LIMIT ' + str(count)

		if (offset is not None):
			sql = sql + ' OFFSET ' + str(offset)

		self.cursor.execute(sql)

		records = CSDict()
		idx = 0

		rows = self.cursor.fetchall()
		print rows

		for row in rows:
			# Create a dictionary with the fields
			j = 0
			for field in fields:
				records[idx][field] = row[j]
				print type(row[j])
				j += 1

			idx += 1

		return records

	# ----------------------------------------------------------------------------------------

	def post_resource(self, resource, data):

		if (not data.has_key('name')):
			raise Exception("Missing parameter 'name'.")

		if (not data.has_key('lastname')):
			raise Exception("Missing parameter 'lastname'.")
		
		# TODO
		sql = self.sql_descriptor.get(resource).get('get').get('sql')

		print 'SQL: ' + sql

		self.cursor.execute(sql)
		self.connection.commit()

		return

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

	# ----------------------------------------------------------------------------------------
	
	def parse_sql_descriptor(self, descriptor_file):
		tree = ET.parse(descriptor_file)
		root = tree.getroot()

		resources = root.findall('./')

		items = {}

		for resource in resources:

			get_node = resource.find('./get')
			get_sql = get_node.text
			get_fields = get_node.get('fields')

			post_node = resource.find('./post')
			post_sql = post_node.text
			post_vars = post_node.get('vars')

			var_list = post_vars.split(' ')

			items[resource.tag] = {
				'get': {
					'sql': get_sql,
					'fields': get_fields
				},
				'post': {
					'sql': post_sql,
					'vars': var_list
				}
			}

		return items
