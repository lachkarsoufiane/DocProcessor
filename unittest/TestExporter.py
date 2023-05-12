import unittest
from service.FilePrinterStrategy import FileExportStrategy

class TestExporter(unittest.TestCase):

    def test_file_export(self):
        self.assertTrue(FileExportStrategy.export("./exports/file.txt", "Hello World"))