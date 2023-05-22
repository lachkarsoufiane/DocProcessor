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
                "first_page": None,
                "last_page": None,
                "export_path": None
            },
            "process_config":
            {
                "start_key": None,
                "end_key": None,

                "escc": 
                {
                    "title": "(?:[0-9]+ )?([A-Z][a-zA-Z -]+(?=:$))",
                    "manufacture": "[^ ,][a-zA-Z!@#$&()\\-`+\\’ ]+\\([a-zA-Z]+\\)",
                    "certificate": "\\d{2,3}[A-Z](?:[rev]{3}\\d)?(?=, )",
                    "extra": "(Extension|Revision): [a-zA-Z. ]+",
                    "revision":"rev\\d{1}"
                },
                "dscc":
                {
                    "start_key":"Document: ",
                    "title":"[A-Z][a-zA-Z ]+(?=:)",
                    "url":"^https?:\/\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\/"
                }
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
        
        
    def add_configuration (file :dict, content :dict, key) -> dict:
        file[key] = content[key]
        return file
    

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
    

    def find_value (content :dict, key :str):
        if key in content:
            return content[key]
        
        for name in content:
            if key in content[name]:
                return content[name][key]
        return None


    def check_structure(content :dict, must_have :list) -> bool:
        for key in must_have:
            if key not in content:
                return False
        return True


    def check_existence(file_path :str) -> bool:
        return path.exists(file_path)
