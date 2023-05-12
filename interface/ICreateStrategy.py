from abc import ABC,abstractclassmethod

class ICreateStrategy(ABC):
    @abstractclassmethod
    def create(self, config: dict):
        pass