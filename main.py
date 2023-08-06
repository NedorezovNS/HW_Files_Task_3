from operator import itemgetter


def write_to_new():
    path_list = ['1.txt', '2.txt', '3.txt']  # Создаем список с путями до файлов
    names_and_length = dict.fromkeys(path_list)  # Создаем словарь, где ключ "Имя файла", а значение None
    for name in path_list:
        with open(name, 'r', encoding='UTF-8') as file:
            list_ = file.read().split('\n')
            length = 0
            for s in list_:  # Считаем количество строк в файле
                length += 1
            names_and_length[name] = length  # Записываем количество строк в значения ключей
    sorted_dict = dict(sorted(names_and_length.items(), key=itemgetter(1)))  # Сортируем словарь по значениям
    with open('4.txt', 'w', encoding='utf-8') as new_file:
        for name in sorted_dict.keys():
            new_file.write(f'{name}\n{sorted_dict[name]}\n')  # Записываем Название файла и количество строк в нем
            with open(name, 'r', encoding='UTF-8') as file2read:
                new_file.write(f'{file2read.read()}\n\n')  # Считываем строки файла и сразу записываем их в новый файл
    return new_file


write_to_new()
