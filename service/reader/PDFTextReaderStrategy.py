from interface.IReader import IReader
import pdfplumber


class PDFTextReaderStrategy(IReader):

    def read(config: dict) -> str:
        pages = []
        content = ""
        # Ententar leer el fichero de configuraci'on
        try:
            file_config = config['reader_config']
            file_path = file_config['path']
            first_page = file_config['first_page']
            last_page = file_config['last_page']
        except KeyError:
            raise Exception(
                "La configuracion no contiene la información suficiente.")
        except Exception as e:
            raise Exception(
                "Error al leer el contenedo del fichero de configuración: ", e)

        # Abrir el documento
        try:
            file = pdfplumber.open(file_path)
        except:
            raise Exception("Error al abrir el fichero.")

        # Leer depende de las paginas determinadas por el usuario
        try:
            if last_page or last_page != "":
                for i in range((first_page), last_page+1):
                    pages.append(i)
            elif first_page is None or first_page == "":
                for i, page in enumerate(file.pages):
                    pages.append(i+1)
            else:
                pages.append(first_page)

            for page in pages:
                content += f"\n{file.pages[page - 1].extract_text()}"
        except IndexError:
            raise Exception(
                "Al leer el fichero. La pagina no existe en el fichero.")
        except Exception as e:
            raise Exception("Al leer el fichero: ", e)
        file.close()

        return content
