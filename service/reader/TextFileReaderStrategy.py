from interface.IReader import IReader


class TextFileReaderStrategy(IReader):

    def read(config: dict) -> str:
        file_config = config['reader_config']
        file_path = file_config["path"]
        content = ""
        # Leer el fichero
        try:
            with open(file_path) as file:
                lines = file.readlines()
            content = "".join(lines)
        except:
            raise("Se ha ocurrido un error al leer el fichero.")
        
        return content
