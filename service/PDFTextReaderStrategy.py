from interface.IReader import IReader
import pdfplumber

class PDFTextReaderStrategy(IReader):

    def read(config: dict) -> str:
        file_config = config['file_config']
        file = pdfplumber.open(file_config['file_path'])
        pages = []
        content = ""

        if file_config['last_page']:
            for i in range((file_config['first_page']), file_config['last_page']+1):
                pages.append(i)
        elif file_config['first_page'] is None:
            for i, page in enumerate(file.pages):
                pages.append(i+1)
        else:
            pages.append(file_config['first_page'])
        
        for page in pages:
            content += file.pages[page -1].extract_text()
        return content
