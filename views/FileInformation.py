from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QFileDialog, QTextEdit
from PyQt5 import QtCore, uic

from views.AdvancedInformation import AdvancedInformation
from service.ConfigurationFile import ConfigurationFile


from Processor import Processor



class FileInformation(QDialog):
    
    def __init__(self, input_file, widget):
        super(FileInformation, self).__init__()
        uic.loadUi("./views/FileType.ui", self)
        self.content = input_file["archivo"]


        self.document_type = self.findChild(QComboBox, 'document_type')
        self.combo_export_format = self.findChild(QComboBox, 'export_format')
        self.file_type = self.findChild(QComboBox, 'file_type')


        self.button_next = self.findChild(QPushButton, 'button_next')
        self.button_back = self.findChild(QPushButton, 'button_back')

        self.add_content(self.document_type, 'document_type', self.content)
        self.add_content(self.combo_export_format, 'export_format', self.content)
        self.add_content(self.file_type, 'file_type', self.content)

        self.button_next.clicked.connect(lambda: self.on_submit(input_file, widget))
        self.button_back.clicked.connect(lambda: self.get_back(widget))

    
    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    
    
    def on_submit(self, input_file, widget):
        
        # Obtener el contenido del formulario
        document_type = self.document_type.currentText().lower()
        file_type = self.file_type.currentText().lower()
        exporter = self.combo_export_format.currentText().lower()

        # Guardar el contenido en el fichero de configuración
        result_file = self.save_config_file(document_type, file_type, exporter)

        # Abrir la seguiente ventana
        window = AdvancedInformation(input_file, result_file, widget)
        width = 560
        height = 465
        self.open_window(window, widget, width, height)




    def get_back(self, widget):
        widget.setFixedHeight(260)
        widget.setFixedWidth(430)
        widget.setCurrentIndex(widget.currentIndex()-1)

    
    
    def open_window(self, window, widget, width, height):
        try:
            widget.addWidget(window)
            widget.setFixedWidth(width)
            widget.setFixedHeight(height)
            widget.setCurrentIndex(widget.currentIndex()+1)
            return True
        except:
            return False


    

    def save_config_file(self, document_type :str, file_type :str, exporter :str):

        json_path = "./configuration/configuration_file.json"
        json_file = ConfigurationFile.import_file(json_path)

        to_check = ["strategy_config", "file_config"]
        
        if not ConfigurationFile.check_existence(json_path):
            json_file = ConfigurationFile.create_file()

        if not ConfigurationFile.check_structure(json_file, to_check):
            json_file = ConfigurationFile.create_file()

        strategy_config = json_file["strategy_config"]
        
        strategy_config["document_type"] = document_type
        strategy_config["file_type"] = file_type
        strategy_config["exporter"] = exporter

        # Guardamos el fichero
        ConfigurationFile.save_file(json_file, json_path)
        
        return  strategy_config
