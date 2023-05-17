from interface.IStrategy import IStrategy
from interface.IPrinter import IPrinter
from interface.IReader import IReader
from interface.ISplitter import ISplitter

class PossibleStrategy(IStrategy):
    reader :IReader
    printer :IPrinter
    splitter :ISplitter

    def __init__(self, reader :IReader,  printer :IPrinter) :
        self.reader = reader
        self.printer = printer
        