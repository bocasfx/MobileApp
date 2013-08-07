import logging
from CSDict import CSDict
from CSDataManager import CSDataManager


class CSDataManagerImpl(CSDataManager):

    logger = logging.getLogger('http_server.data_manager_impl')
    
    def __init__(self, *args):
        self.init_resources_dict()
        CSDataManager.__init__(self, *args)

    # ----------------------------------------------------------------------------------------
    
    def init_resources_dict(self):
        self.get_resources = CSDict()
        self.get_resources['records']['sql'] = 'SELECT ID, NAME, DESCRIPTION, PARENT_JOB_ID, SCOPE_ID from JOB'
        self.get_resources['records']['fields'] = ['ID', 'NAME', 'DESCRIPTION', 'PARENT_JOB_ID', 'SCOPE_ID']

        self.post_resources = CSDict()
        self.post_resources['records']['sql'] = "INSERT INTO JOB (ID, NAME, DESCRIPTION, PARENT_JOB_ID, SCOPE_ID) VALUES (?,?,?,?,?);"
        self.post_resources['records']['fields'] = ['ID', 'NAME', 'DESCRIPTION', 'PARENT_JOB_ID', 'SCOPE_ID']

    # ----------------------------------------------------------------------------------------

    def get_resource(self, resource, params):
        offset = None
        count = None
        sort = None
        orderby = None

        if ('offset' in params):
            offset = params['offset'][0]

        if ('count' in params):
            count = params['count'][0]

        if ('sort' in params):
            sort = params['sort'][0]

        if ('orderby' in params):
            orderby = params['orderby'][0]

        fields = self.get_resources[resource]['fields']
        sql = self.get_resources[resource]['sql']

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

        for row in rows:
            # Create a dictionary with the fields
            for field in fields:
                records[idx][field] = row[field]

            idx += 1

        return records
        
    # ----------------------------------------------------------------------------------------

    def post_resource(self, resource, data):

        param_list = []
        fields = self.post_resources[resource]['fields']
        for field in fields:
            if (field not in data):
                raise Exception("Missing parameter: " + str(field))
            param_list.append(data[field][0])
        
        sql = self.post_resources[resource]['sql']
        
        self.cursor.execute(sql, param_list)
        self.connection.commit()

        return
