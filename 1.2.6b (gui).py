#1.2.6b
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

def read_config_translate():
    translation_provider = TranslationProvider()
    json_file = os.path.join(os.getcwd(), "config.json")
    config = read_config_from_json(json_file)
    if config:
        lang = config.get("language")
        if lang == "ru":
            _translate = translation_provider.translate
        else:
            _translate = translation_provider.original_text
    else:
        _translate = translation_provider.original_text
    return _translate

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
                "Create New \'Config.json\'": "Создать новый \'Config.json\'",
                "About": "О программе"
            },
            "path_dialog": {
                "Select Source File": "Выберите файл для копирования",
                "All Files (*)": "Все файлы (*)",
                "Select Source Path":  "Выберите папку для копирования",
                "Select Destination Path": "Выберите путь для сохранения:"
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
                "New 'config.json' created": "Создан новый 'config.json'",
                "Error: config file not found": "Ошибка: файл конфигурации не найден",
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 501, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 101, 501, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 591, 72, 31))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(os._exit)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 591, 82, 31))
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
        self.actionCreate_New_Config_json = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Config_json.setObjectName("actionCreate_New_Config_json")
        self.actionCreate_New_Config_json.triggered.connect(lambda: self.create_new_config("en"))
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionRussian = QtWidgets.QAction(MainWindow)
        self.actionRussian.setObjectName("actionRussian")
        # Связывание действий с функцией изменения языка
        self.actionEnglish.triggered.connect(lambda: self.change_language("en"))
        self.actionRussian.triggered.connect(lambda: self.change_language("ru"))
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionRussian)
        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionCreate_New_Config_json)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def hide_main_window(self):
        self.MainWindow.hide()

    def create_config_file(self, config, file_path="config.json"):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(config, file, ensure_ascii=False, indent=4)

    def create_new_config(self, lang):
        _translate = read_config_translate()
        config_data = {
            "silence_mode": False,
            "language": lang,
            "source_path": "C:\\",
            "destination_path": "D:\\",
            "interval": 600,
            "max_copies": 5
        }
        self.create_config_file(config_data)
        self.message_with_timestamp(_translate("log_message", "New 'config.json' created"))

    def change_language(self, lang):
        # Обновление значения языка в config.json
        json_file = os.path.join(os.getcwd(), "config.json")
        config = read_config_from_json(json_file)
        if config:
            config["language"] = lang
            self.create_config_file(config)
        else:
            self.create_new_config(lang)
        # Обновление текущего перевода
        self.retranslateUi(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = read_config_translate()
        MainWindow.setWindowTitle("cladoup files")
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
        self.actionCreate_New_Config_json.setText(_translate("MainWindow", "Create New \'Config.json\'"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionEnglish.setText("English")
        self.actionRussian.setText("Русский")

    def exception_handler(self, exc_type, exc_value, exc_traceback):
        _translate = read_config_translate()
        self.message_with_timestamp(
            f"{_translate('log_message', 'ERROR: An exception occurred')} - {exc_value}")
        # Вызываем стандартный обработчик исключений для вывода на экран
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    def exception_handler_only_log(self, exc_type, exc_value, exc_traceback):
        _translate = read_config_translate()
        timestamp = datetime.datetime.now().strftime("[%d-%m-%y %H-%M-%S]")
        self.write_to_log_file(
            f"{timestamp} {_translate('log_message', 'ERROR: An exception occurred')} - {exc_value}")
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    def update_text_browser(self, message):
        self.textBrowser.append(message)
        self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())

    def write_to_log_file(self, message):
        log_file_path = get_log_file_path()
        with open(log_file_path, "a") as log_file:
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

    def on_toolButton_clicked(self):
        if self.radioButton.isChecked():
            self.open_source_path_dialog_folder()
        else:
            self.open_source_path_dialog_file()

    def auto_button_click(self):
        self.stop_copying()
        if self.checkBox.isChecked():
            self.copy_is_silence()
            self.hide_main_window()
        else:
            self.copy_is_auto()

    def open_source_path_dialog_file(self):
        _translate = read_config_translate()
        options = QtWidgets.QFileDialog.Options()
        source_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, _translate("path_dialog", "Select Source File"), "", _translate("path_dialog", "All Files (*)"),
                                                               options=options)
        if source_path:
            source_path = source_path.replace("/", "\\")
            self.lineEdit.setText(source_path)

    def open_source_path_dialog_folder(self):
        _translate = read_config_translate()
        options = QtWidgets.QFileDialog.Options()
        source_path = QtWidgets.QFileDialog.getExistingDirectory(None, _translate("path_dialog", "Select Source Path"), "", options=options)
        if source_path:
            source_path = source_path.replace("/", "\\")
            self.lineEdit.setText(source_path)

    def open_destination_path_dialog(self):
        _translate = read_config_translate()
        options = QtWidgets.QFileDialog.Options()
        destination_path = QtWidgets.QFileDialog.getExistingDirectory(None, _translate("path_dialog", "Select Destination Path"), "",
                                                                      options=options)
        if destination_path:
            destination_path = destination_path.replace("/", "\\")
            self.lineEdit_2.setText(destination_path)

    def get_source_path_from_field(self):
        source_path = self.lineEdit.text()
        return source_path

    def get_destination_path_from_field(self):
        destination_path = self.lineEdit_2.text()
        return destination_path

    def start_button_click(self):
        self.stop_copying()
        self.copy_thread_stop_event = threading.Event()
        _translate = read_config_translate()

        source_path = self.validate_path_source_for_ui(self.get_source_path_from_field())
        if source_path:
            destination_path = self.validate_path_destination_for_ui(self.get_destination_path_from_field(), source_path)
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

    copy_thread_stop_event = threading.Event()

    def stop_copying(self):
        self.copy_thread_stop_event.set()

    def copy_files(self, source_path, destination_path, interval, max_copies, stop_event):
        copies_info = {}  # Словарь для хранения информации о сделанных копиях
        copy_count = 1
        delete_copy_count = 1
        _translate = read_config_translate()

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
        _translate = read_config_translate()

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
            self.exception_handler_only_log(type(e), e, e.__traceback__)

    def validate_path_source_for_ui(self, path):
        _translate = read_config_translate()
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
        _translate = read_config_translate()
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
        _translate = read_config_translate()
        if value == True:
            self.message_with_timestamp(
                f"{_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be an integer.')}")
        else:
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
            config = read_config_from_json(json_file)
            _translate = read_config_translate()

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
                    f"{_translate('log_message', 'Error: config file not found')}")
        except Exception as e:
            self.exception_handler(type(e), e, e.__traceback__)

    def validate_path_source_for_silence(self, path):
        _translate = read_config_translate()
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
            os._exit(1)

    def validate_path_destination_for_silence(self, path, source_path):
        _translate = read_config_translate()
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
            os._exit(1)

    def validate_positive_integer_for_silence(self, value, param_name):
        _translate = read_config_translate()
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
        if value == True:
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'Error:')} '{param_name}' {_translate('log_message', 'must be an integer.')}")
            self.write_to_log_file(
                f"[{timestamp}] {_translate('log_message', 'The program has been stopped.')}")
            os._exit(1)
        else:
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
                os._exit(1)

    def copy_is_silence(self):
        try:
            self.copy_thread_stop_event = threading.Event()
            config = read_config_from_json(json_file)
            _translate = read_config_translate()
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
            os._exit(1)


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        _translate = read_config_translate()
        self.ui = Ui_MainWindow()

        if config:
            silence_mode = config.get("silence_mode")
            if silence_mode == True:
                self.ui.copy_is_silence()
            elif silence_mode == False:
                self.ui.setupUi(self)
                self.show()
            else:
                self.ui.setupUi(self)
                self.show()
                self.ui.message_with_timestamp(
                    f"{_translate('log_message', 'Error: The configuration file contains an invalid data format. You can continue manually.')}")
        else:
            self.ui.setupUi(self)
            self.show()
            self.ui.message_with_timestamp(
                f"Error: config file not found. You can continue manually.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    json_file = os.path.join(os.getcwd(), "config.json")
    config = read_config_from_json(json_file)
    main_window = AppMainWindow()
    sys.exit(app.exec_())