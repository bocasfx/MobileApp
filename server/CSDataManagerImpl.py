import logging
from CSDict import CSDict
from CSDataManager import CSDataManager


class CSDataManagerImpl(CSDataManager):

    logger = logging.getLogger('http_server.data_manager_impl')

    def __init__(self, *args):
        CSDataManager.__init__(self, *args)

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

    
    
