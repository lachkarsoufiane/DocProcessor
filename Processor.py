from interface.IStrategy import IStrategy
from service.CreateStrategyFile import CreateStrategyFile

class Processor():
    strategy: CreateStrategyFile
    
    def __init__(self, config: dict):
        self.strategy = CreateStrategyFile.create(config)

        content = self.strategy.reader.read(config)
        self.strategy.printer.print(content, config)
