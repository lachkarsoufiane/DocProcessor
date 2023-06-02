from interface.IChecker import IChecker
import json 

class JsonFileChecker(IChecker):
    def check(path :str) -> bool:
        try:
            with open(path) as json_file:
                content = json.load(json_file)
        except:
            return False
        return True