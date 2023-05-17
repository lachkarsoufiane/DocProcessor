from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QFileDialog, QTextEdit
from PyQt5 import QtCore, uic

from service.ConfigurationFile import ConfigurationFile


from Processor import Processor



class AdvancedInformation(QDialog):
    
    def __init__(self, input_file, result_file, widget):
        super(AdvancedInformation, self).__init__()
        uic.loadUi("./views/AdvancedInformation.ui", self)
        self.content = input_file["archivo"]
        print(result_file)

        self.file_path = self.findChild(QTextEdit, 'file_path')
        self.file_button = self.findChild(QPushButton, 'file_button')
        self.first_page = self.findChildren(QTextEdit, 'first_page')

        self.button_next = self.findChild(QPushButton, 'button_next')
        self.button_back = self.findChild(QPushButton, 'button_back')


        # self.document_type.activated.connect(lambda: self.empty_text_field(self.file_path))
        self.file_button.clicked.connect(self.file_navigation)
        self.button_next.clicked.connect(lambda: self.on_submit(result_file))
        self.button_back.clicked.connect(lambda: self.get_back(widget))

    
    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    

    def file_navigation(self):
        # input = self.document_type.currentText()
        # extention = '*.' + self.content["document_type"][input]
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Importar Fichero', directory='.', filter="*.pdf")
        if filename:
            self.file_path.setText(filename)

    def on_submit(self, result_file):
        pass
        # Processor(result_file)

    def get_back(self, widget):
        widget.setFixedHeight(455)
        widget.setFixedWidth(550)
        widget.setCurrentIndex(widget.currentIndex()-1)

    
    
    

   