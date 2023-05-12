
from interface.IStrategy import IStrategy
from interface.IPrinter import IPrinter
from interface.IReader import IReader

from service.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.ConsolePrinterStrategy import ConsolePrinterStrategy

class FileToConsoleStrategy(IStrategy):
    reader: IReader
    printer: IPrinter

    def __init__(self) :
        self.reader = PDFTextReaderStrategy
        self.printer = ConsolePrinterStrategy
    