from interface.IReader import IReader

class ConsoleReaderStrategy(IReader):
    def read(content: str):
        content = input("Introduce los datos del archivo:\n")
        return content