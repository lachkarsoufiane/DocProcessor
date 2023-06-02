import unittest
from service.reader.PDFTextReaderStrategy import PDFTextReaderStrategy
from service.reader.TextFileReaderStrategy import TextFileReaderStrategy

class TestReader(unittest.TestCase):
    def test_pdf_read(self):
        config = {"reader_config": {
        "path": "C:/Users/beca_is3/Desktop/Files/Python/File Processor/ProcessorWithViews/files/test_file.pdf",
        "first_page": 1,
        "last_page": None
    }}
        result = PDFTextReaderStrategy.read(config)
        expected_result = "\nTest 123"

        self.assertEqual(result, expected_result)

    def text_text_read(self):
        config = {"reader_config": {
        "path": "C:/Users/beca_is3/Desktop/Files/Python/File Processor/ProcessorWithViews/files/test_file.txt"
    }}
        result = TextFileReaderStrategy.read(config)
        expected_result = ""
        self.assertEqual(result, expected_result)

    