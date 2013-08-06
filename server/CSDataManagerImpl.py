import logging
from CSDict import CSDict
from CSDataManager import CSDataManager


class CSDataManagerImpl(CSDataManager):

    logger = logging.getLogger('http_server.data_manager_impl')

    def __init__(self, *args):
        CSDataManager.__init__(self, *args)

    # ----------------------------------------------------------------------------------------

    def get_resource(self, resource, params):
        

        if (resource == 'records'):
            return self.get_records(params)

        return {}

    def get_records(self, params):

        offset = None
        count = None
        sort = None
        orderby = None

        if (params.has_key('offset')):
            offset = params['offset'][0]

        if (params.has_key('count')):
            count = params['count'][0]

        if (params.has_key('sort')):
            sort = params['sort'][0]

        if (params.has_key('orderby')):
            orderby = params['orderby'][0]

        fields = ['name', 'lastname']
        sql = 'SELECT name AS name, lastname AS lastname FROM names'

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

        # if (not data.has_key('name')):
        #     raise Exception("Missing parameter 'name'.")

        # if (not data.has_key('lastname')):
        #     raise Exception("Missing parameter 'lastname'.")
        
        # # TODO
        # sql = self.sql_descriptor.get(resource).get('get').get('sql')

        # print 'SQL: ' + sql

        # self.cursor.execute(sql)
        # self.connection.commit()

        # return
        pass

    
    
