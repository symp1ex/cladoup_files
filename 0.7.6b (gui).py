#0.7.6b
import os
import shutil
import time
import threading
import json
import datetime
import sys


def get_language_dict(lang):
    if lang == "ru":
        return {
            "delete_old_copy_0": f"Удалена копия",
            "delete_old_copy_1": f"вместе с папкой",
            "create_new_copy_0": f"Сделана копия",
            "create_new_copy_1": f"в папку",
            "stop_app": f"Работа программы остановлена.",
            "error_positive_interval": f"Ошибка: интервал должен быть положительным числом.",
            "error_positive_interval_input": f"Ошибка: введите целое число для интервала.",
            "error_positive_max_cop": f"Ошибка: количество копий должно быть положительным числом.",
            "error_positive_max_cop_input": f"Ошибка: введите целое число для количества копий.",
            "error_not_valid_path_input_1": f"не является допустимым путем. Пожалуйста, укажите путь к папке или файлу.",
            "continue_manual_mode": "Вы можете продолжить работу в ручном режиме.",
            "error_does_not_exist": f"Ошибка: указанный путь не существует:",
            "error_not_valid_path_0": f"Ошибка: значение",
            "error_not_valid_path_1": f"не является допустимым путем.",
            "continue_manual_mode_or_to_correct_config": "Вы можете продолжить работу в ручном режиме или исправить файл конфигурации.",
            "error_param_int_num_1": "должно быть целым числом.",
            "error_int_positive_num": f"должно быть положительным целым числом.",
            "error": f"Ошибка:",
            "error_param_positive_num_1": f"должно быть положительным числом.",
            "config_found": f"Найден файл конфигурации. Копирование будет выполнено по следующим параметрам:",
            "error_to_correct_config": f"Ошибка: Исправьте файл конфигурации.",
            "input_auto_or_enter": "\nВведите команду 'auto', 'create_cfg' или нажмите Enter для продолжения в ручном режиме: ",
            "input_reset_stop_copy": "Введите 'reset', чтобы остановить копирование:\n",
            "error_not_enough_data": f"Ошибка: недостаточно данных в файле конфигурации. Исправьте файл конфигурации или введите параметры вручную.",
            "config_incorrect_data": f"Ошибка: файл конфигурации содержит неверный формат данных. Исправьте файл конфигурации или введите параметры вручную.",
            "input_source_copy": f"Введите путь к папке\файлам для копирования: ",
            "input_destination_copy": f"Введите путь для сохранения копии: ",
            "input_interval_in_sec": "Введите интервал в секундах для копирования: ",
            "input_max_copies": "Введите количество одновременно хранимых копий: ",
            "config_is_manual": f"Следующие параметры для копирования были введены вручную: ",
            "source_path_manual": f"    Исходный путь:",
            "destination_path_manual": f"    Путь для сохранения копии:",
            "interval_manual_0": f"    Интервал копирования:",
            "interval_manual_1": f"секунд",
            "max_copies_manual": f"    Количество хранимых копий:",
            "start_copy_manual": "\nДля запуска копирования введите 'start', для остановки введите 'reset':\n",
            "error_not_correct_input": f"Ошибка: неправильный ввод. Повторите запрос.",
            "help_auto": "\nauto - копирование в авто-режиме с параметрами из 'config.json'",
            "help_reset": "reset - остановка работы программы и возврат к началу",
            "help_new_cfg": "create_cfg - создание нового 'config.json'",
            "config_invalid_data": f"Ошибка: файл конфигурации содержит неверный формат данных. Вы можете продолжить в ручном режиме.",
            "log_new_config": f"Создан новый 'config.json'",
            "error_empty_folder": f"Ошибка: Исходная папка не может быть пустой.",
            "error_source_equals_distination": f"Ошибка: Путь до источника не может совпадать с путём для сохранения.",
            "error_exception": "ОШИБКА: произошло исключение"
        }
    else:
        return {
            "delete_old_copy_0": f"Removed copy",
            "delete_old_copy_1": f"along with the folder",
            "create_new_copy_0": f"Copy created",
            "create_new_copy_1": f"to a folder",
            "stop_app": f"The program has been stopped.",
            "error_positive_interval": f"Error: interval must be a positive number.",
            "error_positive_interval_input": f"Error: Please enter an integer for the interval.",
            "error_positive_max_cop": f"Error: number of copies must be a positive number.",
            "error_positive_max_cop_input": f"Error: Enter an integer for the number of copies.",
            "error_not_valid_path_input_1": f"is not a valid path. Please provide the path to the folder or file.",
            "continue_manual_mode": "You can continue to work in manual mode.",
            "error_does_not_exist": f"Error: The specified path does not exist:",
            "error_not_valid_path_0": f"Error: value",
            "error_not_valid_path_1": f"is not a valid path.",
            "continue_manual_mode_or_to_correct_config": "You can continue to work manually or fix the configuration file.",
            "error_param_int_num_1": "must be an integer.",
            "error_int_positive_num": f"must be a positive integer.",
            "error": f"Error:",
            "error_param_positive_num_1": f"must be a positive number.",
            "config_found": f"Found configuration file. Copying will be performed according to the following parameters:",
            "error_to_correct_config": f"Error: Correct the configuration file.",
            "input_auto_or_enter": "\nEnter the command 'auto', 'create_cfg' or press Enter to continue in manual mode: ",
            "input_reset_stop_copy": "Type 'reset' to stop copying:\n",
            "error_not_enough_data": f"Error: Not enough data in configuration file. Correct the configuration file or enter the parameters manually.",
            "config_incorrect_data": f"Error: The configuration file contains an invalid data format. Correct the configuration file or enter the parameters manually.",
            "input_source_copy": f"Enter the path to the folder/files to copy: ",
            "input_destination_copy": f"Enter the path to save the copy: ",
            "input_interval_in_sec": "Enter the interval in seconds for copying: ",
            "input_max_copies": "Enter the number of copies to keep simultaneously: ",
            "config_is_manual": f"The following parameters for copying have been entered manually: ",
            "source_path_manual": f"    Source path:",
            "destination_path_manual": f"    Path to save copy:",
            "interval_manual_0": f"    Copy Interval:",
            "interval_manual_1": f"seconds",
            "max_copies_manual": f"    Number of copies to keep:",
            "start_copy_manual": "\nTo start copying type 'start', to stop type 'reset':\n",
            "error_not_correct_input": f"Error: invalid input. Repeat request.",
            "help_auto": "\nauto - copying in auto mode with parameters from 'config.json'",
            "help_reset": "reset - stop the program and return to the beginning",
            "help_new_cfg": "create_cfg - creation of a new 'config.json'",
            "config_invalid_data": f"Error: The configuration file contains an invalid data format. You can continue manually.",
            "log_new_config": f"New 'config.json' created",
            "error_empty_folder": f"Error: Source folder cannot be empty.",
            "error_source_equals_distination": "Error: The path to the source cannot be the same as the path to save.",
            "error_exception": "ERROR: An exception occurred"
        }


def read_config_from_json_not_err_mess(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_config_lang():
    json_file = os.path.join(os.getcwd(), "config.json")
    config = read_config_from_json_not_err_mess(json_file)
    if config:
        lang = config.get("language")
        lang_dict = get_language_dict(lang)
    else:
        lang_dict = get_language_dict("en")
    return lang_dict


def read_config_from_json(json_file):
    lang_dict = read_config_lang()
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        log_with_timestamp_nn(f"Error: Configuration file not found. You can continue manually.")
        return None
    except json.JSONDecodeError:
        log_with_timestamp_nn(lang_dict["config_invalid_data"])
        return None
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)


def create_config_file(config_data, file_path="config.json"):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(config_data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)


def hide_console_window():
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def get_log_file_path():
    current_dir = os.getcwd()
    return os.path.join(current_dir, "log.txt")


def write_to_log_file(message):
    log_file_path = get_log_file_path()
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")
        print(message)


def log_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("[%d-%m-%y %H-%M-%S]")
    write_to_log_file(f"{timestamp} {message}")


# добавляем в лог запись, но с переносом строки пере меткой времени
def log_with_timestamp_nn(message):
    timestamp = datetime.datetime.now().strftime("[%d-%m-%y %H-%M-%S]")
    write_to_log_file(f"\n{timestamp} {message}")

def exception_handler(exc_type, exc_value, exc_traceback):
    lang_dict = read_config_lang()
    log_with_timestamp(f"{lang_dict['error_exception']} - {exc_value}")
    # Вызываем стандартный обработчик исключений для вывода на экран
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

def copy_files(source_path, destination_path, interval, max_copies, stop_event):
    copies_info = {}  # Словарь для хранения информации о сделанных копиях
    copy_count = 1
    delete_copy_count = 1
    lang_dict = read_config_lang()

    try:
        while not stop_event.is_set():
            copy_folder_name = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
            copy_folder_path = os.path.join(destination_path, copy_folder_name)

            os.makedirs(copy_folder_path)
            copies_info[copy_folder_path] = time.time()

            if len(copies_info) > max_copies:
                oldest_copy_path = min(copies_info, key=copies_info.get)
                del copies_info[oldest_copy_path]
                shutil.rmtree(oldest_copy_path, ignore_errors=True)
                log_with_timestamp(
                    f"{lang_dict['delete_old_copy_0']} {delete_copy_count} {lang_dict['delete_old_copy_1']} '{oldest_copy_path}'")
                delete_copy_count += 1

            if os.path.isfile(source_path):
                # Если указан конкретный файл, копируем его
                shutil.copy2(source_path, copy_folder_path)
            else:
                for root, dirs, files in os.walk(source_path):
                    relative_path = os.path.relpath(root, source_path)
                    destination_dir = os.path.join(copy_folder_path, relative_path)
                    os.makedirs(destination_dir, exist_ok=True)
                    for file in files:
                        source_file = os.path.join(root, file)
                        destination_file = os.path.join(destination_dir, file)
                        shutil.copy2(source_file, destination_file)

            log_with_timestamp(
                f"{lang_dict['create_new_copy_0']} {copy_count} {lang_dict['create_new_copy_1']} '{copy_folder_path}'")
            copy_count += 1

            if not stop_event.wait(interval):
                continue
            else:
                log_with_timestamp(lang_dict["stop_app"])
                break
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)


def get_valid_path_source_for_manual(prompt):
    try:
        lang_dict = read_config_lang()
        while True:
            path = input(prompt)
            if is_reset_command(path):
                return path

            path = os.path.expandvars(path)  # обработка переменных сред

            if os.path.exists(path):  # Проверяем, существует ли путь (файл или папка)
                if os.path.isdir(path):  # Проверяем, является ли путь папкой
                    contents = os.listdir(path)  # Получаем содержимое папки
                    if not contents:  # Если содержимое пусто, выдаем ошибку
                        log_with_timestamp(f"{lang_dict['error_empty_folder']} '{path}'")
                    else:
                        return os.path.abspath(path)  # Возвращаем абсолютный путь к файлу или папке
                else:
                    return os.path.abspath(path)  # Возвращаем абсолютный путь к файлу или папке
            else:
                log_with_timestamp(f"{lang_dict['error_does_not_exist']} {path}")
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)


def get_valid_path_destination_for_manual(prompt, source_path):
    lang_dict = read_config_lang()
    try:
        while True:
            path = input(prompt)
            if is_reset_command(path):
                return path

            path = os.path.expandvars(path)

            if path == source_path:
                log_with_timestamp(lang_dict["error_source_equals_distination"])
            elif path.startswith(source_path + os.path.sep):
                log_with_timestamp(lang_dict["error_source_equals_distination"])
            else:
                try:
                    os.makedirs(path, exist_ok=True)
                    return os.path.abspath(path)
                except OSError:
                    log_with_timestamp(f"{lang_dict['error_not_valid_path_0']} '{path}' {lang_dict['error_not_valid_path_1']}")
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)

def get_valid_interval_for_manual(prompt):
    lang_dict = read_config_lang()
    while True:
        interval = input(prompt)
        if is_reset_command(interval):
            return interval
        try:
            interval = int(interval)
            if interval > 0:
                return interval
            log_with_timestamp(lang_dict["error_positive_interval"])
        except ValueError:
            log_with_timestamp(lang_dict["error_positive_interval_input"])
        except Exception as e:
            exception_handler(type(e), e, e.__traceback__)


def get_valid_max_copies_for_manual(prompt):
    lang_dict = read_config_lang()
    while True:
        max_copies = input(prompt)
        if is_reset_command(max_copies):
            return max_copies
        try:
            max_copies = int(max_copies)
            if max_copies > 0:
                return max_copies
            log_with_timestamp(lang_dict["error_positive_max_cop"])
        except ValueError:
            log_with_timestamp(lang_dict["error_positive_max_cop_input"])
        except Exception as e:
            exception_handler(type(e), e, e.__traceback__)


def validate_path_source_for_auto(path):
    json_file = os.path.join(os.getcwd(), "config.json")
    lang_dict = read_config_lang()
    try:
        if not isinstance(path, str):
            log_with_timestamp(f"{lang_dict['error_does_not_exist']} {path}")
            log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
            copy_is_ui(json_file)

        path = os.path.expandvars(path)

        if os.path.exists(path):
            if os.path.isdir(path):  # Проверяем, является ли путь папкой
                contents = os.listdir(path)
                if not contents:
                    log_with_timestamp(f"{lang_dict['error_empty_folder']} '{path}'")
                    log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
                    copy_is_ui(json_file)
                else:
                    return os.path.abspath(path)
            else:
                return os.path.abspath(path)
        else:
            log_with_timestamp(f"{lang_dict['error_does_not_exist']} {path}")
            log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
            copy_is_ui(json_file)
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)
        copy_is_ui(json_file)


def validate_path_destination_for_auto(path, source_path):
    json_file = os.path.join(os.getcwd(), "config.json")
    lang_dict = read_config_lang()
    try:
        if not isinstance(path, str):
            log_with_timestamp(f"{lang_dict['error_not_valid_path_0']} '{path}' {lang_dict['error_not_valid_path_1']}")
            log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
            copy_is_ui(json_file)

        path = os.path.expandvars(path)

        if path == source_path:
            log_with_timestamp(lang_dict["error_source_equals_distination"])
            log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
            copy_is_ui(json_file)
        elif path.startswith(source_path + os.path.sep):
            log_with_timestamp(lang_dict["error_source_equals_distination"])
            log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
            copy_is_ui(json_file)
        else:
            try:
                os.makedirs(path, exist_ok=True)
                return os.path.abspath(path)
            except OSError:
                log_with_timestamp(f"{lang_dict['error_not_valid_path_0']} '{path}' {lang_dict['error_not_valid_path_1']}")
                log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
                copy_is_ui(json_file)
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)
        copy_is_ui(json_file)

def validate_positive_integer_for_auto(value, param_name):
    json_file = os.path.join(os.getcwd(), "config.json")
    lang_dict = read_config_lang()
    if value == True:
        log_with_timestamp(f"{lang_dict['error']} '{param_name}' {lang_dict['error_param_int_num_1']}")
        log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
        copy_is_ui(json_file)
    else:
        try:
            value = int(value)
            if value > 0:
                return value
            else:
                log_with_timestamp(f"{lang_dict['error']} '{param_name}' {lang_dict['error_param_positive_num_1']}")
                log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
                copy_is_ui(json_file)
        except ValueError:
            log_with_timestamp(f"{lang_dict['error']} '{param_name}' {lang_dict['error_param_int_num_1']}")
            log_with_timestamp(lang_dict["continue_manual_mode_or_to_correct_config"])
            copy_is_ui(json_file)
        except Exception as e:
            exception_handler(type(e), e, e.__traceback__)
            copy_is_ui(json_file)


def validate_path_source_for_silence(path):
    lang_dict = read_config_lang()
    try:
        if not isinstance(path, str):
            log_with_timestamp(f"{lang_dict['error_does_not_exist']} {path}")
            log_with_timestamp(lang_dict["stop_app"])
            sys.exit()

        path = os.path.expandvars(path)

        if os.path.exists(path):
            if os.path.isdir(path):  # Проверяем, является ли путь папкой
                contents = os.listdir(path)
                if not contents:
                    log_with_timestamp(f"{lang_dict['error_empty_folder']} '{path}'")
                    log_with_timestamp(lang_dict["stop_app"])
                    sys.exit()
                else:
                    return os.path.abspath(path)
            else:
                return os.path.abspath(path)
        else:
            log_with_timestamp(f"{lang_dict['error_does_not_exist']} {path}")
            log_with_timestamp(lang_dict["stop_app"])
            sys.exit()
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)
        sys.exit()


def validate_path_destination_for_silence(path, source_path):
    lang_dict = read_config_lang()
    if not isinstance(path, str):
        log_with_timestamp(
            f"{lang_dict['error_not_valid_path_0']} '{path}' {lang_dict['error_not_valid_path_input_1']}")
        log_with_timestamp(lang_dict["stop_app"])
        sys.exit()

    path = os.path.expandvars(path)

    if path == source_path:
        log_with_timestamp(lang_dict["error_source_equals_distination"])
        log_with_timestamp(lang_dict["stop_app"])
        sys.exit()
    elif path.startswith(source_path + os.path.sep):
        log_with_timestamp(lang_dict["error_source_equals_distination"])
        log_with_timestamp(lang_dict["stop_app"])
        sys.exit()
    else:
        try:
            os.makedirs(path, exist_ok=True)
            return os.path.abspath(path)
        except OSError:
            log_with_timestamp(f"{lang_dict['error_not_valid_path_0']} '{path}' {lang_dict['error_not_valid_path_1']}")
            log_with_timestamp(lang_dict["stop_app"])
            sys.exit()
        except Exception as e:
            exception_handler(type(e), e, e.__traceback__)
            log_with_timestamp(lang_dict["stop_app"])
            sys.exit()


def validate_positive_integer_for_silence(value, param_name):
    lang_dict = read_config_lang()
    if value == True:
        log_with_timestamp(f"{lang_dict['error']} '{param_name}' {lang_dict['error_int_positive_num']}")
        log_with_timestamp(lang_dict["stop_app"])
        sys.exit()
    else:
        try:
            value = int(value)
            if value > 0:
                return value
            else:
                log_with_timestamp(f"{lang_dict['error']} '{param_name}' {lang_dict['error_param_positive_num_1']}")
                log_with_timestamp(lang_dict["stop_app"])
                sys.exit()
        except ValueError:
            log_with_timestamp(f"{lang_dict['error']} '{param_name}' {lang_dict['error_int_positive_num']}")
            log_with_timestamp(lang_dict["stop_app"])
            sys.exit()
        except Exception as e:
            exception_handler(type(e), e, e.__traceback__)
            sys.exit()


def is_reset_command(text):
    return text.lower() == "reset"


def is_auto_command(text):
    return text.lower() == "auto"


def create_cfg_command(text):
    return text.lower() == "create_cfg"


def copy_is_silence(json_file):
    hide_console_window()
    config = read_config_from_json(json_file)
    lang_dict = read_config_lang()
    try:
        if config:
            log_with_timestamp_nn(lang_dict["config_found"])

            for key, value in config.items():
                write_to_log_file(f"    {key}: {value}")

            source_path = validate_path_source_for_silence(config.get("source_path"))
            destination_path = validate_path_destination_for_silence(config.get("destination_path"), source_path)
            interval = validate_positive_integer_for_silence(config.get("interval"), "interval")
            max_copies = validate_positive_integer_for_silence(config.get("max_copies"), "max_copies")

            if source_path and destination_path and interval and max_copies:
                stop_event = threading.Event()
                copy_thread = threading.Thread(target=copy_files,
                                               args=(source_path, destination_path, interval, max_copies, stop_event))
                copy_thread.start()
            else:
                log_with_timestamp(lang_dict["error_to_correct_config"])
                sys.exit()
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)
        sys.exit()


def copy_is_ui(json_file):
    lang_dict = read_config_lang()
    stop_event = threading.Event()
    while True:
        try:
            user_input = input(lang_dict["input_auto_or_enter"])

            if is_auto_command(user_input):
                config = read_config_from_json(json_file)
                if config:
                    silence_mode = config.get("silence_mode")
                    if silence_mode == True:
                        copy_is_silence(json_file)
                    elif silence_mode == False:
                        if config:
                            log_with_timestamp_nn(lang_dict["config_found"])

                            for key, value in config.items():
                                write_to_log_file(f"    {key}: {value}")

                            source_path = validate_path_source_for_auto(config.get("source_path"))
                            destination_path = validate_path_destination_for_auto(config.get("destination_path"), source_path)
                            interval = validate_positive_integer_for_auto(config.get("interval"), "interval")
                            max_copies = validate_positive_integer_for_auto(config.get("max_copies"), "max_copies")

                            if source_path and destination_path and interval and max_copies:
                                stop_event = threading.Event()
                                copy_thread = threading.Thread(target=copy_files, args=(
                                source_path, destination_path, interval, max_copies, stop_event))
                                copy_thread.start()

                                while True:
                                    if copy_thread.is_alive():
                                        stop_confirmation = input(lang_dict["input_reset_stop_copy"])
                                        if is_reset_command(stop_confirmation):
                                            stop_event.set()
                                            copy_thread.join()
                                            break
                                    else:
                                        break

                            else:
                                log_with_timestamp(lang_dict["error_not_enough_data"])
                    else:
                        log_with_timestamp_nn(lang_dict["config_incorrect_data"])
                        continue

            elif create_cfg_command(user_input):
                config_data = {
                    "silence_mode": False,
                    "language": "en",
                    "source_path": "C:\\",
                    "destination_path": "D:\\",
                    "interval": 600,
                    "max_copies": 5
                }
                create_config_file(config_data)
                log_with_timestamp(lang_dict["log_new_config"])
                continue

            else:
                source_path = get_valid_path_source_for_manual(lang_dict["input_source_copy"])
                if source_path == "reset":
                    log_with_timestamp(lang_dict["stop_app"])
                    continue

                destination_path = get_valid_path_destination_for_manual(lang_dict["input_destination_copy"], source_path)
                if destination_path == "reset":
                    log_with_timestamp(lang_dict["stop_app"])
                    continue


                interval = get_valid_interval_for_manual(lang_dict["input_interval_in_sec"])
                if interval == "reset":
                    log_with_timestamp(lang_dict["stop_app"])
                    continue

                max_copies = get_valid_max_copies_for_manual(lang_dict["input_max_copies"])
                if max_copies == "reset":
                    log_with_timestamp(lang_dict["stop_app"])
                    continue

                log_with_timestamp_nn(lang_dict["config_is_manual"])
                write_to_log_file(f"{lang_dict['source_path_manual']} {source_path}")
                write_to_log_file(f"{lang_dict['destination_path_manual']} {destination_path}")
                write_to_log_file(f"{lang_dict['interval_manual_0']} {interval} {lang_dict['interval_manual_1']}")
                write_to_log_file(f"{lang_dict['max_copies_manual']} {max_copies}")

                start_confirmation = input(lang_dict["start_copy_manual"])
                if is_reset_command(start_confirmation):
                    log_with_timestamp(lang_dict["stop_app"])
                    continue
                elif start_confirmation.lower() == "start":
                    stop_event = threading.Event()
                    copy_thread = threading.Thread(target=copy_files, args=(
                    source_path, destination_path, interval, max_copies, stop_event))
                    copy_thread.start()

                    while True:
                        if copy_thread.is_alive():
                            stop_confirmation = input(lang_dict["input_reset_stop_copy"])
                            if stop_confirmation.lower() == "reset":
                                stop_event.set()
                                copy_thread.join()
                                break
                        else:
                            break
                else:
                    log_with_timestamp(lang_dict["error_not_correct_input"])
        except KeyboardInterrupt:
            stop_event.set()
            log_with_timestamp(lang_dict["stop_app"])
            continue
        except Exception as e:
            exception_handler(type(e), e, e.__traceback__)
            continue


def main():
    lang_dict = read_config_lang()
    try:
        help1 = [
            lang_dict["help_auto"],
            lang_dict["help_new_cfg"],
            lang_dict["help_reset"]
        ]

        for help0 in help1:
            print(help0)

        json_file = os.path.join(os.getcwd(), "config.json")
        config = read_config_from_json(json_file)
        if config:
            silence_mode = config.get("silence_mode")
            if silence_mode == True:
                copy_is_silence(json_file)
            elif silence_mode == False:
                copy_is_ui(json_file)
            else:
                log_with_timestamp_nn(lang_dict["config_incorrect_data"])
                copy_is_ui(json_file)
        else:
            copy_is_ui(json_file)
    except Exception as e:
        exception_handler(type(e), e, e.__traceback__)


if __name__ == "__main__":
    main()
