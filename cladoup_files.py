import os
import time
import threading
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import configtools
import logger
import settingsbar
import filebar
import copy_method
import about


class Ui_MainWindow(object):
    def __init__(self):
        self.copy_thread_stop_event = threading.Event()
        self.delete_thread_stop_event = threading.Event()

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
        self.pushButton_5.clicked.connect(self.stop_copying_and_clean)

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
        self.toolButton.clicked.connect(self.open_source_path_dialog)  # Привязка кнопки к методу

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

        # Создание нового меню "file"
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        # Добавление созданного меню в меню-панель на позицию после меню "settings"
        self.menuBar.insertMenu(self.menuSettings.menuAction(), self.menuFile)

        self.actionCreate_New_Config_json = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Config_json.setObjectName("actionCreate_New_Config_json")
        self.actionCreate_New_Config_json.triggered.connect(lambda: filebar.create_default_config(self))

        self.actionSave_cur_Config_json = QtWidgets.QAction(MainWindow)
        self.actionSave_cur_Config_json.setObjectName("actionSave_cur_Config_json")
        self.actionSave_cur_Config_json.triggered.connect(lambda: filebar.save_cur_config(self))

        self.actionselect_Config_json = QtWidgets.QAction(MainWindow)
        self.actionselect_Config_json.setObjectName("action_select_Config_json")
        self.actionselect_Config_json.triggered.connect(lambda: filebar.open_config_select_dialog(self))

        self.action_open_ui_folder = QtWidgets.QAction(MainWindow)
        self.action_open_ui_folder.setObjectName("action_open_ui_folder")
        self.action_open_ui_folder.triggered.connect(lambda: filebar.open_output_folder_ui(self))

        self.action_open_config_folder = QtWidgets.QAction(MainWindow)
        self.action_open_config_folder.setObjectName("action_open_config_folder")
        self.action_open_config_folder.triggered.connect(lambda: filebar.open_output_folder_config(self))

        self.actionAutorun = QtWidgets.QAction(MainWindow)
        self.actionAutorun.setCheckable(True)
        self.actionAutorun.setObjectName("autorun")
        self.actionAutorun.triggered.connect(lambda: settingsbar.manage_startup_shortcut(self))

        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionRussian = QtWidgets.QAction(MainWindow)
        self.actionRussian.setCheckable(True)
        self.actionRussian.setObjectName("actionRussian")
        # Связывание действий с функцией изменения языка
        self.actionEnglish.triggered.connect(lambda: settingsbar.change_language(self, "en"))
        self.actionRussian.triggered.connect(lambda: settingsbar.change_language(self, "ru"))

        self.action_open_settings = QtWidgets.QAction(MainWindow)
        self.action_open_settings.setObjectName("open_settings")

        self.menu_open_folder.addAction(self.action_open_ui_folder)
        self.menu_open_folder.addAction(self.action_open_config_folder)
        self.menuFile.addAction(self.actionselect_Config_json)
        self.menuFile.addAction(self.actionSave_cur_Config_json)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Config_json)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_open_folder.menuAction())
        self.menuSettings.addAction(self.actionAutorun)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionRussian)
        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuSettings.addAction(self.action_open_settings)
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = configtools.read_config_translate()
        MainWindow.setWindowTitle(about.version)
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
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.action_open_ui_folder.setText(_translate("MainWindow", "for 'UI'"))
        self.action_open_config_folder.setText(_translate("MainWindow", "for config"))
        self.menu_open_folder.setTitle(_translate("MainWindow", "Open save folder"))
        self.actionselect_Config_json.setText(_translate("MainWindow", "Select another config"))
        self.actionCreate_New_Config_json.setText(_translate("MainWindow", "Create default config"))
        self.actionSave_cur_Config_json.setText(_translate("MainWindow", "Save current config"))
        self.actionAutorun.setText(_translate("MainWindow", "Autorun on Windows startup"))
        self.action_open_settings.setText(_translate("MainWindow", "Options")) # добавить перевол
        self.actionEnglish.setText("English")
        self.actionRussian.setText("Русский")

    def hide_main_window(self):
        self.MainWindow.hide()

    def open_source_path_dialog(self):
        _translate = configtools.read_config_translate()
        try:
            options = QtWidgets.QFileDialog.Options()
            if self.radioButton.isChecked():
                source_path = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                                         _translate("path_dialog", "Select Source Path"),
                                                                         "", options=options)
            else:
                source_path, _ = QtWidgets.QFileDialog.getOpenFileName(None,_translate("path_dialog", "Select Source File"), "" ,_translate("path_dialog", "All Files (*)"), options=options)
            if source_path:
                source_path = source_path.replace("/", "\\")
                self.lineEdit.setText(source_path)
        except Exception as e:
            logger.exception_handler(self, type(e), e, e.__traceback__)

    def open_destination_path_dialog(self):
        _translate = configtools.read_config_translate()
        try:
            options = QtWidgets.QFileDialog.Options()
            destination_path = QtWidgets.QFileDialog.getExistingDirectory(None, _translate("path_dialog",
                                                                                           "Select Destination Path"),
                                                                          "",
                                                                          options=options)
            if destination_path:
                destination_path = destination_path.replace("/", "\\")
                self.lineEdit_2.setText(destination_path)
        except Exception as e:
            logger.exception_handler(self, type(e), e, e.__traceback__)

    def start_button_click(self):
        source_path, destination_path, interval, max_copies = copy_method.get_copy_data_to_ui(self)
        copy_method.start_copy(self, source_path, destination_path, interval, max_copies)

    def auto_button_click(self):
        try:
            self.stop_copying_and_clean()
            time.sleep(1)
            if self.checkBox.isChecked():
                logger.not_interface_exists = True
                self.hide_main_window()
            source_path, destination_path, interval, max_copies = copy_method.get_copy_data_to_config(self)
            copy_method.start_copy(self, source_path, destination_path, interval, max_copies)
        except Exception as e:
            logger.exception_handler(self, type(e), e, e.__traceback__)

    def stop_copying(self):
        self.copy_thread_stop_event.set()

    def stop_clean(self):
        self.delete_thread_stop_event.set()

    def stop_copying_and_clean(self):
        self.stop_copying()
        self.stop_clean()

class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = configtools.read_config_translate()

        self.ui.action_open_settings.triggered.connect(self.open_settings)  # Привязываем кнопку к методу open_settings

        try:
            config = configtools.read_config_from_json("config.json")
            self.lang = config.get("language", "en")
        except AttributeError:
            self.lang = "en"
        self.ui.lineEdit_4.setText(self.lang)

    def open_settings(self):
        config = configtools.read_config_from_json("config.json")
        try:
            logs_days = config.get("logs_days", int(14))
        except AttributeError:
            logs_days = 14

        settings_window = QtWidgets.QDialog()  # Создаем новое окно для настроек
        settings_ui = settingsbar.ui_settings_win()  # Создаем экземпляр ui_settings_win

        # Вызов окна настроек
        settings_ui.setupui_settings(settings_window, logs_days, self.ui)  # Настраиваем интерфейс
        settings_window.setWindowModality(QtCore.Qt.ApplicationModal)
        settings_window.exec_()


    def main(self):
        config = configtools.read_config_from_json("config.json")
        try:
            shortcut_path, exe_full_path = settingsbar.get_path_lnk(self.ui)

            if shortcut_path.exists():
                self.ui.actionAutorun.setChecked(True)
            else:
                self.ui.actionAutorun.setChecked(False)

            if config:
                silence_mode = config.get("silence_mode")
                if silence_mode == True:
                    logger.not_interface_exists = True
                    source_path, destination_path, interval, max_copies = copy_method.get_copy_data_to_config(self.ui)
                    copy_method.start_copy(self.ui, source_path, destination_path, interval, max_copies)
                elif silence_mode == False:
                    self.show()
                    settingsbar.set_checked_lang(self.ui, self.lang)
                else:
                    self.show()
                    logger.message_with_timestamp(self.ui, f"{self._translate('log_message', 'Error: The configuration file contains an invalid data format. You can continue manually.')}")
                    settingsbar.set_checked_lang(self.ui, self.lang)
            else:
                self.show()
                settingsbar.set_checked_lang(self.ui, self.lang)
                logger.message_with_timestamp(self.ui, f"Error: config file not found. You can continue manually.")
                configtools.create_new_config(self.ui)
        except Exception as e:
            logger.exception_handler(self.ui, type(e), e, e.__traceback__)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AppMainWindow().main()
    sys.exit(app.exec_())
