class TranslationProvider:
    def __init__(self):
        self.translations_ru = {
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
                "File": "Файл",
                "Settings": "Настройки",
                "Language": "Язык",
                "Open save folder": "Открыть папку сохранения",
                "for 'UI'": "для интерфейса",
                "for config": "для конфига",
                "Select another config": "Выбрать другой конфиг",
                "Select Config File": "Выберите конфиг файл",
                "JSON Files (*.json)": "JSON-файл (*.json)",
                "Create default config": "Создать конфиг \"по умолчанию\"",
                "Save current config": "Сохранить текущий конфиг",
                "Autorun on Windows startup": "Автозапуск при загрузке Windows",
                "Options": "Дополнительно"
            },
            "path_dialog": {
                "Select Source File": "Выберите файл для копирования",
                "All Files (*)": "Все файлы (*)",
                "Select Source Path": "Выберите папку для копирования",
                "Select Destination Path": "Выберите путь для сохранения:",
                "Save as": "Сохранить как"
            },
            "settings_win": {
                "Settings": "Настройки",
                "Save": "Сохранить",
                "Cancel": "Отмена",
                "Keep logs for": "Хранить логи",
                "days.": "дней.",
                "Error!": "Ошибка!",
                "This value must be an integer.": "Это значение должно быть целым числом."
            },
            "log_message": {
                "Removed copy": "Удалены копия",
                "with folder:": "и папка:",
                "Copy created": "Сделана копия",
                "to a folder:": "в папку:",
                "The program has been stopped.": "Работа программы остановлена.",
                "Error: The specified path does not exist:": "Ошибка: указанный путь не существует:",
                "Error: value": "Ошибка: значение",
                "is not a valid path.": "не является допустимым путем.",
                "You can continue to work manually or fix the configuration file.":
                    "Вы можете продолжить работу в ручном режиме или исправить файл конфигурации.",
                "Error:": "Ошибка:",
                "must be a positive number.": "должно быть положительным числом.",
                "Found configuration file. Copying will be performed according to the following parameters:":
                    "Найден файл конфигурации. Копирование будет выполнено по следующим параметрам:",
                "Copying will be performed with the following parameters: ":
                    "Кoпирование будет произведено со следующими параметрами: ",
                "    Source path:": "    Исходный путь:",
                "    Path to save copy:": "    Путь для сохранения копии:",
                "    Copy Interval:": "    Интервал копирования:",
                "sec.": "сек.",
                "    Number of copies to keep:": "    Количество хранимых копий:",
                "Error: The configuration file contains an invalid data format. You can continue manually.":
                    "Ошибка: файл конфигурации содержит неверный формат данных. Вы можете продолжить в ручном режиме.",
                "Created a new 'config.json' ": "Создан новый 'config.json' ",
                "Selected 'config.json' ": "Выбран 'config.json' ",
                "with the following options:": "со следующими параметрами:",
                "ERROR: An exception occurred": "ОШИБКА: Произошло исключение",
                "Error: The path to the source cannot be the same as the path to save":
                    "Ошибка: Путь до источника не может совпадать с путём для сохранения",
                "Error: Source folder cannot be empty:": "Ошибка: Исходная папка не может быть пустой:",
                "Select the correct settings for copying.": "Укажите корректные параметры для копирования.",
                "Removed old copy from": "Удалена старая копия от",
                "Removed old copies:": "Удалено старых копий:",
                "Program removed from startup": "Программа удалена из автозапуска",
                "The program has been added to the startup": "Программа добавлена в автозапуск",
                "must be an integer.": "должно быть целым числом.",
                "The value of “logs_days” has been changed to:": "Значение 'logs_days' изменено на:",
                "Unable to make a copy due to missing source file, next attempt will be made via": "Невозможно сделать копию из-за отсутсвия исходного файла, следущая попытка будет выполнена через"
            }
        }

    def translate_ru(self, context, text):
        if context in self.translations_ru and text in self.translations_ru[context]:
            return self.translations_ru[context][text]
        return text

    def original_text(self, context, text):
        return text
