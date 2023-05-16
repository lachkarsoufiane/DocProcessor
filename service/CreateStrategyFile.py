from service.ConsolePrinterStrategy import ConsolePrinterStrategy
from service.FilePrinterStrategy import FilePrinterStrategy
from service.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.PDFTextReaderStrategy import PDFTextReaderStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():
    
    def create(config: dict):
        config = config['strategy_config']
        file_type = CreateStrategyFile.find_reader(config['file_type'].lower())
        exporter = CreateStrategyFile.find_printer(config['exporter'].lower())

        return PossibleStrategy(file_type, exporter)
    
    def find_printer(num: int):
        switch = {
            "consola" : ConsolePrinterStrategy,
            "texto" : FilePrinterStrategy
        }
        return switch.get(num, ConsolePrinterStrategy)
    
    def find_reader(num: int):
        switch = {
            "text" : ConsoleReaderStrategy,
            "pdf" : PDFTextReaderStrategy
        }
        return switch.get(num, PDFTextReaderStrategy)

