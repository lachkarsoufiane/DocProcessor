from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QFileDialog, QTextEdit
from PyQt5 import QtCore, uic

from service.ConfigurationFile import ConfigurationFile


from Processor import Processor



class AdvancedInformation(QDialog):
    
    def __init__(self, input_file, result_file, widget):
        super(AdvancedInformation, self).__init__()
        uic.loadUi("./views/AdvancedInformation.ui", self)
        self.content = input_file["archivo"]


        self.combo_file_types = self.findChild(QComboBox, 'file_types')

        self.button_next = self.findChild(QPushButton, 'button_next')
        self.button_back = self.findChild(QPushButton, 'button_back')

        self.add_content(self.combo_file_types, 'file_kind', self.content)

        self.button_next.clicked.connect(lambda: self.on_submit(result_file))
        self.button_back.clicked.connect(lambda: self.get_back(widget))

    
    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    
    def on_submit(self, result_file):
        file_kind = self.combo_file_types.currentText().lower()
        if file_kind == "dscc":
            start_key = "Document:"

        result_file["strategy_config"]["file_kind"] = file_kind
        result_file["conf_file"]["start_key"] = start_key
        Processor(result_file)

    def get_back(self, widget):
        widget.setFixedHeight(455)
        widget.setFixedWidth(550)
        widget.setCurrentIndex(widget.currentIndex()-1)

    
    
    

   