from service.printer.ConsolePrinterStrategy import ConsolePrinterStrategy
from service.printer.FilePrinterStrategy import FilePrinterStrategy
from service.reader.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.reader.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.splitter.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from service.splitter.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from service.formatter.DSCCFormatterStrategy import DSCCFormatterStrategy
from service.table_formatter.TableDSCCFormatterStrategy import TableDSCCFormatterStrategy
from service.exporter.ExcelExporterStrategy import ExcelExportStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():


    def create(config: dict):
        config = config['strategy_config']
        file_type = CreateStrategyFile.find_reader(config['document_type'].lower())
        splitter = CreateStrategyFile.find_splitter(config['file_type'].lower())
        formatter = CreateStrategyFile.find_formatter(config['file_type'].lower())
        table_formatter = CreateStrategyFile.find_tabe_formatter(config['file_type'].lower())
        exporter = CreateStrategyFile.find_printer(config['exporter'].lower())

        return PossibleStrategy(file_type, splitter, formatter, table_formatter, exporter)
    
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
    
    def find_formatter(key: str):
        switch = {
            "escc" : DSCCFormatterStrategy,
            "dscc": DSCCFormatterStrategy 
        }
        return switch.get(key, DSCCFormatterStrategy)
    
    def find_tabe_formatter(key :str):
        switch = {
            "escc" : TableDSCCFormatterStrategy,
            "dscc": TableDSCCFormatterStrategy 
        }
        return switch.get(key, TableDSCCFormatterStrategy)

    def find_printer(key: str):
        switch = {
            "consola" : ConsolePrinterStrategy,
            "texto" : FilePrinterStrategy,
            "excel" : ExcelExportStrategy
        }
        return switch.get(key, ExcelExportStrategy)
