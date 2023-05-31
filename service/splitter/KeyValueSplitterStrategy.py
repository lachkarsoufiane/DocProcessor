from interface.ISplitter import ISplitter
import re
import json

class KeyValueSplitterStrategy(ISplitter):

    def split_content(content :str, config :dict):

            config = config["splitter_config"]
            regex= re.compile(r'%s' % config["key_regex"])

            sections = re.split(regex, content)
            # Quitar el primer elemento
            sections.pop(0)
            keys = re.findall(regex, content)
            result = {}
            past_keys = 1
            for i in range(len(keys)):       
                section = sections[i+past_keys].strip()
                key = keys[i].replace(":", "")
                if (key not in result):
                    result[key] = section
                    past_keys += 1

            result = json.dumps(result)

            return result