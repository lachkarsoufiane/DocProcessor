from interface.IPrinter import IPrinter

class FilePrinterStrategy(IPrinter):
    def print(content: str, config: dict):
        try:
            config = config['strategy_config']
            file_path = "./exports/" + config['exporter'] 
            with open(file_path, "w") as file:
                file.write(content)
            return True
        except:
            return False