from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QPushButton, QApplication
from PyQt5 import uic

class MainWindows(QMainWindow):
    def __init__(self, file :dict):
        super(MainWindows, self).__init__()
        #read ui
        uic.loadUi('./views/MainView.ui', self)

        #define wigets
        self.combo_type_content = self.findChild(QComboBox, 'comboTypeContent')
        self.button_next = self.findChild(QPushButton, 'buttonNext')

        #do something
        self.button_next.clicked.connect(self.NextView)
        self.add_content(self.combo_type_content, file)

        #show the app
        self.show()

    def NextView(self):
        print("entro")

    def add_content(self, element, json_file):
        for f in json_file["content_type"] :
            element.addItem(f)

