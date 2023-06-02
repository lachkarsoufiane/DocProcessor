from interface.IChecker import IChecker
import json

class ConfigurationChecker(IChecker):
    def check(content :str):
        
        try:
            
            content = json.loads(content)
            
            


        except Exception as e:
            raise Exception("Fichero de configuración:", e)
