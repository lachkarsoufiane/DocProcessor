from service.configuration.ConfigurationFile import ConfigurationFile
import re


class ServiceESCC():

    # Obtener los certificados con sus titulos (Actions) desde un parradfo
    def get_certificate(paragraph, title, certificate_re):
        result = {}
        result[title] = []
        result[title] = certificate_re.findall(paragraph)
        return result

    # Obtener la description del certificado specificado
    def get_certificate_description(paragraph, certificate, certificate_re, stop_re=None):

        # Importar el regex del certificado
        # certificate_re = re.compile(
        #     r'%s' % config["formatter_config"]["certificate"])

        found = False
        stop_looking = None
        end_certificate = None
        description = ""

        for line in paragraph.split("\n"):
            find_certificate = line.find(certificate)

            if found:
                end_certificate = certificate_re.match(line)

            if (stop_re):
                stop_looking = stop_re.match(line)

            if find_certificate >= 0:
                found = True

            if found and stop_looking:
                return description

            if end_certificate:
                return description

            if find_certificate < 0 and found and not end_certificate:
                description += line

        return description

    def get_by_regex_from_line(paragraph, keyword, regex_re):
        result = None
        for line in paragraph.split("\n"):
            find_keyword = line.find(keyword)
            if (find_keyword >= 0):
                if (len(regex_re.findall(line)) > 0):
                    result = regex_re.findall(line)[0]
        return result
