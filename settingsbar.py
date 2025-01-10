import os
import winshell
from win32com.client import Dispatch
from pathlib import Path
import logger
import configtools


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