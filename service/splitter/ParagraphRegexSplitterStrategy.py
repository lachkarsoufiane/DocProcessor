from interface.ISplitter import ISplitter
import re
import json

class ParagraphRegexSplitterStrategy(ISplitter):
    def split_content(content, config):

        config = config["process_config"]
        
        start = re.compile(r'%s' % config["start_key"])
        end = re.compile(r'%s' % config["end_key"])


        end = start if end is None else end 
        paragraphs = {}
        paragraph = ""
        current_title = None
        content_list = content.split("\n")
        
        for i, line in enumerate(content_list):

            # Si estamos en la ultima linea
            if(i == len(content_list)-1 or end.match(line)):
                paragraphs[current_title] = paragraph
                break
            
            if(start.match(line) and line != current_title and current_title ):
                paragraphs[current_title] = paragraph
                paragraph = ""
                current_title = line
            
            if(start.match(line)):
                current_title = re.search(start, line).group(1)
                paragraphs[current_title] = {}
            
            if(current_title and not start.match(line)):
                paragraph += line + " \n"


        result = json.dumps(paragraphs)
        return result