
from service.reader.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.reader.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.splitter.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from service.splitter.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy
from service.splitter.KeyValueSplitterStrategy import KeyValueSplitterStrategy
from service.formatter.ESCCFormatterStrategy import ESCCFormatterStrategy
from service.formatter.RegexFormatterStrategy import RegexFormatterStrategy
from service.exporter.ExcelExporterStrategy import ExcelExporterStrategy
from service.exporter.JsonExporterStrategy import JsonExporterStrategy
from strategy.PossibleStrategy import PossibleStrategy

class CreateStrategyFile():


    def create(config: dict):
        file_type = CreateStrategyFile.find_reader(config['reader'].lower())
        splitter = CreateStrategyFile.find_splitter(config['splitter'].lower())
        formatter = CreateStrategyFile.find_formatter(config['formatter'].lower())
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
            "key value splitter" : KeyValueSplitterStrategy,
            "regex paragraph splitter" : ParagraphRegexSplitterStrategy,
            "keyword paragraph splitter": ParagraphKeywordSplitterStrategy
        }
        return switch.get(key, None)
    
    def find_formatter(key: str):
        switch = {
            "escc formatter" : ESCCFormatterStrategy,
            "regex formatter": RegexFormatterStrategy 
        }
        return switch.get(key, None)
    
    def find_exporter(key: str):
        switch = {
            "excel exporter" : ExcelExporterStrategy,
            "json exporter" : JsonExporterStrategy,

        }
        return switch.get(key, JsonExporterStrategy)
