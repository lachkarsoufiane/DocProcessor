from PyQt5.QtWidgets import QComboBox, QPushButton, QDialog
from PyQt5 import uic
from service.configuration.Manager import Manager

from views.FileInformation import FileInformation


class MainWindows(QDialog):

    output_file :str
    def __init__(self, input_file :dict, widget):
        super(MainWindows, self).__init__()
        
        # Leer la UI
        uic.loadUi('./views/interface/MainView.ui', self)

        # Definir widgets
        self.combo_type_content = self.findChild(QComboBox, 'combo_type_content')
        self.button_next = self.findChild(QPushButton, 'button_next')

        
        self.add_types(self.combo_type_content, input_file)
        self.button_next.clicked.connect(lambda: self.on_submit(input_file, widget))

        # Mostrar la app
        self.show()
        

        

    def on_submit(self, input_file, widget):
        # Obtener el contenido del Combo Box 
        self.content = self.combo_type_content.currentText()

        # Preparar la ventana
        window = FileInformation(input_file, widget)
        width = 555
        height = 500

        # Abrir la seguiente ventana
        self.open_window(window, widget,  width, height)
        
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

        
    
    def add_types(self, element :object,  input_file :dict):
        for content in input_file["content_type"]:
            element.addItem(content)


