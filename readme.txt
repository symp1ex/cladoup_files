All versions of Windows x86-x64 are supported, starting with Windows 7 SP1.*

A program for automatically copying files at a specified interval. There are functions to work in the background and delete the oldest copies. Allows you to specify a specific target file or an entire folder as a copy source, which is copied while preserving the internal structure.  It has a graphical interface.

The program takes as arguments: the path to the folder\files to copy "source_path", the path to the folder to save "destination_path", the copying interval in seconds "interval" and the maximum number of simultaneously stored copies "max_copies".
When the number of copies made reaches the value specified in "max_copies", the program starts deleting the oldest copy each time a new copy is create. Copies are added to the specified path with the creation inside a folder named as the current timestamp.

Allows saving configs to separate files and selecting them for use.

Works in two modes:
1. Parameters for copying can be registered in the console window. Paths entered manually in the console window are separated by '\'.
2. Can be loaded from config.json. The paths specified in config.json must be separated by '\\'. 
If '"silence_mode": true' in config.json, then the program runs in the background and the start of the copy process does not require additional confirmation from the user after starting the program, and all output occurs in log.txt.

If you run several parallel processes of copying different files, then it is better to specify folders with different names along the save path, in order to avoid errors associated with creating folders with the same names inside the current timestamp.

"language": "en" - English (Google Translate)
"language": "ru" - Russian language.

*To work on Windows 7, you may need to install security update KB3063858. For the 32-bit version, the offline installer is in the archive.



Поддерживаются все версии Windows x86-x64, начиная с Windows 7 SP1.*

Программа для автоматического копирования файлов с заданным интервалом. Есть функции работы в фоновом режиме и удаления самых старых копий. Позволяет в виде источника копирования указывать конкретный конечный файл или целую папку, копирование которой происходит с сохранением внутренней струкртуры. Имеет графический интерфейс.

Программа принимает в виде аргументов: путь к папке\файлам для копирования "source_path", путь к папке для сохранения "destination_path", интервал копирования в секундах "interval" и максимально количество одновременно хранимых копий "max_copies". 
Когда количество сделанных копий достигает указанной в "max_copies" величины, программа начинает удалять самую старую копию при создании каждой следующей копии. Копии складываются по указанному пути с созданием внутри папки с именем в виде текущей метки времени.

Позволяет сохранять конфиги в отдельные файлы и выбирать их для использования.

	Работает в двух режимах:
1. Параметры для копирования можно прописать в окне консоли. Пути прописанные вручную в окне консоли разделяются через "\".
2. Можно подргрузить из config.json. Пути указанные в config.json обязательно разделяются через "\\". Если в config.json "silence_mode": true, то программа запускается в фоновом режиме и запуск процесса копирования не требует дополнительных подтверждений от пользователя после запуска программы, а весь вывод происходит в log.txt.

Если запускаете несколько параллельных процессов копирования разных файлов, то лучше по пути сохранения указывать папки с разными именами, во избежание ошибок связанных с созданием внутри папок с одинаковыми именами в виде текущей метки времени.

Для корректной работы с русским языком, необходимо зайти в языковые и региональные настройки windows и установить в разделе "Язык программ, не поддерживающих Юникод" Русский язык.

"language": "ru" - русский язык.
"language": "en" - английский язык (Google Translate)

*Для работы на Виндовс 7 может понадобиться установить обновление безопасности KB3063858. Для 32-бит версии автономный установщик лежит в архиве.