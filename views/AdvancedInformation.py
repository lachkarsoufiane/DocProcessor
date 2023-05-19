from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QFileDialog, QTextEdit, QCheckBox
from PyQt5 import QtCore, uic

from service.configuration.Manager import Manager
from service.configuration.ConfigurationFile import ConfigurationFile


from Processor import Processor



class AdvancedInformation(QDialog):
    
    def __init__(self, input_file, result_file, widget):
        super(AdvancedInformation, self).__init__()
        uic.loadUi("./views/AdvancedInformation.ui", self)
        self.content = input_file["archivo"]

        options = self.content["document_type"]
        document_type = result_file["document_type"]
        self.extension = self.file_extension(options, document_type)


        self.file_path = self.findChild(QTextEdit, 'file_path')
        self.file_button = self.findChild(QPushButton, 'file_button')

        self.save_path = self.findChild(QTextEdit, 'save_path')
        self.save_button = self.findChild(QPushButton, 'save_button')

        self.first_page = self.findChild(QTextEdit, 'first_page')
        self.last_page = self.findChild(QTextEdit, 'last_page')
        self.all_pages = self.findChild(QCheckBox, 'all_pages')

        self.button_next = self.findChild(QPushButton, 'button_next')
        self.button_back = self.findChild(QPushButton, 'button_back')


        self.file_button.clicked.connect(lambda: self.file_navigation(self.extension))
        self.save_button.clicked.connect(self.save_navigation)
        self.button_next.clicked.connect(self.on_submit)
        self.button_back.clicked.connect(lambda: self.get_back(widget))

    
    
    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    

    def file_extension(self, options :dict, document_type :str):
        return options[document_type]


    def file_navigation(self, extension):
        ext = "*."+extension
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Importar Fichero', directory='.', filter=ext)
        if filename:
            self.file_path.setText(filename)

    
    def save_navigation(self):
        filename, filter = QFileDialog.getSaveFileName(parent=self, caption='Importar Fichero', directory='.', filter="*.txt")
        if filename:
            self.save_path.setText(filename)


    def on_submit(self):
        file_path = self.file_path.toPlainText()
        export_path = self.save_path.toPlainText()
        
        if self.all_pages.isChecked():
            first_page = None
            last_page = None 
        elif self.last_page.toPlainText() ==  "":
            first_page = int(self.first_page.toPlainText())
            last_page = None
        else:
            first_page = int(self.first_page.toPlainText())
            last_page = int(self.last_page.toPlainText())


        config_file = self.save_config_file(file_path, export_path, first_page, last_page)
        
        Manager(config_file)

        # Processor(config_file)


    def get_back(self, widget):
        widget.setFixedHeight(455)
        widget.setFixedWidth(550)
        widget.setCurrentIndex(widget.currentIndex()-1)



    def save_config_file(self, file_path :str, export_path :str, first_page :int, last_page :int):

        json_path = "./configuration/configuration_file.json"
        json_file = ConfigurationFile.import_file(json_path)

        to_check = ["strategy_config", "file_config"]
        
        if not ConfigurationFile.check_existence(json_path):
            json_file = ConfigurationFile.create_file()

        if not ConfigurationFile.check_structure(json_file, to_check):
            json_file = ConfigurationFile.create_file()

        file_config = json_file["file_config"]
        
        file_config["file_path"] = file_path
        file_config["export_path"] = export_path
        file_config["first_page"] = first_page
        file_config["last_page"] = last_page

        # Guardamos el fichero
        ConfigurationFile.save_file(json_file, json_path)
        
        return  json_file

    
    
    

   