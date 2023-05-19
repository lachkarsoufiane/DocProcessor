from interface.IFormatter import IFormatter
from service.configuration.ConfigurationFile import ConfigurationFile
import re
import json

class DSCCFormatterStrategy(IFormatter):
    
    def format(content):
        # Importar el contenido del fichero de assets
        asset_file = ConfigurationFile.import_file("./asset/process_settings.json")
        url_re = re.compile(r'%s' % asset_file["dscc"]["url"])
        title_re = re.compile(r'%s' % asset_file["dscc"]["title"])

        # Deserializar el contenido
        content = json.loads(content)
        result = []
        
        # Recorrer los parrafos del contenido
        for index in content:
            data = {}
            current_title = None
            titles = title_re.findall(content[index])
            
            for line in content[index].split("\n"):
                match_title = False
                
                for title in titles:
                    if line.lower().startswith(title.lower()):
                        current_title = title
                        data[current_title] = line[len(title)+2:]
                        match_title = True
                

                if not match_title and current_title:
                    data[current_title] += line

                    #Quitar los espacios en blancos, en el caso de ser enlace
                    if url_re.match(data[current_title]):
                        data[current_title] = data[current_title].replace(" ", "")
            
            result.append(data)
        result = json.dumps(result)
        print(result)
        return result