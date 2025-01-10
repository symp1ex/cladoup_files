import datetime
import os
import sys
import traceback
import configtools

not_interface_exists = False  # ставим флаг на отсутствие интерфейса

def clear_logs():
    try:
        # Получаем текущую дату
        current_date = datetime.datetime.now()
        # Определяем дату, старше которой логи будут удаляться
        old_date_limit = current_date - datetime.timedelta(days=30)
        # Удаляем логи старше 30 дней
        for file_name in os.listdir("logs"):
            file_path = os.path.join("logs", file_name)
            file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            if file_creation_time < old_date_limit:
                os.remove(file_path)
    except Exception:
        pass

def get_log_file_path():
    timestamp = datetime.datetime.now().strftime("%d-%m-%y")
    current_dir = os.getcwd()
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file_path = os.path.join(current_dir, "logs", f"{timestamp}.log")
    clear_logs()
    return log_file_path

def write_to_log_file(message):
    log_file_path = get_log_file_path()
    with open(log_file_path, "a", encoding="cp1251") as log_file:
        log_file.write(message + "\n")

def message(ui, message):
    if not not_interface_exists:  # Проверяем флаг отсутствия интерфейса
        update_text_browser(ui, f"{message}")
    write_to_log_file(f"{message}")

def message_with_timestamp(ui, message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]"
    if not not_interface_exists:  # Проверяем флаг отсутствия интерфейса
        update_text_browser(ui, f"{timestamp} {message}")
    write_to_log_file(f"{timestamp} {message}")

# добавляем в лог запись, но с переносом строки перед меткой времени
def message_with_timestamp_nn(ui, message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]"
    if not not_interface_exists:  # Проверяем флаг отсутствия интерфейса
        update_text_browser(ui, f"\n{timestamp} {message}")
    write_to_log_file(f"\n{timestamp} {message}")

def exception_handler(ui, exc_type, exc_value, exc_traceback):
    _translate = configtools.read_config_translate()
    error_message = f"{_translate('log_message', 'ERROR: An exception occurred')}\n"
    error_message += ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    message_with_timestamp(ui, error_message)
    # Вызываем стандартный обработчик исключений для вывода на экран
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

def exception_handler_only_log(exc_type, exc_value, exc_traceback):
    _translate = configtools.read_config_translate()
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S.%f")[:-3] + "]"
    error_message = f"{_translate('log_message', 'ERROR: An exception occurred')}\n"
    error_message += ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    write_to_log_file(
        f"{timestamp} {error_message}")
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

def update_text_browser(ui, message):
    try:
        ui.textBrowser.append(message)
        ui.textBrowser.selectAll()  # выделяем весь текст для корректного обновления шрифтов
        ui.textBrowser.verticalScrollBar().setValue(ui.textBrowser.verticalScrollBar().maximum())
        cursor = ui.textBrowser.textCursor()
        cursor.movePosition(cursor.End)
        ui.textBrowser.setTextCursor(cursor)
        ui.textBrowser.ensureCursorVisible()
    except Exception as e:
        exception_handler_only_log(type(e), e, e.__traceback__)
