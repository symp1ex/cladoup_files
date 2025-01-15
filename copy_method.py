import time
import datetime
import threading
import shutil
import os
import configtools
import logger

def get_copy_data_to_config(ui):
    _translate = configtools.read_config_translate()
    try:
        config = configtools.read_config_select_mode(ui)

        source_path = validate_path_source(ui, config.get("source_path"))
        if source_path:
            destination_path = validate_path_destination(ui, config.get("destination_path"), source_path)
        interval = validate_positive_integer(ui, config.get("interval"), "interval")
        max_copies = validate_positive_integer(ui, config.get("max_copies"), "max_copies")
        return source_path, destination_path, interval, max_copies
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def get_copy_data_to_ui(ui):
    try:
        source_path = validate_path_source(ui, ui.lineEdit.text())
        if source_path:
            destination_path = validate_path_destination(ui, ui.lineEdit_2.text(), source_path)
        interval = validate_positive_integer(ui, ui.spinBox_2.value(), "interval")
        max_copies = validate_positive_integer(ui, ui.spinBox.value(), "max_copies")
        return source_path, destination_path, interval, max_copies
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def start_copy(ui, source_path, destination_path, interval, max_copies):
    ui.stop_copying_and_clean()
    time.sleep(1)
    ui.copy_thread_stop_event = threading.Event()
    _translate = configtools.read_config_translate()

    try:
        if source_path and destination_path and interval and max_copies:
            logger.message_with_timestamp_nn(ui,
                                             f"{_translate('log_message', 'Copying will be performed with the following parameters: ')}")
            logger.message(ui, f"{_translate('log_message', '    Source path:')} '{source_path}'")
            logger.message(ui, f"{_translate('log_message', '    Path to save copy:')} '{destination_path}'")
            logger.message(ui,
                           f"{_translate('log_message', '    Copy Interval:')} {interval} {_translate('log_message', 'sec.')}")
            logger.message(ui, f"{_translate('log_message', '    Number of copies to keep:')} {max_copies}")

            if ui.checkBox.isChecked():
                logger.not_interface_exists = True
                ui.hide_main_window()
            cleanup_folders_in_thread(ui, destination_path, interval, max_copies)
            copy_thread = threading.Thread(target=copy_files,
                                           args=(ui, source_path, destination_path, interval, max_copies,
                                                 ui.copy_thread_stop_event), daemon=True)
            copy_thread.start()
        else:
            logger.message_with_timestamp(ui,
                                          f"{_translate('log_message', 'Select the correct settings for copying.')}")
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def copy_files(ui, source_path, destination_path, interval, max_copies, stop_event):
    copies_info = {}  # Словарь для хранения информации о сделанных копиях
    copy_count = 1
    delete_copy_count = 1
    _translate = configtools.read_config_translate()

    try:
        while not stop_event.is_set():
            copy_folder_name = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
            copy_folder_path = os.path.join(destination_path, copy_folder_name)
            if not os.path.exists(copy_folder_path):  # Проверка существования папки
                os.makedirs(copy_folder_path)
            copies_info[copy_folder_path] = time.time()

            if len(copies_info) > max_copies:
                oldest_copy_path = min(copies_info, key=copies_info.get)
                del copies_info[oldest_copy_path]
                shutil.rmtree(oldest_copy_path, ignore_errors=True)
                logger.message_with_timestamp(ui, f"{_translate('log_message', 'Removed copy')} {delete_copy_count} {_translate('log_message', 'with folder:')} '{oldest_copy_path}'")
                delete_copy_count += 1
                time.sleep(0.2)

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
            logger.message_with_timestamp(ui, f"{_translate('log_message', 'Copy created')} {copy_count} {_translate('log_message', 'to a folder:')} '{copy_folder_path}'")
            copy_count += 1
            if stop_event.wait(interval):
                logger.message_with_timestamp(ui, f"{_translate('log_message', 'The program has been stopped.')}")
                break
            continue
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def validate_path_source(ui, path):
    _translate = configtools.read_config_translate()
    try:
        if not isinstance(path, str):
            logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error: The specified path does not exist:')} '{path}'")
            if logger.not_interface_exists:
                logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                os._exit(1)

        path = os.path.expandvars(path)

        if os.path.exists(path):
            if os.path.isdir(path):  # Проверяем, является ли путь папкой
                contents = os.listdir(path)
                if not contents:
                    logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error: Source folder cannot be empty:')} '{path}'")
                else:
                    return os.path.abspath(path)
            else:
                return os.path.abspath(path)
        else:
            logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error: The specified path does not exist:')} '{path}'")
            if logger.not_interface_exists:
                logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                os._exit(1)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def validate_path_destination(ui, path, source_path):
    _translate = configtools.read_config_translate()
    try:
        if not isinstance(path, str):
            logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error: value')} '{path}' {_translate('log_message', 'is not a valid path.')}")
            if logger.not_interface_exists:
                logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                os._exit(1)

        path = os.path.expandvars(path)

        if path == source_path:
            logger.message_with_timestamp(ui, _translate('log_message', "Error: The path to the source cannot be the same as the path to save"))
            if logger.not_interface_exists:
                logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                os._exit(1)
        elif path.startswith(source_path + os.path.sep):
            logger.message_with_timestamp(ui, _translate('log_message', "Error: The path to the source cannot be the same as the path to save"))
            if logger.not_interface_exists:
                logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                os._exit(1)
        else:
            try:
                os.makedirs(path, exist_ok=True)
                return os.path.abspath(path)
            except OSError:
                logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error: value')} '{path}' {_translate('log_message', 'is not a valid path.')}")
                if logger.not_interface_exists:
                    logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                    os._exit(1)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def validate_positive_integer(ui, value, param_name):
    _translate = configtools.read_config_translate()
    try:
        value = int(value)
        if value > 0:
            return value
        else:
            logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be a positive number.')}")
            if logger.not_interface_exists:
                logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
                os._exit(1)
    except ValueError:
        logger.message_with_timestamp(ui, f"{_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be an integer.')}")
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def is_valid_folder_name(folder_name, date_format):
    try:
        datetime.datetime.strptime(folder_name, date_format)
        return True
    except ValueError:
        return False

def cycle_removed_old_copy(ui, _translate, filtered_folders, folder_path, interval_seconds, stop_event):
    try:
        for folder in filtered_folders:
            folder_path_full = os.path.join(folder_path, folder)
            shutil.rmtree(folder_path_full)
            logger.message_with_timestamp(ui, f"{_translate('log_message', 'Removed old copy from')} \'{folder}\'")
            if stop_event.wait(interval_seconds):
                break
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def cleanup_folders(ui, folder_path, target_count, interval_seconds, stop_event):
    _translate = configtools.read_config_translate()
    try:
        # Получаем список папок в указанной директории
        folders = os.listdir(folder_path)

        # Фильтруем папки, оставляем только те, у которых формат имени соответствует дате и времени
        date_format = "%d-%m-%y %H-%M-%S"
        filtered_folders = [folder for folder in folders if is_valid_folder_name(folder, date_format)]

        # Сортируем папки по дате создания
        filtered_folders.sort(key=lambda x: datetime.datetime.strptime(x, date_format))

        # Проверяем количество папок
        folder_count = len(filtered_folders)

        while not stop_event.is_set():  # запускаем цикл проверки на событие установки удаления
            if folder_count == target_count:
                cycle_removed_old_copy(ui, _translate, filtered_folders, folder_path, interval_seconds, stop_event)
                break
            elif folder_count > target_count:
                # Если количество папок больше целевого, удаляем лишние папки
                folders_to_remove = folder_count - target_count
                for i in range(folders_to_remove):
                    folder_path_full = os.path.join(folder_path, filtered_folders[i])
                    shutil.rmtree(folder_path_full)
                logger.message_with_timestamp(ui, f"{_translate('log_message', 'Removed old copies:')} {folders_to_remove}")
                # Устанавливаем начало списка папок после удаления лишних
                filtered_folders = filtered_folders[folders_to_remove:]
                cycle_removed_old_copy(ui, _translate, filtered_folders, folder_path, interval_seconds, stop_event)
                break
            else:
                # Если количество папок меньше целевого, вычисляем разницу, ожидаем и начинаем удалять с интервалом
                difference = target_count - folder_count
                wait_time = difference * interval_seconds
                if stop_event.wait(wait_time):
                    break
                cycle_removed_old_copy(ui, _translate, filtered_folders, folder_path, interval_seconds, stop_event)
                break
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)

def cleanup_folders_in_thread(ui, folder_path, interval_seconds, target_count):
    _translate = configtools.read_config_translate()
    try:
        ui.delete_thread_stop_event = threading.Event()
        # Создаем новый поток и передаем в него функцию cleanup_folders
        cleanup_thread = threading.Thread(target=cleanup_folders, args=(ui, folder_path, target_count, interval_seconds,
                                                                        ui.delete_thread_stop_event), daemon=True)
        # Запускаем поток
        cleanup_thread.start()
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
        if logger.not_interface_exists:
            logger.message_with_timestamp(ui, _translate('log_message', 'The program has been stopped.'))
            os._exit(1)
