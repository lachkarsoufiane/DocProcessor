from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QFileDialog, QTextEdit
from PyQt5 import QtCore, uic

from service.ConfigurationFile import ConfigurationFile


from Processor import Processor



class AdvancedInformation(QDialog):
    
    def __init__(self, input_file, widget):
        super(AdvancedInformation, self).__init__()
        uic.loadUi("./views/AdvancedInformation.ui", self)
        self.content = input_file["archivo"]


        self.combo_file_types = self.findChild(QComboBox, 'file_types')

        self.button_next = self.findChild(QPushButton, 'button_next')
        self.button_back = self.findChild(QPushButton, 'button_back')

        self.add_content(self.combo_file_types, 'file_kind', self.content)

        self.button_next.clicked.connect(self.on_submit)
        self.button_back.clicked.connect(lambda: self.get_back(widget))

    
    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    
    def on_submit(self):
        print("done")

    def get_back(self, widget):
        widget.setFixedHeight(455)
        widget.setFixedWidth(550)
        widget.setCurrentIndex(widget.currentIndex()-1)

    
    
    

   