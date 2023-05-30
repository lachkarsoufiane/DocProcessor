from interface.IFormatter import IFormatter
import re
import json

class RegexFormatterStrategy(IFormatter):
    
    def format(content, config):
        
        # Importar el contenido del fichero de assets
        escc_settings = config["formatter_config"]
        regex = re.compile(r'%s' % escc_settings["regex"])

        # Deserializar el contenido
        content = json.loads(content)
        result = []
        
        # Recorrer los parrafos del contenido
        for index in content:
            data = {}
            current_title = None
            titles = regex.findall(content[index])
            
            for line in content[index].split("\n"):
                match_title = False
                
                for title in titles:
                    if line.lower().startswith(title.lower()):
                        current_title = title
                        data[current_title] = line[len(title)+2:]
                        match_title = True
                

                if not match_title and current_title:
                    data[current_title] += line
            
            result.append(data)
        result = json.dumps(result)
        return result