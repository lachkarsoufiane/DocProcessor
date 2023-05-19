from interface.IStrategy import IStrategy
from interface.IPrinter import IPrinter
from interface.IReader import IReader
from interface.ISplitter import ISplitter
from interface.IFormatter import IFormatter
from interface.IExporter import IExporter

class PossibleStrategy(IStrategy):
    reader :IReader
    printer :IPrinter
    splitter :ISplitter
    formatter :IFormatter
    table_formatter :IFormatter
    exporter :IExporter

    def __init__(self, reader :IReader, splitter :ISplitter, formatter :IFormatter, table_formatter :IFormatter, exporter :IExporter) :
        self.reader = reader
        self.splitter = splitter
        self.formatter = formatter
        self.table_formatter = table_formatter
        self.exporter = exporter
        