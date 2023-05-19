from service.configuration.CreateStrategyFile import CreateStrategyFile

class Processor():
    strategy: CreateStrategyFile
    
    def __init__(self, config: dict):
        # Crear el json de strategia
        self.strategy = CreateStrategyFile.create(config)

        # Leer el contenido del fichero requerido
        content = self.strategy.reader.read(config)
        paragraphs = self.strategy.splitter.split_content(content, config)
        formated_content = self.strategy.formatter.format(paragraphs)
        table_formate = self.strategy.table_formatter.format(formated_content)
        # Exportar el resultado
        self.strategy.exporter.export(table_formate, config)
