from interface.IFormatter import IFormatter
from collections import namedtuple
import json

class TableDSCCFormatterStrategy(IFormatter):
    
    def format(content, format = None):
        content = json.loads(content)
        columns = "Document Description URL"
        table = namedtuple('table', column)
        order_table = []

        for column in content:
            document = column["Document"]
            description = column["Description"]
            url = column["URL"]
            order_table.append(table(document, description, url))
        return order_table