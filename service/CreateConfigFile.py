from interface.ICreateConfig import ICreateConfig
class CreateConfigFile(ICreateConfig):
    

    def create_strategy_config(data) -> dict:
        data['strategy'] = []
        print("Introduce los datos de configuración:")
        reader = input("¿Como quieres leer los datos?\n1- Consola\n2- Archivo\n")
        printer = input("¿Como quieres imprimir los datos?\n1- Consola\n2- Archivo\n")

        data['strategy'].append({
            'reader' : int(reader),
            'printer' : int(printer)
        })

        return data

    def create_info_config(data) -> dict:
        data['info'] = []
        strategy = data['strategy'][0]

        if(strategy['reader'] == 2):
            print("Introduce la configuración del archivo:")
            file_path = "./files/" + input("¿Cuál es el nombre del archivo?\n")
            page = input("¿Que páginas quieres leer?\n1- Una página\n2- Varias páginas\n3- Todas las paginas\n")
            final_page = CreateConfigFile.page_number(page)
            file_output = None
            if(strategy['printer'] == 2):
                file_output = input("¿Como quieres que se llame el fichero de salida?\n")

            if(len(final_page) > 1 ):
                if(final_page != None):
                    data['info'].append({
                        "file_path" : file_path,
                        "page_init" : final_page[0],
                        "page_end" : final_page[1],
                        "file_output" : file_output
                    })
                else: 
                     data['info'].append({
                        "file_path" : file_path,
                        "page_init" : final_page[0],
                        "page_end" : final_page[1],
                    })
            else:
                if(final_page != None):
                    data['info'].append({
                        "file_path" : file_path,
                        "page" : final_page,
                        "file_output" : file_output
                    })
                else:
                    data['info'].append({
                        "file_path" : file_path,
                        "page" : final_page,
                    })
        return data

        
    def page_number(page_number: str) -> str:
        if(page_number == '1'):
            page = input("¿Que página quiere leer?\n")
            
        elif(page_number == '2'):
            page_init = input("¿Primera página?\n")
            page_end = input("¿Página final?\n")

            return page_init + page_end
        else:
            page = '0'

        return page