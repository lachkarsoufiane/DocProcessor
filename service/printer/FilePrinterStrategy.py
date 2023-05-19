from interface.IPrinter import IPrinter

class FilePrinterStrategy(IPrinter):
    
    def print(content: str, config: dict):
        try:
            config = config['file_config']
            # file_name = config['export_name']+".txt"
            file_path = config['export_path']
            
            if file_path is None:
                file_path = "./exports/" + "test" 

            
            with open(file_path, "w") as file:
                file.write(content)
            return True
        except:
            return False