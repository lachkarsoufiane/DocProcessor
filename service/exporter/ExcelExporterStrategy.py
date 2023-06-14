from interface.IExporter import IExporter
import json
from pathlib import Path
import pandas as pd


class ExcelExporterStrategy(IExporter):

    def export(content, config: dict) -> bool:

        mode_type = 'w'
        sheet = None

        try:
            config = config["exporter_config"]
            export_path = config["path"]
        except:
            raise Exception(
                "Se ha ocurrido un error al leer el fichero de configuracion.")

        try:
            # Deserializar el contenido
            content = json.loads(content)
        except:
            raise Exception(
                "El contenido no esta en el formato correcto (Json).")

        try:
            # comprobar si el fichero existe, para que no sobre escriba
            export_path = Path(export_path)
            if export_path.is_file():
                mode_type = 'a'
                sheet = 'new'

            with pd.ExcelWriter(export_path, mode=mode_type, if_sheet_exists=sheet) as writer:
                df = pd.DataFrame(data=content)
                df.to_excel(writer, sheet_name="fichero")
        except Exception as e:
            raise Exception(
                "Se ha ocurrido un error al intentar guardar el archivo.")

        return True
