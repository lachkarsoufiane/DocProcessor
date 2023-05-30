from os import path
import json

class PresetManger():
    
    def __init__(self) -> None:
        pass

    def save_content(name, content):
        try:
            url = "./presets/"+name+".json"

            if not path.exists(url):
                with open(url, "w") as file:
                    json.dump(content, file)
            else:
                with open(url) as file:
                    data = json.load(file)
            return True
        except:
            return False



