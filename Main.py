from Processor import Processor
import json

if __name__ == "__main__":

    # Importar el fichero de configuración
    json_path = "presets/escc.json"
    with open(json_path) as conf_file:
        configuration = json.load(conf_file)

    Processor(configuration)
