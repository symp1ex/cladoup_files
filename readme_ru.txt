Программа для автоматического копирования файлов с заданным интервалом. Есть функции работы в фоновом режиме и удаления самых старых копий. Позволяет в виде источника копирования указывать конкретный конечный файл или целую папку, копирование которой происходит с сохранением внутренней струкртуры.

Программа принимает в виде аргументов: путь к папке\файлам для копирования "source_path", путь к папке для сохранения "destination_path", интервал копирования в секундах "interval" и максимально количество одновременно хранимых копий "max_copies". 
Когда количество сделанных копий достигает указанной в "max_copies" величины, программа начинает удалять самую старую копию при создании каждой следующей копии. Копии складываются по указанному пути с созданием внутри папки с именем в виде текущей метки времени.

	Работает в двух режимах:
1. Параметры для копирования можно указать в интерфейсе. Пути указанные вручную разделяются через "\".
2. Можно подргрузить из config.json. Пути указанные в config.json обязательно разделяются через "\\". Если в config.json "silence_mode": true, то программа запускается в фоновом режиме и запуск процесса копирования не требует дополнительных подтверждений от пользователя после запуска программы, а весь вывод происходит в log.txt.

Если запускаете несколько параллельных процессов копирования разных файлов, то лучше по пути сохранения указывать папки с разными именами, во избежание ошибок связанных с созданием внутри папок с одинаковыми именами в виде текущей метки времени.

Для корректной работы с русским языком, необходимо зайти в языковые и региональные настройки windows и установить в разделе "Язык программ, не поддерживающих Юникод" Русский язык.

"language": "ru" - русский язык.
"language": "en" - английский язык (Google Translate)