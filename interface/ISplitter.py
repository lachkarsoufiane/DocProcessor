from abc import ABC, abstractstaticmethod

class ISplitter(ABC):
    @abstractstaticmethod
    def split_content(content, start, end = None):
        pass