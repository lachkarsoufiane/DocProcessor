from abc import ABC, abstractclassmethod

class ICreateConfig(ABC):
    @abstractclassmethod
    def create_strategy_config() -> str:
        pass

    @abstractclassmethod
    def create_info_config() -> str:
        pass