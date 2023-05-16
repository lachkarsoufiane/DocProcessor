from interface.ISaver import ISaver
import json


class ConfigurationFile(ISaver):
    
    def create_file() -> dict:
        file = {
            "strategy_config": {
                "file_type": "",
                "exporter": ""
            },
            "conf_file":{
                "file_path": "",
                "file_kind": ""
            }
        }
        return file

    
    def save_file(content :dict, path :str = None) -> bool:
        try:
            if path == None : path = "./configuration/configuration_file.json"
            with open(path, "w") as file:
                json.dump(content, file)
            return True
        except:
            return False
        

    def import_file(path :str) -> dict:
        try:
            with open(path) as json_file:
                data = json.load(json_file)
            return data
        except:
            return None
    
    def check_structure(content :dict, must_have :list) -> bool:
        for key in must_have:
            if key not in content:
                return False
        return True
    
