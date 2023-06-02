import json
import unittest
from service.splitter.ParagraphKeywordSplitterStrategy import ParagraphKeywordSplitterStrategy


class TestSplitter(unittest.TestCase):

    def test_keyword_splitter(self):
        content = "Document: lorem texto text hello world in the faer of the lord of thron,\nDocument: Hello galaxy of the mandelorian."
        config = {
            "splitter_config": {
                "start_key": "Document:",
                "end_key": None
                }
        }
        expected_result = {"1": "Document: lorem texto text hello world in the faer of the lord of thron, \n", "2": "Document: Hello galaxy of the mandelorian. \n"}
        result = ParagraphKeywordSplitterStrategy.split_content(content, config)
        
        self.assertEqual(result, json.dumps(expected_result))