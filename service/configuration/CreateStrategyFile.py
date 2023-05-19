from service.printer.ConsolePrinterStrategy import ConsolePrinterStrategy
from service.printer.FilePrinterStrategy import FilePrinterStrategy
from service.reader.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.reader.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.splitter.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from service.splitter.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():
    
    def create(config: dict):
        config = config['strategy_config']
        file_type = CreateStrategyFile.find_reader(config['document_type'].lower())
        splitter = CreateStrategyFile.find_splitter(config['file_type'].lower())
        exporter = CreateStrategyFile.find_printer(config['exporter'].lower())

        return PossibleStrategy(file_type, splitter, exporter)
    
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
