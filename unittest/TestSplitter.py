import unittest
from service.ParagraphRegexSplitterStrategy import ParagraphRegexSplitterStrategy
from service.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy

class TestSplitter(unittest.TestCase):

    def test_keyword_splitter(self):
        content = "Document: lorem texto text hello world in the faer of the lord of thron, Document: Hello galaxy of the mandelorian."
        config = {
            "file_path": "C:/Users/beca_is3/Desktop/Files/Python/File Processor/ProcessorWithViews/files/test_file.pdf", 
            "page_number": 3,
            "start_keyword": "Document:",
            "end_keyword" : None 
        }
        print(ParagraphKeywordSplitterStrategy.split_content(content, config))