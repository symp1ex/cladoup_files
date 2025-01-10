from PyQt5 import QtWidgets
import os
import configtools
import logger

def open_config_select_dialog(ui):
    _translate = configtools.read_config_translate()
    try:
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly  # Опция "Только чтение"

        json_filter = _translate("MainWindow", "JSON Files (*.json)")  # Фильтр для JSON файлов

        config_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            _translate("MainWindow", "Select Config File"),
            "",
            json_filter,  # Используем только фильтр JSON файлов
            options=options
        )
        if config_path:
            ui.lineEdit_3.setText(config_path)
            path = ui.lineEdit_3.text()
            config = configtools.read_config_from_json(path)
            logger.message_with_timestamp_nn(ui, _translate("log_message", "Selected 'config.json' ") + _translate(
                "log_message", "with the following options:"))
            for key, value in config.items():
                logger.message(ui, f"    {key}: {value}")
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def save_cur_config(ui):
    try:
        silence_mode = ui.checkBox.isChecked()
        language = ui.lineEdit_4.text()
        source_path = ui.lineEdit.text()
        destination_path = ui.lineEdit_2.text()
        interval = ui.spinBox_2.value()
        max_copies = ui.spinBox.value()

        config_data = {
            "silence_mode": silence_mode,
            "language": language,
            "source_path": source_path,
            "destination_path": destination_path,
            "interval": interval,
            "max_copies": max_copies
        }
        open_dialog_save_config(ui, config_data)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def open_dialog_save_config(ui, config):
    _translate = configtools.read_config_translate()

    try:
        json_filter = _translate("MainWindow", "JSON Files (*.json)")  # Фильтр для JSON файлов
        options = QtWidgets.QFileDialog.Options()
        file_path = QtWidgets.QFileDialog.getSaveFileName(None, _translate("path_dialog", "Save as"), "",
                                                          json_filter, options=options)
        file_path_str = file_path[0]
        if file_path_str:
            # Если расширение не .json, добавляем его
            if not file_path_str.endswith('.json'):
                file_path_str += '.json'
            configtools.create_config_file(config, file_path_str)

            logger.message_with_timestamp_nn(ui, _translate("log_message", "Created a new 'config.json' ") + _translate(
                "log_message", "with the following options:"))
            for key, value in config.items():
                logger.message(ui, f"    {key}: {value}")
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def create_default_config(ui):
    configtools.create_new_config(ui)

def open_output_folder_ui(ui):
    try:
        path = os.path.expandvars(ui.lineEdit_2.text())
        os.startfile(path)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def open_output_folder_config(ui):
    try:
        config = configtools.read_config_select_mode(ui)
        path = os.path.expandvars(config.get("destination_path"))
        os.startfile(path)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)
