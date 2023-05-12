from interface.IPrinter import IPrinter

class ConsolePrinterStrategy(IPrinter):

    def print(content: str, config: dict):
        try:
            print(content)
            return True
        except:
            return False