import json
import sys
import typing
from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QPushButton, QApplication, QDialog, QFileDialog, QTextEdit
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore, uic

from Processor import Processor


class MainWindows(QDialog):

    output_file :str
    def __init__(self, input_file :dict, widget):
        super(MainWindows, self).__init__()
        
        # Leer la UI
        uic.loadUi('./views/MainView.ui', self)

        # Definir widgets
        self.combo_type_content = self.findChild(QComboBox, 'combo_type_content')
        self.button_next = self.findChild(QPushButton, 'button_next')

        
        self.add_types(self.combo_type_content, input_file)
        self.button_next.clicked.connect(lambda: self.next_view(input_file, widget))

        # Mostrar la app
        self.show()
        

        

    def next_view(self, input_file, widget):
        self.content = self.combo_type_content.currentText()
        next_page = NextPage(input_file)
        widget.addWidget(next_page)
        widget.setFixedHeight(430)
        widget.setFixedWidth(550)
        widget.setCurrentIndex(widget.currentIndex()+1)
        return self.content
    


    def add_types(self, element :object,  input_file :dict):
        for content in input_file["content_type"]:
            element.addItem(content)




class NextPage(QDialog):
    def __init__(self, input_file):
        super(NextPage, self).__init__()
        uic.loadUi("./views/FileType.ui", self)
        self.content = input_file["archivo"]


        self.combo_file_types = self.findChild(QComboBox, 'file_types')
        self.combo_export_format = self.findChild(QComboBox, 'export_format')
        self.button_next = self.findChild(QPushButton, 'button_next')
        self.file_path = self.findChild(QTextEdit, 'file_path')
        self.file_button = self.findChild(QPushButton, 'file_button')

        self.add_content(self.combo_file_types, 'file_type', self.content)
        self.add_content(self.combo_export_format, 'export_format', self.content)

        self.file_button.clicked.connect(self.file_navigation)
        self.button_next.clicked.connect(self.on_submit)

    
    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)
    
    def file_navigation(self):
        input = self.combo_file_types.currentText()
        extention = '*.' + self.content["file_type"][input]
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Importar Fichero', directory='.', filter=extention)
        if filename:
            self.file_path.setText(filename)
    
    def on_submit(self):
        file_type = self.combo_file_types.currentText().lower()
        file_path = self.file_path.toPlainText()
        exporter = self.combo_export_format.currentText().lower()
        Processor(self.save_config_file(file_type, file_path, exporter))

    
    def save_config_file(self, file_type :str, file_path :str, exporter :str):
        data = {}
        data["strategy_config"] = {}
        data["conf_file"] = {}

        data["strategy_config"]["file_type"] = file_type
        data["strategy_config"]["exporter"] = exporter
        data["conf_file"]["file_path"] = file_path
        data["conf_file"]["page_number"] = 1


        return data
