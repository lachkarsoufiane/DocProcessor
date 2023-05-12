from abc import ABC
from interface.IReader import IReader
from interface.IPrinter import IPrinter

class IStrategy(ABC):
    reader: IReader
    printer: IPrinter