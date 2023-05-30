from service.printer.ConsolePrinterStrategy import ConsolePrinterStrategy
from service.printer.FilePrinterStrategy import FilePrinterStrategy
from service.reader.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.reader.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.splitter.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from service.splitter.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from service.formatter.DSCCFormatterStrategy import DSCCFormatterStrategy
from service.formatter.ESCCFormatterStrategy import ESCCFormatter
from service.formatter.RegexFormatterStrategy import RegexFormatterStrategy
from service.table_formatter.TableESCCFormatterStrategy import TableESCCFormatterStrategy
from service.table_formatter.TableDSCCFormatterStrategy import TableDSCCFormatterStrategy
from service.exporter.ExcelExporterStrategy import ExcelExportStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():


    def create(config: dict):
        file_type = CreateStrategyFile.find_reader(config['reader'].lower())
        splitter = CreateStrategyFile.find_splitter(config['splitter'].lower())
        formatter = CreateStrategyFile.find_formatter(config['formatter'].lower())
        # table_formatter = CreateStrategyFile.find_tabe_formatter(config['table_formatter'].lower())
        exporter = CreateStrategyFile.find_exporter(config['exporter'].lower())

        return PossibleStrategy(file_type, splitter, formatter, exporter)
    
    def find_reader(key: str):
        switch = {
            "text reader" : ConsoleReaderStrategy,
            "pdf reader" : PDFTextReaderStrategy
        }
        return switch.get(key, PDFTextReaderStrategy)

    
    def find_splitter(key: str):
        switch = {
            "regex paragraph splitter" : ParagraphRegexSplitterStrategy,
            "keyword paragraph splitter": ParagraphKeywordSplitterStrategy
        }
        return switch.get(key, None)
    
    def find_formatter(key: str):
        switch = {
            "dictionary formatter" : ESCCFormatter,
            "regex formatter": RegexFormatterStrategy 
        }
        return switch.get(key, None)
    
    def find_tabe_formatter(key :str):
        switch = {
            "escc" : TableESCCFormatterStrategy,
            "dscc": TableDSCCFormatterStrategy 
        }
        return switch.get(key, None)

    def find_exporter(key: str):
        switch = {
            "consola" : ConsolePrinterStrategy,
            "texto" : FilePrinterStrategy,
            "excel" : ExcelExportStrategy
        }
        return switch.get(key, ExcelExportStrategy)
