from interface.IExporter import IExporter
import json


class JsonExporterStrategy(IExporter):
    
    def export(content, config :dict) -> bool:
        

        try:
            config = config["export_config"]
            export_path = config["path"]
        except:
            raise Exception("Se ha ocurrido un error al leer el fichero de configuracion.")
        
        try:
            # Deserializar el contenido para comprobar si tiene un formato valido
            content = json.loads(content)
        except:
            raise Exception("El contenido no esta en el formato correcto.")
        


        try:
            with open(export_path, "w")as file:
                json.dump(content, file)
        except Exception as e:
            raise Exception("Se ha ocurrido un error al guardar el archivo.")

        return True