import json


def get_strategy(options: dict, title) -> dict:
    try:
        current_opts = options[title]
        data = {}
        # mostrar opciones
        print("Introduce el tipo de " + title)
        for key, opt in current_opts.items():
            print(opt + ": " + key)

        result = input("-> ")
        if (result in options[title]):
            data[title] = result

        return data
    except Exception as ex:
        raise (ex)


def get_config(option_config: dict, title: str,  strategy_name: str) -> dict:
    try:
        data = {}
        print("Introduce la configuración del " + strategy_name)
        current_config = option_config[title]
        for key, config in current_config.items():
            data[key] = input(config + ": ")
        return data
    except Exception as ex:
        raise (ex)
