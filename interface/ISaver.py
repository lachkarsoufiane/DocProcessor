from abc import ABC, abstractstaticmethod

class ISaver(ABC):
    @abstractstaticmethod
    
    def create_file() -> dict:
        pass

    def save_file(content :dict, path :str = None) -> bool:
        pass

    def import_file(path :str) -> dict:
        pass