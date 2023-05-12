from abc import ABC, abstractstaticmethod

class IReader(ABC):
    @abstractstaticmethod
    def read(config = None, content = None):
        pass
