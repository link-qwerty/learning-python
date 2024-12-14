# Defines
import os, time, stat

# Code
for root, dirs, files in os.walk('.'):
    # Let's skip hidden files and dirs (for windows and linux)
    files = [f for f in files if not f[0] == '.' and not (os.stat(os.path.join(os.path.abspath(root), f)).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)]
    dirs[:] = [d for d in dirs if not d[0] == '.' and not (os.stat(os.path.join(os.path.abspath(root), d)).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)]

    # Parse results
    for file in files:
        filepath = os.path.join(os.path.abspath(root), file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.basename(os.path.dirname(filepath))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')