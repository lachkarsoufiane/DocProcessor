from service.configuration.CreateStrategyFile import CreateStrategyFile

class Processor():
    strategy: CreateStrategyFile
    
    def __init__(self, config: dict):
        # Crear el json de strategia
        self.strategy = CreateStrategyFile.create(config)

        # Leer el contenido del fichero requerido
        print("Leyendo el documento...")
        content = self.strategy.reader.read(config)
        print("Cortando el contenido...")
        paragraphs = self.strategy.splitter.split_content(content, config)
        print("Formateando el contenido...")
        formated_content = self.strategy.formatter.format(paragraphs, config)
        print("Creando la tabla...")
        table_formate = self.strategy.table_formatter.format(formated_content)
        # Exportar el resultado
        print("Exportando el resultado...")
        self.strategy.exporter.export(table_formate, config)
