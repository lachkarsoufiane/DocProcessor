from interface.IExporter import IExporter
from service.configuration.ConfigurationFile import ConfigurationFile
from collections import namedtuple
import json
from pathlib import Path
import pandas as pd


class ExcelExportStrategy(IExporter):
    
    def export(content, config :dict) -> bool:
        
        config = config["export_config"]
        content = json.loads(content)

        mode_type = 'w'
        sheet = None
        export_path = config["path"]

        # comprobar si el fichero existe, para que no sobre escriba
        export_path = Path(export_path)
        if export_path.is_file():
            mode_type = 'a'
            sheet = 'new'
        try:
            with pd.ExcelWriter(export_path, mode = mode_type, if_sheet_exists=sheet) as writer:
                df = pd.DataFrame(data=content)
                df.to_excel(writer, sheet_name="pagina")
        except Exception as e:
            print(e)
            return False
        return True