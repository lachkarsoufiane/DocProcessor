from abc import ABC, abstractstaticmethod

class IWindow(ABC):
    @abstractstaticmethod
    def on_submit():
        pass

    def add_content():
        pass