from interface.IStrategy import IStrategy
from interface.IPrinter import IPrinter
from interface.IReader import IReader

from service.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.FilePrinterStrategy import FilePrinterStrategy

class FileToConsoleStrategy(IStrategy):
    reader: IReader
    exporter: IPrinter

    def __init__(self) :
        self.reader = PDFTextReaderStrategy
        self.exporter = FilePrinterStrategy
    