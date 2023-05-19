from service.ConfigurationFile import ConfigurationFile
from Processor import Processor
import re

class Manager():

    strategy_config :dict
    process_config :dict

    def __init__(self, configuration_file) -> None:
        
        self.strategy_config = configuration_file["strategy_config"]
        self.process_config = configuration_file["process_config"]

        self.add_keys()

        self.run(configuration_file)

    
    def add_keys(self):
        file_type = self.strategy_config["file_type"].lower() 
        if  file_type == "dscc":
            self.process_config["start_key"] = "Document:"
            self.process_config["end_key"] = None
        elif file_type == "escc":
            self.process_config["start_key"] = re.compile(r'[A-Z][a-zA-Z -]+(?=:$)')
            self.process_config["end_key"] = re.compile(r'(Extension|Revision): [a-zA-Z. ]+')

        
    def run(self, configuration_file):
        Processor(configuration_file)
        
