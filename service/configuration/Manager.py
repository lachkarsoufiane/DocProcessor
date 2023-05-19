from Processor import Processor
# from views.MainWindows import MainWindows
# from views.FileInformation import FileInformation
# from views.AdvancedInformation import AdvancedInformation
from service.configuration.ConfigurationFile import ConfigurationFile


class Manager():

    configuration_file :dict
    strategy_config :dict
    process_config :dict

    
    def __init__(self, configuration_file) -> None:

        self.process_settings = ConfigurationFile.import_file("./asset/process_settings.json")
        # self.form_content = form_content
        # self.filter_form(form_content)
        self.configuration_file = configuration_file
        self.strategy_config = configuration_file["strategy_config"]
        self.process_config = configuration_file["process_config"]
        self.add_keys()
        self.run(configuration_file)


    # def filter_form(self, form_content): 
    #     try:
    #         for key in form_content:
    #             switch = {
    #                 "content_type" : FileInformation,
    #                 "strategy_config" : AdvancedInformation,
    #                 "file_config" : "",
    #             }
    #             return switch.get(key, MainWindows)
    #     except:
    #         return MainWindows()
    



    def add_keys(self):
        file_type = self.strategy_config["file_type"].lower() 
        if  file_type == "dscc":
            self.process_config["start_key"] = self.process_settings["dscc"]["start_key"]
            self.process_config["end_key"] = None
        elif file_type == "escc":
            self.process_config["start_key"] = self.process_settings[file_type]["title"]
            self.process_config["end_key"] = self.process_settings[file_type]["extra"]

        # Guardar cambios en el fichero de configuración 
        ConfigurationFile.save_file(self.configuration_file)
        
    def run(self, configuration_file):
        Processor(configuration_file)
        
