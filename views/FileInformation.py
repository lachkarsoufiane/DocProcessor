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


        self.combo_file_types = self.findChild(QComboBox, 'file_types')
        self.combo_export_format = self.findChild(QComboBox, 'export_format')
        self.file_path = self.findChild(QTextEdit, 'file_path')
        self.file_button = self.findChild(QPushButton, 'file_button') 

        self.button_next = self.findChild(QPushButton, 'button_next')
        self.button_back = self.findChild(QPushButton, 'button_back')

        self.add_content(self.combo_file_types, 'file_type', self.content)
        self.add_content(self.combo_export_format, 'export_format', self.content)

        self.combo_file_types.activated.connect(lambda: self.empty_text_field(self.file_path))
        self.file_button.clicked.connect(self.file_navigation)
        self.button_next.clicked.connect(lambda: self.on_submit(input_file, widget))
        self.button_back.clicked.connect(lambda: self.get_back(widget))

    
    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    
    
    def file_navigation(self):
        input = self.combo_file_types.currentText()
        extention = '*.' + self.content["file_type"][input]
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Importar Fichero', directory='.', filter=extention)
        if filename:
            self.file_path.setText(filename)
            print(filter)
    
    
    def on_submit(self, input_file, widget):
        file_type = self.combo_file_types.currentText().lower()
        file_path = self.file_path.toPlainText()
        exporter = self.combo_export_format.currentText().lower()

        result_file = self.save_config_file(file_type, file_path, exporter)

        window = AdvancedInformation(input_file, result_file, widget)
        width = 560
        height = 325
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
    
    def empty_text_field(self, element):
        element.setPlainText("")

    def save_config_file(self, file_type :str, file_path :str, exporter :str):

        json_path = "./configuration/configuration_file.json"
        json_file = ConfigurationFile.import_file(json_path)
        print()
        to_check = ["strategy_config", "conf_file"]
        
        if not ConfigurationFile.check_existence(json_path):
            json_file = ConfigurationFile.create_file()


        if not ConfigurationFile.check_structure(json_file, to_check):
            json_file = ConfigurationFile.create_file()


        json_file["strategy_config"]["file_type"] = file_type
        json_file["strategy_config"]["exporter"] = exporter
        json_file["conf_file"]["file_path"] = file_path
        json_file["conf_file"]["page_number"] = 3

        # Guardamos el fichero
        ConfigurationFile.save_file(content=json_file, file_path=json_path)
        return json_file
