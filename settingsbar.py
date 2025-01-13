import os
import time

import winshell
from win32com.client import Dispatch
from pathlib import Path
import logger
import configtools
from PyQt5 import QtCore, QtGui, QtWidgets


class ui_settings_win(object):
    def __init__(self):
        self.config = configtools.read_config_from_json("config.json")
        self.settings_win = None

    def setupui_settings(self, settings_win, logs_days, ui):
        self.settings_win = settings_win
        settings_win.setObjectName("settings_win")
        settings_win.resize(337, 98)
        settings_win.setMinimumSize(QtCore.QSize(337, 98))
        settings_win.setMaximumSize(QtCore.QSize(337, 98))
        icon = QtGui.QIcon("icon.ico")
        settings_win.setWindowIcon(icon)
        settings_win.setWindowFlags(settings_win.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.save_button = QtWidgets.QPushButton(settings_win)
        self.save_button.setGeometry(QtCore.QRect(250, 60, 81, 31))
        self.save_button.setObjectName("pushButton")
        self.save_button.clicked.connect(lambda: self.set_logs_days(ui))
        self.cansel_button = QtWidgets.QPushButton(settings_win)
        self.cansel_button.setGeometry(QtCore.QRect(160, 60, 81, 31))
        self.cansel_button.setObjectName("pushButton_2")
        self.cansel_button.clicked.connect(self.hide_settings_win)
        self.label = QtWidgets.QLabel(settings_win)
        self.label.setGeometry(QtCore.QRect(10, 10, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(settings_win)
        self.lineEdit.setGeometry(QtCore.QRect(95, 10, 41, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(str(logs_days))
        self.label_2 = QtWidgets.QLabel(settings_win)
        self.label_2.setGeometry(QtCore.QRect(143, 10, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslate_settings(settings_win)
        QtCore.QMetaObject.connectSlotsByName(settings_win)

    def retranslate_settings(self, settings_win):
        _translate = configtools.read_config_translate()
        settings_win.setWindowTitle(_translate("settings_win", "Settings"))
        self.save_button.setText(_translate("settings_win", "Save"))
        self.cansel_button.setText(_translate("settings_win", "Cancel"))
        self.label.setText(_translate("settings_win", "Keep logs for"))
        self.label_2.setText(_translate("settings_win", "days."))

    def hide_settings_win(self):
        self.settings_win.hide()

    def set_logs_days(self, ui):
        from copy_method import validate_positive_integer

        _translate = configtools.read_config_translate()
        try:
            logs_days = self.lineEdit.text()
            validate_logs_days = validate_positive_integer(ui, logs_days, "logs_days")
            if validate_logs_days:
                if not self.config:
                    configtools.create_new_config(ui)
                    self.config = configtools.read_config_from_json("config.json")
                self.config["logs_days"] = int(logs_days)
                configtools.write_config_file(self.config)
                logger.message_with_timestamp(ui, f'{_translate("log_message", "The value of “logs_days” has been changed to:")} {logs_days}')
                self.settings_win.hide()
            else:
                show_error_message(_translate, "Error!", "This value must be an integer.")
        except Exception as e:
            logger.exception_handler(ui, type(e), e, e.__traceback__)

def show_error_message(_translate, title_message, text_message):
    # Создаем экземпляр QMessageBox
    msg_box = QtWidgets.QMessageBox()
    icon = QtGui.QIcon("icon.ico")
    msg_box.setWindowIcon(icon)

    # Устанавливаем тип сообщения как критическое (ошибка)
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle(_translate("settings_win", title_message))
    msg_box.setText(_translate("settings_win", text_message))

    # Отображаем окно сообщения
    msg_box.exec_()


def get_path_lnk(ui):
    try:
        exe_path = "cladoup_files.exe"
        exe_full_path = str(Path(exe_path).resolve())
        # Получаем путь к общедоступной папке автозагрузки
        startup_dir = winshell.startup(common=False)
        shortcut_path = Path(startup_dir) / (Path(exe_path).stem + ".lnk")
        return shortcut_path, exe_full_path
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def manage_startup_shortcut(ui):
    _translate = configtools.read_config_translate()

    try:
        shortcut_path, exe_full_path = get_path_lnk(ui)
        shell = Dispatch('WScript.Shell')

        if shortcut_path.exists():
            # Удаляем ярлык, если он существует
            os.remove(shortcut_path)
            logger.message_with_timestamp(ui, _translate("log_message", "Program removed from startup"))
        else:
            # Создаем ярлык, если его нет
            shortcut = shell.CreateShortCut(str(shortcut_path))
            shortcut.TargetPath = exe_full_path
            shortcut.WorkingDirectory = str(Path(exe_full_path).parent)
            shortcut.IconLocation = exe_full_path
            shortcut.save()
            logger.message_with_timestamp(ui, _translate("log_message", "The program has been added to the startup"))
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)

def set_checked_lang(ui, lang):
    if lang == "ru":
        ui.actionEnglish.setChecked(False)
        ui.actionRussian.setChecked(True)
    else:
        ui.actionEnglish.setChecked(True)
        ui.actionRussian.setChecked(False)

def change_language(ui, lang):
    try:
        # Обновление значения языка в config.json
        json_file = os.path.join(os.getcwd(), "config.json")
        config = configtools.read_config_from_json(json_file)

        ui.lineEdit_4.setText(lang)

        if config:
            config["language"] = lang
            configtools.write_config_file(config)
        else:
            configtools.create_new_config(ui)

        set_checked_lang(ui, lang)
        # Обновление текущего перевода
        ui.retranslateUi(ui.MainWindow)
    except Exception as e:
        logger.exception_handler(ui, type(e), e, e.__traceback__)