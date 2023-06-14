import Generator
import json

if __name__ == "__main__":

    config_file = {}
    options_config = {}
    strategy_file = {}
    result_file = {}
    try:
        # Importar el fichero de opciones
        json_path = "generator\opcions.json"
        with open(json_path) as conf_file:
            options = json.load(conf_file)

        options_config = options["config"]

        # Pedir las strategias
        name = input("Nombre del preset: ")

        reader = Generator.get_strategy(options, "reader")
        splitter = Generator.get_strategy(options, "splitter")
        formatter = Generator.get_strategy(options, "formatter")
        exporter = Generator.get_strategy(options, "exporter")

        # Merge las strategias
        strategy_file = strategy_file | reader | splitter | formatter | exporter

        for key, strategy in strategy_file.items():
            config_file[key +
                        "_config"] = Generator.get_config(options_config, strategy, key)

        strategy_file["name"] = name
        result_file = strategy_file | config_file

        with open("presets/"+name+".json", "w") as f:
            json.dump(result_file, f)
    except Exception as ex:
        print(ex)
