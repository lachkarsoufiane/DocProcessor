import unittest
from service.PDFTextReaderStrategy import PDFTextReaderStrategy

class TestReader(unittest.TestCase):
    def test_read(self):
        config = {"conf_file": {
                    "file_path": "./files/test_file.pdf", 
                    "page_number": 1,
                    "start_keyword": "Document:",
                    "end_keyword" : None 
        }}
        file_path = "./files/test_file.pdf"
        result = PDFTextReaderStrategy.read(config)
        expected_result = "Test 123"

        self.assertEqual(result, expected_result)
