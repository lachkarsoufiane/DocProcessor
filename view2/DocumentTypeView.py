from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog, QTextEdit
from PyQt5 import uic
from view2.SplitterView import SplitterView

from service.configuration.PresetManager import PresetManger


class DocumentTypeView(QDialog):

    output_file :str

    def __init__(self, input_file :dict, widget):
        super(DocumentTypeView, self).__init__()
        # Leer la UI
        uic.loadUi('./view2/interface/document_type.ui', self)

        # Definir componentes
        self.source_input = self.findChild(QComboBox, 'source_input')
        self.type_input = self.findChild(QComboBox, 'type_input')
        self.name_input = self.findChild(QTextEdit, 'name_input')
        self.button_next = self.findChild(QPushButton, 'siguiente')
        
        # Añadir contenido al componentes
        self.add_content(self.source_input, "document_source", input_file)
        self.add_content(self.type_input, "file_type", input_file)
        self.button_next.clicked.connect(lambda: self.on_submit(input_file, widget))
        
        # Mostrar la app
        self.show()



    def add_content(self, element :object, key, input_file):
        for content in input_file[key]:
            element.addItem(content)



    def on_submit(self, input_file, widget):
        # Obtener el contenido del Combo Box 
        self.source_data = self.source_input.currentText()
        self.type_data = self.type_input.currentText()
        self.name_data = self.name_input.toPlainText()


        # Guardar ajustes
        if (PresetManger.save_content(self.name_data, )):
            # Preparar la ventana
            window = SplitterView(input_file, self.name_data, widget)
            width = 490
            height = 460

            
            # Abrir la seguiente ventana
            self.open_window(window, widget, width, height)
            
            return self.content

        

    
    def open_window(self, window, widget, width, height):
        try:
            widget.addWidget(window)
            widget.setFixedWidth(width)
            widget.setFixedHeight(height)
            widget.setCurrentIndex(widget.currentIndex()+1)
            return True
        except:
            return False


