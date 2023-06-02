from abc import ABC, abstractstaticmethod

class IChecker(ABC):
    @abstractstaticmethod
    def check(content ):
        pass