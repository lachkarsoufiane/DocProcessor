from interface.IExporter import IExporter
from service.configuration.ConfigurationFile import ConfigurationFile

from pathlib import Path
import pandas as pd


class ExcelExportStrategy(IExporter):
    
    def export(table, config :dict) -> bool:
        mode_type = 'w'
        sheet = None
        export_path = ConfigurationFile.find_value(config, "export_path") 
        
        # comprobar si el fichero existe, para que no sobre escriba
        export_path = Path(export_path)
        if export_path.is_file():
            mode_type = 'a'
            sheet = 'new'
        try:
            with pd.ExcelWriter(export_path, mode = mode_type, if_sheet_exists=sheet ) as writer:
                df = pd.DataFrame(table)
                df.to_excel(writer, sheet_name="pagina")
        except Exception as e:
            print(e)
            return False
        return True