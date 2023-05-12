import unittest
from service.PDFTextReaderStrategy import PDFTextReaderStrategy

class TestReader(unittest.TestCase):
    def test_read(self):
        file_path = "./files/test_file.pdf"
        result = PDFTextReaderStrategy.read(file_path)
        expected_result = "Test 123"

        self.assertEqual(result, expected_result)
