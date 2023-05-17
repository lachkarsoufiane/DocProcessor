from interface.ISaver import ISaver
from os import path
import json


class ConfigurationFile(ISaver):
    
    def __init__(self) -> None:
        pass


    def create_file() -> dict:
        file = {
            "strategy_config": {
                "document_type": None,
                "file_type": None,
                "exporter": None
            },
            "file_config":{
                "file_path": None,
                "start_key": None,
                "page_number": None,
                "end_key": None
            }
        }
        return file

    
    def save_file(content :dict, file_path :str = None) -> bool:
        try:
            if file_path == None : file_path = "./configuration/configuration_file.json"
            with open(file_path, "w") as file:
                json.dump(content, file)
            return True
        except:
            return False
        
    
    def modify_file (file :dict, content :dict, root :str) -> dict:
        
        content = content[root]

        try:
            for key in content:
                file[root][key] = content[key]
            print(file)
            return file 
        except:
            return None

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
    
    def check_existence(file_path :str) -> bool:
        return path.exists(file_path)
