import sqlite3
import sys


class DataManager():

	records = {}
	index = 0
	connection = None
	cursor = None

	def __init__(self):
		try:
			self.connection = sqlite3.connect('server.db')
			self.cursor = self.connection.cursor()
		except sqlite3.error, e:
			print "Error %s:" % e.args[0]
			sys.exit(1)

	def get_records(self):
		sql = "SELECT name, lastname FROM names"
		self.cursor.execute(sql)

		records = {}
		idx = 0

		while True:
			row = self.cursor.fetchone()
			if row == None:
				break
			records[idx] = {'name' : row[0], 'lastname' : row[1]}
			idx += 1
		
		return records

	def set_record(self, data):
		print "Saving record " + str(self.index)
		self.records[self.index] = data
		self.index += 1