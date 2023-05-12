from interface.IStrategy import IStrategy
from interface.IPrinter import IPrinter
from interface.IReader import IReader

from service.ConsoleReaderStrategy import ConsoleReaderStrategy
from service.FilePrinterStrategy import FilePrinterStrategy

class FileToConsoleStrategy(IStrategy):
    reader: IReader
    printer: IPrinter

    def __init__(self) :
        self.reader = ConsoleReaderStrategy
        self.printer = FilePrinterStrategy
    