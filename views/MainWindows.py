import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QComboBox, QPushButton, QApplication
from PyQt5 import uic

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        #read ui
        uic.loadUi('./views/MainView.ui', self)

        #define wigets
        self.combo_type_content = self.findChild(QComboBox, 'comboTypeContent')
        self.button_next = self.findChild(QPushButton, 'buttonNext')

        #do something
        self.button_next.clicked.connect(self.NextView)

        self.combo_type_content.addItem("Archivo")
        self.combo_type_content.addItem("Api")

        #show the app
        self.show()

    def NextView(self):
        print("entro")

app = QApplication(sys.argv)
UIWindows = MainWindows()
app.exec_()