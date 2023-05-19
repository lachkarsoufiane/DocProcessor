from interface.IFormatter import IFormatter
from collections import namedtuple
import json

class TableDSCCFormatterStrategy(IFormatter):
    
    def format(content):
        content = json.loads(content)
        table = namedtuple('table', 'Document Description URL')
        order_table = []

        for column in content:
            document = column["Document"]
            description = column["Description"]
            url = column["URL"]
            order_table.append(table(document, description, url))
        return order_table