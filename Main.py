from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from views.MainWindows import MainWindows
from service.configuration.ConfigurationFile import ConfigurationFile
import sys
import json

if __name__ == "__main__":
    
    # Importar el fichero de opciones
    json_path = "configuration\inputs.json"
    json_content = ConfigurationFile.import_file(json_path)

    # Inicializar la applicación
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = MainWindows(json_content, widget)
    widget.addWidget(main)
    widget.setFixedHeight(260)
    widget.setFixedWidth(430)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Saliendo")


