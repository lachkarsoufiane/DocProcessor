from interface.IFormatter import IFormatter
from collections import namedtuple
import json

class TableESCCFormatterStrategy(IFormatter):
    def format(content):
        content = json.loads(content)
        table = namedtuple('table', 'Certificate Revision Description Manufacturer Action')
        order_table = []
        for certificate in content:
            action = content[certificate]["Title"]
            description = content[certificate]["Description"]
            manufacturer = content[certificate]["Manufacturer"]
            revision = content[certificate]["Revision"]
            order_table.append(table(certificate, revision, description, manufacturer, action))
        return order_table