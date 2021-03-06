'''
Данный модуль проходит по каждому файлу в папке
и задаёт данные о нём в словарь, которые в свою
очередь передаются в список
Прошу обратить внимание, что он не реализовывает
рекурсивный поиск, судя по заданию я решил что в этом
нет необходимости
Даты обе, создания и изменения (по возможности и зависит от ОС)
'''
import os
import platform # Модуль для определения ОС
import time # Для преобразования UNIX времени в человеко-читабельный

def dir_to_json(dirname: str) -> dict: # Обозначаем директорию
    json = {'data':[]}
    for name in os.listdir(dirname):
        dct = {} # Создаём пустой словарь, в который будем отдавать данные о файле

        full_path = os.path.join(dirname, name)
        file_type = os.path.splitext(full_path)[1]
        dct['name'] = os.path.splitext(os.path.basename(full_path))[0]

        if os.path.isfile(full_path): # Если файл - не папка, то задаём ему соответствующий тип
            dct['type'] = file_type
        elif os.path.isdir(full_path): # Если папка, то так и записываем
            dct['type'] = 'folder'

        # Начинаем смотреть и добавлять данные по дате файла
        if platform.system() == 'Windows': 
            # Если сервер запущен на Виндоус, то получить дату создания файла достаточно просто
            dct['created_at']= time.ctime(os.path.getctime(full_path))
            dct['modified_at'] = time.ctime(os.path.getmtime(full_path))
        else:
            stat = os.stat(full_path) # Для Mac и Linux
            try:
                dct['created_at'] = time.ctime(stat.st_birthtime)
            except AttributeError:
                # Утыкаемся в Линукс, получить время создания файла для него адекватным способом
                # Не представляется возможным, так что используем только время изменения
                dct['modified_at'] = time.ctime(stat.st_mtime)
        json['data'].append(dct) # Составляем итоговый json и возвращаем его
    return json

if __name__ == "__converter__":
    dir_to_json('../files')
