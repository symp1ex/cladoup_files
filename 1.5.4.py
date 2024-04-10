#1.5.4
import os
import shutil
import time
import threading
import json
import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def read_config_from_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
def get_log_file_path():
    current_dir = os.getcwd()
    return os.path.join(current_dir, "log.txt")

class TranslationProvider:
    def __init__(self):
        self.translations = {
            "MainWindow": {
                "Auto": "Авто",
                "Start": "Старт",
                "Exit": "Выход",
                "Stop": "Стоп",
                "Interval (sec):": "Интервал (сек):",
                "Num of copies:": "Кол-во копий:",
                "Select the object to copy:": "Выберите объект копирования:",
                "Select a save path:": "Выберите путь для сохранения:",
                "Silence mode": "Фоновый режим",
                "Select folder as object": "Выбрать папку как объект",
                "Settings": "Настройки",
                "Language": "Язык",
                "Open save folder": "Открыть папку сохранения",
                "for manual mode": "для ручного режима",
                "for auto mode": "для авто-режима",
                "Select another config": "Выбрать другой конфиг",
                "Select Config File": "Выберите конфиг файл",
                "JSON Files (*.json)": "JSON-файл (*.json)",
                "Create new \'config.json\'": "Создать новый \'config.json\'",
                "Save current config": "Сохранить текущий конфиг",
                "About": "О программе"
            },
            "path_dialog": {
                "Select Source File": "Выберите файл для копирования",
                "All Files (*)": "Все файлы (*)",
                "Select Source Path":  "Выберите папку для копирования",
                "Select Destination Path": "Выберите путь для сохранения:",
                "Save as": "Сохранить как"
            },
            "log_message": {
                "Removed copy": "Удалены копия",
                "with folder:": "и папка:",

                "Copy created": "Сделана копия",
                "to a folder:": "в папку:",

                "The program has been stopped.": "Работа программы остановлена.",
                "Error: interval must be a positive number.": "Ошибка: интервал должен быть положительным числом.",
                "Error: Please enter an integer for the interval.": "Ошибка: введите целое число для интервала.",
                "Error: number of copies must be a positive number.": "Ошибка: количество копий должно быть положительным числом.",
                "Error: Enter an integer for the number of copies.": "Ошибка: введите целое число для количества копий.",

                "is not a valid path. Please provide the path to the folder or file.": "не является допустимым путем. Пожалуйста, укажите путь к папке или файлу.",
                "You can continue to work in manual mode.": "Вы можете продолжить работу в ручном режиме.",
                "Error: The specified path does not exist:": "Ошибка: указанный путь не существует:",

                "Error: value": "Ошибка: значение",
                "is not a valid path.": "не является допустимым путем.",

                "You can continue to work manually or fix the configuration file.": "Вы можете продолжить работу в ручном режиме или исправить файл конфигурации.",
                "must be an integer.": "должно быть целым числом.",
                "Error:": "Ошибка:",
                "must be a positive number.": "должно быть положительным числом.",
                "must be a positive integer.": "должно быть положительным целым числом.",
                "Found configuration file. Copying will be performed according to the following parameters:": "Найден файл конфигурации. Копирование будет выполнено по следующим параметрам:",
                "Error: Correct the configuration file.": "Ошибка: Исправьте файл конфигурации.",
                "Error: Not enough data in configuration file. Correct the configuration file or enter the parameters manually.": "Ошибка: недостаточно данных в файле конфигурации. Исправьте файл конфигурации или введите параметры вручную.",
                "Error: The configuration file contains an invalid data format. Correct the configuration file or enter the parameters manually.": "Ошибка: файл конфигурации содержит неверный формат данных. Исправьте файл конфигурации или введите параметры вручную.",
                "The following parameters for copying have been entered manually: ": "Следующие параметры для копирования были введены вручную: ",
                "    Source path:": "    Исходный путь:",
                "    Path to save copy:": "    Путь для сохранения копии:",
                "    Copy Interval:": "    Интервал копирования:",
                "sec.": "сек.",
                "    Number of copies to keep:": "    Количество хранимых копий:",
                "Error: invalid input. Repeat request.": "Ошибка: неправильный ввод. Повторите запрос.",
                "Error: The configuration file contains an invalid data format. You can continue manually.": "Ошибка: файл конфигурации содержит неверный формат данных. Вы можете продолжить в ручном режиме.",
                "Created a new 'config.json' ": "Создан новый 'config.json' ",
                "Selected 'config.json' ": "Выбран 'config.json' ",
                "with the following options:": "со следующими параметрами:",
                "Error: config file not found or contains an invalid data format": "Ошибка: файл конфигурации не найден или содержит неверный формат данных.",
                "ERROR: An exception occurred": "ОШИБКА: Произошло исключение",
                "Error: The path to the source cannot be the same as the path to save": "Ошибка: Путь до источника не может совпадать с путём для сохранения",
                "Error: Source folder cannot be empty:": "Ошибка: Исходная папка не может быть пустой:",
                "Select the correct settings for copying.": "Укажите корректные параметры для копирования."
            }
        }

    def translate(self, context, text):
        if context in self.translations and text in self.translations[context]:
            return self.translations[context][text]
        else:
            return text

    def original_text(self, context, text):
        if context in self.translations and text in self.translations[context]:
            return text
        else:
            return text

class Ui_MainWindow(object):
    def closeEvent(self, event):
        QtWidgets.QApplication.quit()
        event.accept()

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(522, 680)
        MainWindow.setMinimumSize(QtCore.QSize(521, 665))
        MainWindow.setMaximumSize(QtCore.QSize(521, 665))
        icon = QtGui.QIcon("icon.ico")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 501, 21))
        self.lineEdit.setText("C:\\")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 101, 501, 21))
        self.lineEdit_2.setText("C:\\")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 591, 82, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.auto_button_click)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 131, 82, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.start_button_click)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 181, 501, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(True)  # Отключаем возможность редактирования
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)  # Отключаем фокус
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 591, 72, 31))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(os._exit)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(9, 591, 82, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.stop_copying)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(350, 141, 61, 21))
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 139, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 139, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 141, 81, 21))
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 71, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(460, 101, 51, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.open_destination_path_dialog)  # Привязка кнопки к методу
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(460, 40, 51, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.on_toolButton_clicked)  # Привязка кнопки к методу
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(191, 598, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(354, 14, 157, 16))
        self.radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton.setObjectName("radioButton")
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.textBrowser.raise_()
        self.toolButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.spinBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.toolButton_2.raise_()
        self.spinBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.checkBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuLanguage = QtWidgets.QMenu(self.menuSettings)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menuBar)
        self.menu_open_folder = QtWidgets.QMenu(self.menuSettings)
        self.menu_open_folder.setObjectName("open_folder")
        MainWindow.setMenuBar(self.menuBar)
        self.actionCreate_New_Config_json = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Config_json.setObjectName("actionCreate_New_Config_json")
        self.actionCreate_New_Config_json.triggered.connect(lambda: self.create_new_config())
        self.actionSave_cur_Config_json = QtWidgets.QAction(MainWindow)
        self.actionSave_cur_Config_json.setObjectName("actionSave_cur_Config_json")
        self.actionSave_cur_Config_json.triggered.connect(lambda: self.save_cur_config())
        self.actionselect_Config_json = QtWidgets.QAction(MainWindow)
        self.actionselect_Config_json.setObjectName("action_select_Config_json")
        self.actionselect_Config_json.triggered.connect(self.open_config_select_dialog)
        self.action_open_ui_folder = QtWidgets.QAction(MainWindow)
        self.action_open_ui_folder.setObjectName("action_open_ui_folder")
        self.action_open_ui_folder.triggered.connect(self.open_output_folder_ui)
        self.action_open_config_folder = QtWidgets.QAction(MainWindow)
        self.action_open_config_folder.setObjectName("action_open_config_folder")
        self.action_open_config_folder.triggered.connect(self.open_output_folder_config)
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionRussian = QtWidgets.QAction(MainWindow)
        self.actionRussian.setCheckable(True)
        self.actionRussian.setObjectName("actionRussian")
        # Связывание действий с функцией изменения языка
        self.actionEnglish.triggered.connect(lambda: self.change_language("en"))
        self.actionRussian.triggered.connect(lambda: self.change_language("ru"))
        self.menu_open_folder.addAction(self.action_open_ui_folder)
        self.menu_open_folder.addAction(self.action_open_config_folder)
        self.menuSettings.addAction(self.actionCreate_New_Config_json)
        self.menuSettings.addAction(self.actionSave_cur_Config_json)
        self.menuSettings.addSeparator()   
        self.menuSettings.addAction(self.actionselect_Config_json)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menu_open_folder.menuAction())
        self.menuSettings.addSeparator()
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionRussian)
        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def hide_main_window(self):
        self.MainWindow.hide()

    def open_config_select_dialog(self):
        _translate = self.read_config_translate()
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
                self.lineEdit_3.setText(config_path)
                path = self.lineEdit_3.text()
                config = read_config_from_json(path)
                self.message_with_timestamp_nn(
                    _translate("log_message", "Selected 'config.json' ") + _translate("log_message", "with the following options:"))
                for key, value in config.items():
                    self.message(f"    {key}: {value}")

        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def read_config_select_mode(self):
        try:
            config_path = self.lineEdit_3.text()
            if config_path:
                config = read_config_from_json(config_path)
            else:
                config = read_config_from_json(json_file)
            return config
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def create_config_file(self, config, file_path="config.json"):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(config, file, ensure_ascii=False, indent=4)

    def create_new_config(self):
        _translate = self.read_config_translate()

        try:
            language = self.lineEdit_4.text()
            
            config_data = {
                "silence_mode": False,
                "language": language,
                "source_path": "C://",
                "destination_path": "C://",
                "interval": 300,
                "max_copies": 10
            }
            self.create_config_file(config_data)
            self.message_with_timestamp_nn(_translate("log_message", "Created a new 'config.json' ") + _translate("log_message", "with the following options:"))
            for key, value in config_data.items():
                self.message(f"    {key}: {value}")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def save_cur_config_file(self, config):
        _translate = self.read_config_translate()
        try:
            json_filter = _translate("MainWindow", "JSON Files (*.json)")  # Фильтр для JSON файлов
            options = QtWidgets.QFileDialog.Options()
            file_path = QtWidgets.QFileDialog.getSaveFileName(None, _translate("path_dialog", "Save as"), "", json_filter, options=options)
            file_path_str = file_path[0]
            if file_path_str:
                # Если расширение не .json, добавляем его
                if not file_path_str.endswith('.json'):
                    file_path_str += '.json'
                with open(file_path_str, "w", encoding="utf-8") as file:
                    json.dump(config, file, ensure_ascii=False, indent=4)

                self.message_with_timestamp_nn(
                    _translate("log_message", "Created a new 'config.json' ") + _translate("log_message", "with the following options:"))
                for key, value in config.items():
                    self.message(f"    {key}: {value}")

        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def save_cur_config(self):
        _translate = self.read_config_translate()

        try:
            language = self.lineEdit_4.text()
            source_path = self.lineEdit.text()
            destination_path = self.lineEdit_2.text()
            interval = self.spinBox_2.value()
            max_copies = self.spinBox.value()

            config_data = {
                "silence_mode": False,
                "language": language,
                "source_path": source_path,
                "destination_path": destination_path,
                "interval": interval,
                "max_copies": max_copies
            }
            self.save_cur_config_file(config_data)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def change_language(self, lang):
        try:
            # Обновление значения языка в config.json
            json_file = os.path.join(os.getcwd(), "config.json")
            config = read_config_from_json(json_file)
            if config:
                config["language"] = lang
                self.create_config_file(config)
            else:
                lang_cfg = lang
                self.lineEdit_4.setText(lang_cfg)
                self.create_new_config()

            if lang == "ru":
                self.actionEnglish.setChecked(False)
                self.actionRussian.setChecked(True)
            else:
                self.actionEnglish.setChecked(True)
                self.actionRussian.setChecked(False)
            # Обновление текущего перевода
            self.retranslateUi(self.MainWindow)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def read_config_translate(self):
        try:
            translation_provider = TranslationProvider()
            json_file = os.path.join(os.getcwd(), "config.json")
            config = read_config_from_json(json_file)
            if config:
                lang = config.get("language")
                if lang == "ru":
                    _translate = translation_provider.translate
                    lang_cfg = "ru"
                    self.lineEdit_4.setText(lang_cfg)
                else:
                    _translate = translation_provider.original_text
                    lang_cfg = "en"
                    self.lineEdit_4.setText(lang_cfg)
            else:
                _translate = translation_provider.original_text
            return _translate
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def retranslateUi(self, MainWindow):
        _translate = self.read_config_translate()
        MainWindow.setWindowTitle("cladoup files v1.5.4")
        self.pushButton_2.setText(_translate("MainWindow", "Auto"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Exit"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Interval (sec):"))
        self.label_2.setText(_translate("MainWindow", "Num of copies:"))
        self.label_3.setText(_translate("MainWindow", "Select the object to copy:"))
        self.label_4.setText(_translate("MainWindow", "Select a save path:"))
        self.toolButton_2.setText("...")
        self.toolButton.setText("...")
        self.checkBox.setText(_translate("MainWindow", "Silence mode"))
        self.radioButton.setText(_translate("MainWindow", "Select folder as object"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.action_open_ui_folder.setText(_translate("MainWindow", "for manual mode"))
        self.action_open_config_folder.setText(_translate("MainWindow", "for auto mode"))
        self.menu_open_folder.setTitle(_translate("MainWindow", "Open save folder"))
        self.actionselect_Config_json.setText(_translate("MainWindow", "Select another config"))
        self.actionCreate_New_Config_json.setText(_translate("MainWindow", "Create new \'config.json\'"))
        self.actionSave_cur_Config_json.setText(_translate("MainWindow", "Save current config"))
        self.actionEnglish.setText("English")
        self.actionRussian.setText("Русский")

    def exception_handler(self, exc_type, exc_value, exc_traceback):
        _translate = self.read_config_translate()
        self.message_with_timestamp(
            f"{_translate('log_message', 'ERROR: An exception occurred')} - {exc_value}")
        # Вызываем стандартный обработчик исключений для вывода на экран
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    def exception_handler_only_log(self, exc_type, exc_value, exc_traceback):
        _translate = self.read_config_translate()
        timestamp = datetime.datetime.now().strftime("[%d-%m-%y %H-%M-%S]")
        self.write_to_log_file(
            f"{timestamp} {_translate('log_message', 'ERROR: An exception occurred')} - {exc_value}")
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    def update_text_browser(self, message):
        try:
            self.textBrowser.append(message)
            self.textBrowser.selectAll() #выделяем весь текст для корректного обновления шрифтов
            self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
            cursor = self.textBrowser.textCursor()
            cursor.movePosition(cursor.End)
            self.textBrowser.setTextCursor(cursor)
            self.textBrowser.ensureCursorVisible()
        except Exception as e:
            self.exception_handler_only_log(type(e), e, e.__traceback__)

    def write_to_log_file(self, message):
        log_file_path = get_log_file_path()
        with open(log_file_path, "a", encoding="cp1251") as log_file:
            log_file.write(message + "\n")

    def message(self, message):
        self.update_text_browser(f"{message}")
        self.write_to_log_file(f"{message}")

    def message_with_timestamp(self, message):
        timestamp = datetime.datetime.now().strftime("[%d-%m-%y %H-%M-%S]")
        self.update_text_browser(f"{timestamp} {message}")
        self.write_to_log_file(f"{timestamp} {message}")

    # добавляем в лог запись, но с переносом строки пере меткой времени
    def message_with_timestamp_nn(self, message):
        timestamp = datetime.datetime.now().strftime("[%d-%m-%y %H-%M-%S]")
        self.update_text_browser(f"\n{timestamp} {message}")
        self.write_to_log_file(f"\n{timestamp} {message}")

    def open_output_folder_ui(self):
        try:
            path = os.path.expandvars(self.lineEdit_2.text())
            os.startfile(path)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def open_output_folder_config(self):
        try:
            config = self.read_config_select_mode()
            path = os.path.expandvars(config.get("destination_path"))
            os.startfile(path)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def on_toolButton_clicked(self):
        try:
            if self.radioButton.isChecked():
                self.open_source_path_dialog_folder()
            else:
                self.open_source_path_dialog_file()
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def auto_button_click(self):
        try:
            self.stop_copying()
            time.sleep(1)
            if self.checkBox.isChecked():
                self.copy_is_silence()
                self.hide_main_window()
            else:
                self.copy_is_auto()
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def open_source_path_dialog_file(self):
        _translate = self.read_config_translate()
        try:
            options = QtWidgets.QFileDialog.Options()
            source_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, _translate("path_dialog", "Select Source File"), "", _translate("path_dialog", "All Files (*)"),
                                                                   options=options)
            if source_path:
                source_path = source_path.replace("/", "\\")
                self.lineEdit.setText(source_path)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def open_source_path_dialog_folder(self):
        _translate = self.read_config_translate()
        try:
            options = QtWidgets.QFileDialog.Options()
            source_path = QtWidgets.QFileDialog.getExistingDirectory(None, _translate("path_dialog", "Select Source Path"), "", options=options)
            if source_path:
                source_path = source_path.replace("/", "\\")
                self.lineEdit.setText(source_path)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def open_destination_path_dialog(self):
        _translate = self.read_config_translate()
        try:
            options = QtWidgets.QFileDialog.Options()
            destination_path = QtWidgets.QFileDialog.getExistingDirectory(None, _translate("path_dialog", "Select Destination Path"), "",
                                                                          options=options)
            if destination_path:
                destination_path = destination_path.replace("/", "\\")
                self.lineEdit_2.setText(destination_path)
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def start_button_click(self):
        self.stop_copying()
        time.sleep(1)
        self.copy_thread_stop_event = threading.Event()
        _translate = self.read_config_translate()

        try:
            source_path = self.validate_path_source_for_ui(self.lineEdit.text())
            if source_path:
                destination_path = self.validate_path_destination_for_ui(self.lineEdit_2.text(), source_path)
            interval = self.validate_positive_integer_for_ui(self.spinBox_2.value(), "interval")
            max_copies = self.validate_positive_integer_for_ui(self.spinBox.value(), "max_copies")

            if source_path and destination_path and interval and max_copies:
                self.message_with_timestamp_nn(
                    f"{_translate('log_message', 'The following parameters for copying have been entered manually: ')}")
                self.message(f"{_translate('log_message', '    Source path:')} '{source_path}'")
                self.message(f"{_translate('log_message', '    Path to save copy:')} '{destination_path}'")
                self.message(f"{_translate('log_message', '    Copy Interval:')} {interval} {_translate('log_message', 'sec.')}")
                self.message(f"{_translate('log_message', '    Number of copies to keep:')} {max_copies}")

                if self.checkBox.isChecked():
                    copy_thread = threading.Thread(target=self.copy_files_silence,
                                                   args=(source_path, destination_path, interval, max_copies))
                    copy_thread.start()
                    self.hide_main_window()
                else:
                    copy_thread = threading.Thread(target=self.copy_files,
                                                   args=(source_path, destination_path, interval, max_copies, self.copy_thread_stop_event))
                    copy_thread.start()
            else:
                self.message_with_timestamp(f"{_translate('log_message', 'Select the correct settings for copying.')}")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    copy_thread_stop_event = threading.Event()

    def stop_copying(self):
        self.copy_thread_stop_event.set()

    def copy_files(self, source_path, destination_path, interval, max_copies, stop_event):
        copies_info = {}  # Словарь для хранения информации о сделанных копиях
        copy_count = 1
        delete_copy_count = 1
        _translate = self.read_config_translate()

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
                    self.message_with_timestamp(
                        f"{_translate('log_message', 'Removed copy')} {delete_copy_count} {_translate('log_message', 'with folder:')} '{oldest_copy_path}'")
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

                self.message_with_timestamp(
                    f"{_translate('log_message', 'Copy created')} {copy_count} {_translate('log_message', 'to a folder:')} '{copy_folder_path}'")
                copy_count += 1
                if not stop_event.wait(interval):
                    continue
                else:
                    # запись в вывод и в лог об остановке
                    self.message_with_timestamp(
                        f"{_translate('log_message', 'The program has been stopped.')}")
                    break
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def copy_files_silence(self, source_path, destination_path, interval, max_copies):
        copies_info = {}  # Словарь для хранения информации о сделанных копиях
        copy_count = 1
        delete_copy_count = 1
        _translate = self.read_config_translate()

        try:
            while True:
                copy_folder_name = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
                copy_folder_path = os.path.join(destination_path, copy_folder_name)
                os.makedirs(copy_folder_path)
                copies_info[copy_folder_path] = time.time()

                if len(copies_info) > max_copies:
                    oldest_copy_path = min(copies_info, key=copies_info.get)
                    del copies_info[oldest_copy_path]
                    shutil.rmtree(oldest_copy_path, ignore_errors=True)
                    self.write_to_log_file(
                        f"[{copy_folder_name}] {_translate('log_message', 'Removed copy')} {delete_copy_count} {_translate('log_message', 'with folder:')} '{oldest_copy_path}'")
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

                self.write_to_log_file(
                    f"[{copy_folder_name}] {_translate('log_message', 'Copy created')} {copy_count} {_translate('log_message', 'to a folder:')} '{copy_folder_path}'")
                copy_count += 1
                time.sleep(interval)
                continue
        except Exception as e:
            timestamp = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
            self.exception_handler_only_log(type(e), e, e.__traceback__)
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)


    def validate_path_source_for_ui(self, path):
        _translate = self.read_config_translate()
        try:
            if not isinstance(path, str):
                self.message_with_timestamp(
                    f"{_translate('log_message', 'Error: The specified path does not exist:')} '{path}'")

            path = os.path.expandvars(path)

            if os.path.exists(path):
                if os.path.isdir(path):  # Проверяем, является ли путь папкой
                    contents = os.listdir(path)
                    if not contents:
                        self.message_with_timestamp(
                            f"{_translate('log_message', 'Error: Source folder cannot be empty:')} '{path}'")
                    else:
                        return os.path.abspath(path)
                else:
                    return os.path.abspath(path)
            else:
                self.message_with_timestamp(
                    f"{_translate('log_message', 'Error: The specified path does not exist:')} '{path}'")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def validate_path_destination_for_ui(self, path, source_path):
        _translate = self.read_config_translate()
        try:
            if not isinstance(path, str):
                self.message_with_timestamp(
                    f"{_translate('log_message', 'Error: value')} '{path}' {_translate('log_message', 'is not a valid path.')}")

            path = os.path.expandvars(path)

            if path == source_path:
                self.message_with_timestamp(_translate('log_message', "Error: The path to the source cannot be the same as the path to save"))
            elif path.startswith(source_path + os.path.sep):
                self.message_with_timestamp(_translate('log_message', "Error: The path to the source cannot be the same as the path to save"))
            else:
                try:
                    os.makedirs(path, exist_ok=True)
                    return os.path.abspath(path)
                except OSError:
                    self.message_with_timestamp(
                        f"{_translate('log_message', 'Error: value')} '{path}' {_translate('log_message', 'is not a valid path.')}")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def validate_positive_integer_for_ui(self, value, param_name):
        _translate = self.read_config_translate()
        try:
            value = int(value)
            if value > 0:
                return value
            else:
                self.message_with_timestamp(
                    f"{_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be a positive number.')}")
        except ValueError:
            self.message_with_timestamp(
                f"{_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be an integer.')}")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def copy_is_auto(self):
        try:
            self.copy_thread_stop_event = threading.Event()
            config = self.read_config_select_mode()
            _translate = self.read_config_translate()

            if config:
                silence_mode = config.get("silence_mode")
                if silence_mode == True:
                    self.copy_is_silence()
                    self.hide_main_window()
                elif silence_mode == False:
                    self.message_with_timestamp_nn(
                        f"{_translate('log_message', 'Found configuration file. Copying will be performed according to the following parameters:')}")

                    for key, value in config.items():
                        self.message(f"    {key}: {value}")

                    source_path = self.validate_path_source_for_ui(config.get("source_path"))
                    if source_path:
                        destination_path = self.validate_path_destination_for_ui(config.get("destination_path"), source_path)
                    interval = self.validate_positive_integer_for_ui(config.get("interval"), "interval")
                    max_copies = self.validate_positive_integer_for_ui(config.get("max_copies"), "max_copies")

                    if source_path and destination_path and interval and max_copies:
                        copy_thread = threading.Thread(target=self.copy_files,
                                                       args=(source_path, destination_path, interval, max_copies, self.copy_thread_stop_event))
                        copy_thread.start()
                    else:
                        self.message_with_timestamp(
                            f"{_translate('log_message', 'You can continue to work manually or fix the configuration file.')}")
                else:
                    self.message_with_timestamp_nn(
                        f"{_translate('log_message', 'Error: The configuration file contains an invalid data format. Correct the configuration file or enter the parameters manually.')}")
            else:
                self.message_with_timestamp(
                    f"{_translate('log_message', 'Error: config file not found or contains an invalid data format')}")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def validate_path_source_for_silence(self, path):
        _translate = self.read_config_translate()
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
        try:
            if not isinstance(path, str):
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'Error: The specified path does not exist:')} '{path}'")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)

            path = os.path.expandvars(path)

            if os.path.exists(path):
                if os.path.isdir(path):  # Проверяем, является ли путь папкой
                    contents = os.listdir(path)
                    if not contents:
                        self.write_to_log_file(
                            f"[{timestamp}] {_translate('log_message', 'Error: Source folder cannot be empty:')} '{path}'")
                        self.write_to_log_file(
                            f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                        os._exit(1)
                    else:
                        return os.path.abspath(path)
                else:
                    return os.path.abspath(path)
            else:
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'Error: The specified path does not exist:')} '{path}'")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)
        except Exception as e:
            self.exception_handler_only_log(type(e), e, e.__traceback__)
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)

    def validate_path_destination_for_silence(self, path, source_path):
        _translate = self.read_config_translate()
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
        try:
            if not isinstance(path, str):
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'Error: value')} '{path}' {_translate('log_message', 'is not a valid path.')}")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)

            path = os.path.expandvars(path)

            if path == source_path:
                self.write_to_log_file(f"[{timestamp}] {_translate('log_message', 'Error: The path to the source cannot be the same as the path to save')}")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)
            elif path.startswith(source_path + os.path.sep):
                self.write_to_log_file(f"[{timestamp}] {_translate('log_message', 'Error: The path to the source cannot be the same as the path to save')}")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)
            else:
                try:
                    os.makedirs(path, exist_ok=True)
                    return os.path.abspath(path)
                except OSError:
                    self.write_to_log_file(
                        f"[{timestamp}] {_translate('log_message', 'Error: value')} '{path}' {_translate('log_message', 'is not a valid path.')}")
                    self.write_to_log_file(
                        f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                    os._exit(1)
        except Exception as e:
            self.exception_handler_only_log(type(e), e, e.__traceback__)
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)

    def validate_positive_integer_for_silence(self, value, param_name):
        _translate = self.read_config_translate()
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
        try:
            value = int(value)
            if value > 0:
                return value
            else:
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be a positive number.')}")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)
        except ValueError:
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be an integer.')}")
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)
        except Exception as e:
            self.exception_handler_only_log(type(e), e, e.__traceback__)
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)

    def copy_is_silence(self):
        try:
            self.copy_thread_stop_event = threading.Event()
            config = self.read_config_select_mode()
            _translate = self.read_config_translate()
            timestamp = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")

            if config:
                self.write_to_log_file(
                    f"\n[{timestamp}] {_translate('log_message', 'Found configuration file. Copying will be performed according to the following parameters:')}")

                for key, value in config.items():
                    self.write_to_log_file(f"    {key}: {value}")

                source_path = self.validate_path_source_for_silence(config.get("source_path"))
                if source_path:
                    destination_path = self.validate_path_destination_for_silence(config.get("destination_path"), source_path)
                interval = self.validate_positive_integer_for_silence(config.get("interval"), "interval")
                max_copies = self.validate_positive_integer_for_silence(config.get("max_copies"), "max_copies")

                if source_path and destination_path and interval and max_copies:
                    copy_thread = threading.Thread(target=self.copy_files_silence,
                                                   args=(source_path, destination_path, interval, max_copies))
                    copy_thread.start()
                else:
                    self.write_to_log_file(
                        f"\n[{timestamp}] {_translate('log_message', 'Error: Correct the configuration file.')}")
                    self.write_to_log_file(
                        f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                    os._exit(1)
            else:
                self.write_to_log_file(
                    f"\n[{timestamp}] {_translate('log_message', 'Error: config file not found')}")
                self.write_to_log_file(
                    f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
                os._exit(1)
        except Exception as e:
            self.exception_handler_only_log(type(e), e, e.__traceback__)
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        _translate = self.ui.read_config_translate()

        if config:
            silence_mode = config.get("silence_mode")
            if silence_mode == True:
                self.ui.copy_is_silence()
            elif silence_mode == False:
                self.show()

                lang = config.get("language")
                if lang == "ru":
                    self.ui.actionEnglish.setChecked(False)
                    self.ui.actionRussian.setChecked(True)
                else:
                    self.ui.actionEnglish.setChecked(True)
                    self.ui.actionRussian.setChecked(False)
            else:
                self.show()
                self.ui.message_with_timestamp(
                    f"{_translate('log_message', 'Error: The configuration file contains an invalid data format. You can continue manually.')}")

                lang = config.get("language")
                if lang == "ru":
                    self.ui.actionEnglish.setChecked(False)
                    self.ui.actionRussian.setChecked(True)
                else:
                    self.ui.actionEnglish.setChecked(True)
                    self.ui.actionRussian.setChecked(False)
        else:
            self.ui.setupUi(self)
            self.show()
            self.ui.actionEnglish.setChecked(True)
            self.ui.actionRussian.setChecked(False)
            self.ui.message_with_timestamp(
                f"Error: config file not found. You can continue manually.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    json_file = os.path.join(os.getcwd(), "config.json")
    config = read_config_from_json(json_file)
    main_window = AppMainWindow()
    sys.exit(app.exec_())
