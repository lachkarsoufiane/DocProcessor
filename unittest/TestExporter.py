import json
import unittest
from service.exporter.ExcelExporterStrategy import ExcelExportStrategy

class TestExporter(unittest.TestCase):

    def test_file_export(self):
        content = "Hello World"
        
        # Convertir el contenido a json pq el exporter lo recibe como json
        content = json.dumps(content)
        
        # La parte que necesita del fichero de configuración
        config = {"export_config": {
        "path": "C:/Users/beca_is3/Desktop/Files/Python/File Processor/ProcessorWithViews/exports/test.xlsx"
    }}
        # Recorrer el metodo 
        ExcelExportStrategy.export(content, config)
