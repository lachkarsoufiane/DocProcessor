from interface.ISplitter import ISplitter
import re
import json

class ParagraphRegexSplitterStrategy(ISplitter):
    
    def split_content(content, config):

        config = config["splitter_config"]
        sections = []

        start_regex = re.compile(r'%s' % config["start_key"])
        end_regex = re.compile(r'%s' % config["end_key"])

        end_regex = end_regex if config["end_key"] else start_regex

        start_positions = [match.start() for match in re.finditer(start_regex, content)]
        end_positions = [match.start() for match in re.finditer(end_regex, content)]
        end_positions.append(len(content))  # Add the end position of the last section
        
        for i in range(len(start_positions)):
            start = start_positions[i]
            end = min(end_pos for end_pos in end_positions if end_pos > start)
            section = content[start:end].strip()
            sections.append(section)
        
        result = json.dumps(sections)
        return result
    