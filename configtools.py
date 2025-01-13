import json
import translation

def read_config_translate():
    translation_provider = translation.TranslationProvider()

    config = read_config_from_json("config.json")

    _translate = translation_provider.original_text

    if config:
        lang = config.get("language")
        if lang == "ru":
            _translate = translation_provider.translate_ru
    return _translate

def read_config_from_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def write_config_file(config, file_path="config.json"):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(config, file, ensure_ascii=False, indent=4)

def create_new_config(ui):
    from logger import message_with_timestamp_nn, message, exception_handler

    _translate = read_config_translate()

    try:
        language = ui.lineEdit_4.text()

        config_data = {
            "silence_mode": False,
            "language": language,
            "logs_days": 14,
            "source_path": "C:\\",
            "destination_path": "C:\\",
            "interval": 300,
            "max_copies": 10
        }
        write_config_file(config_data)
        message_with_timestamp_nn(ui, _translate("log_message", "Created a new 'config.json' ") + _translate("log_message", "with the following options:"))
        for key, value in config_data.items():
            message(ui, f"    {key}: {value}")
    except Exception as e:
        exception_handler(ui, type(e), e, e.__traceback__)

def read_config_select_mode(ui):
    from logger import exception_handler

    try:
        config_path = ui.lineEdit_3.text()
        if config_path:
            config = read_config_from_json(config_path)
        else:
            config = read_config_from_json("config.json")
        return config
    except Exception as e:
        exception_handler(ui, type(e), e, e.__traceback__)