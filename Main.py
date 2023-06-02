from service.configuration.ConfigurationFile import ConfigurationFile
from Processor import Processor

if __name__ == "__main__":
    
    # Importar el fichero de opciones
    json_path = "presets/escc.json"
    json_content = ConfigurationFile.import_file(json_path)

    Processor(json_content)


