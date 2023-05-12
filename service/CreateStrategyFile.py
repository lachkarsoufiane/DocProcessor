from service.ConsolePrinterStrategy import ConsolePrinterStrategy
from service.FilePrinterStrategy import FilePrinterStrategy
from service.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.PDFTextReaderStrategy import PDFTextReaderStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():
    def create(config: dict):
        config = config['strategy'][0]
        reader = CreateStrategyFile.find_reader(config['reader'])
        printer = CreateStrategyFile.find_printer(config['printer'])
        print(f"Estrategia: {reader}, {printer}")

        return PossibleStrategy(reader, printer)
    
    def find_printer(num: int):
        switch = {
            "Archivo" : ConsolePrinterStrategy,
            "Api" : FilePrinterStrategy
        }
        return switch.get(num, ConsolePrinterStrategy)
    
    def find_reader(num: int):
        switch = {
            "Archivo" : ConsoleReaderStrategy,
            "Api" : PDFTextReaderStrategy
        }
        return switch.get(num, PDFTextReaderStrategy)
