import unittest
from service.ConsolePrinterStrategy import ConsolePrinterStrategy

class TestPrinter(unittest.TestCase):
    def test_console_print(self):
        content = "Hello World"
        self.assertTrue(ConsolePrinterStrategy.print(content))