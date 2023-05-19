from interface.IFormatter import IFormatter
from service.formatter.ServiceESCC import ServiceESCC
from service.configuration.ConfigurationFile import ConfigurationFile

import re
import json

class ESCCFormatter (IFormatter):

    def format(content) -> str:

         # Importar el contenido del fichero de assets
        asset_file = ConfigurationFile.import_file("./asset/process_settings.json")
        escc_settings = asset_file["escc"]
        certificate_re = re.compile(r'%s' % escc_settings["certificate"])
        manufacturer_re = re.compile(r'%s' % escc_settings["manufacture"])
        extra_re = re.compile(r'%s' % escc_settings["extra"])



        content = json.loads(content)
        result = {}
        for title in content:
            certificates =  ServiceESCC.get_certificate(content[title], title, certificate_re)
            for title in certificates:
                description = ""
                for certificate in certificates[title]:
                    revision = ""
                    manifacturer = ServiceESCC.get_by_regex_from_line(content[title], certificate, manufacturer_re)
                    description = ServiceESCC.get_certificate_description(content[title], certificate, extra_re) 

                    if(certificate.find("rev") >= 0):
                        revision = certificate[certificate.find("rev"):]
                        certificate = certificate[:-4]
                    result[certificate] = {}
                    
                    result[certificate]["Title"] = title
                    result[certificate]["Revision"] = revision
                    result[certificate]["Manufacturer"] = manifacturer
                    result[certificate]["Description"] = description

        result = json.dumps(result)
        return result