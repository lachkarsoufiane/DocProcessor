from Processor import Processor
from service.CreateConfigFile import CreateConfigFile

if __name__ == "__main__":
    
    data = {}
    prueba = CreateConfigFile
    data = prueba.create_strategy_config(data)
    data = prueba.create_info_config(data)

    Processor(data)