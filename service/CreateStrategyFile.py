from service.ConsolePrinterStrategy import ConsolePrinterStrategy
from service.FilePrinterStrategy import FilePrinterStrategy
from service.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from service.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():
    
    def create(config: dict):
        config = config['strategy_config']
        file_type = CreateStrategyFile.find_reader(config['document_type'].lower())
        splitter = CreateStrategyFile.find_splitter(config['file_type'].lower())
        exporter = CreateStrategyFile.find_printer(config['exporter'].lower())

        return PossibleStrategy(file_type, exporter)
    
    def find_reader(key: str):
        switch = {
            "text" : ConsoleReaderStrategy,
            "pdf" : PDFTextReaderStrategy
        }
        return switch.get(key, PDFTextReaderStrategy)

    def find_splitter(key: str):
        switch = {
            "escc" : ParagraphRegexSplitterStrategy,
            "dscc": ParagraphKeywordSplitterStrategy 
        }
        return switch.get(key, ParagraphKeywordSplitterStrategy)

    def find_printer(key: str):
        switch = {
            "consola" : ConsolePrinterStrategy,
            "texto" : FilePrinterStrategy
        }
        return switch.get(key, ConsolePrinterStrategy)
