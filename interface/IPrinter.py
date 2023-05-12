from abc import ABC, abstractstaticmethod

class IPrinter(ABC):
    @abstractstaticmethod
    def print(content: str, config = None):
        pass