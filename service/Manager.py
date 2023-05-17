from service.ConfigurationFile import ConfigurationFile
import re

class Manager():

    strategy_config :dict
    file_config :dict

    def __init__(self, configuration_file) -> None:
        
        self.strategy_config = configuration_file["strategy_config"]
        self.file_config = configuration_file["file_config"]

        self.add_keys()

    
    def add_keys(self):
        file_type = self.strategy_config["file_type"].lower() 
        if  file_type == "dscc":
            self.file_config["start_key"] = "Document:"
            self.file_config["end_key"] = None
        elif file_type == "escc":
            self.file_config["start_key"] = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')
            self.file_config["end_key"] = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')
        
