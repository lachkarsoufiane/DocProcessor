from interface.IFormatter import IFormatter
from service.formatter.ServiceESCC import ServiceESCC

import re
import json


class ESCCFormatterStrategy (IFormatter):

    def format(content, config) -> str:

        # Importar el contenido del config
        escc_settings = config["formatter_config"]
        certificate_re = re.compile(r'%s' % escc_settings["certificate"])
        manufacturer_re = re.compile(r'%s' % escc_settings["manufacture"])
        extra_re = re.compile(r'%s' % escc_settings["extra"])
        content = json.loads(content)
        result = []

        # Por cada parrafo, obtenemos los certificados disponibles
        for title in content:
            certificates = ServiceESCC.get_certificate(
                content[title], title, certificate_re)
            # Por cada certificado, coemos la descripci'on, la revision si existe y el manifacturer
            for title in certificates:

                description = ""
                for certificate in certificates[title]:
                    data = {}
                    revision = ""
                    manifacturer = ServiceESCC.get_by_regex_from_line(
                        content[title], certificate, manufacturer_re)
                    description = ServiceESCC.get_certificate_description(
                        content[title], certificate, certificate_re, extra_re)

                    if (certificate.find("rev") >= 0):
                        revision = certificate[certificate.find("rev"):]
                        certificate = certificate[:-4]

                    data["Certificate"] = certificate
                    data["Revision"] = revision
                    data["Action"] = title
                    data["Manifacturer"] = manifacturer
                    data["Description"] = description

                    result.append(data)

        # Convertir el resultado a un json
        result = json.dumps(result)
        return result
