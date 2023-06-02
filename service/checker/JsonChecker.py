from interface.IChecker import IChecker 
import json

class JsonChecker(IChecker):
    def ceck(content :str) -> bool:
        
        try:
            json.loads(content)
        except:
            return False
        return True
