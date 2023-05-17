from abc import ABC, abstractstaticmethod

class IExporter(ABC):
    @abstractstaticmethod
    def export(table, config :dict) -> bool:
        pass
