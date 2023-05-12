from interface.IReader import IReader
import pdfplumber

class PDFTextReaderStrategy(IReader):

    def read(config: dict) -> str:
        config_info = config['info'][0]
        file = pdfplumber.open(config_info['file_path']);
        content = file.pages[int(config_info['page']) -1].extract_text()
        return content
