from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QPushButton, QApplication
from PyQt5 import uic

class FileType(QMainWindow):
    def __init__(self, input_file :dict):
        super(FileType, self).__init__()
        
        # Leer la UI
        uic.loadUi('./views/FileType.ui', self)

        # Definir widgets
        # self.combo_type_content = self.findChild(QComboBox, 'combo_file_type')
        # self.button_next = self.findChild(QPushButton, 'button_next')

        # self.button_next.clicked.connect(self.next_view)
        # self.add_content(self.combo_type_content, input_file)

        # Mostrar la app
        # self.show()
        

        

    # def next_view(self):
    #     self.content = self.combo_type_content.currentText()
    #     self.close()
    #     return self.content
    
    
    def add_content(self, element :object, input_file :dict):
        for content in input_file["file_type"]:
            element.addItem(content)
    

