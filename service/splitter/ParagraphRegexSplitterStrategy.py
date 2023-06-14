from interface.ISplitter import ISplitter
import re
import json


class ParagraphRegexSplitterStrategy(ISplitter):

    def split_content(content, config):

        try:

            config = config["splitter_config"]
            sections = []

            start_regex = re.compile(r'%s' % config["start_key"])
            end_regex = re.compile(r'%s' % config["end_key"])

            end_regex = start_regex if end_regex is None or end_regex == "" else end_regex

            start_positions = [match.start()
                               for match in re.finditer(start_regex, content)]
            end_positions = [match.start()
                             for match in re.finditer(end_regex, content)]
            # Add the end position of the last section
            end_positions.append(len(content))

            for i in range(len(start_positions)):
                start = start_positions[i]
                end = min(
                    end_pos for end_pos in end_positions if end_pos > start)
                section = content[start:end].strip()
                sections.append(section)

            result = json.dumps(sections)

            return result

        except IndexError:
            raise Exception(
                "Error al dividir el contenido. Índice fuera de rango.")

        except KeyError:
            raise Exception(
                "Error al dividir el contenido. Clave no encontrada en la configuración.")

        except Exception as e:
            raise Exception("Error al dividir el contenido. ", e)
