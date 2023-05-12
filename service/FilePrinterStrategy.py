from interface.IPrinter import IPrinter

class FilePrinterStrategy(IPrinter):
    def print(content: str, config: dict):
        try:
            config = config['info'][0]
            file_path = "./exports/" + config['file_output'] 
            with open(file_path, "w") as file:
                file.write(content)
            return True
        except:
            return False