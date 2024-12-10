# Defines

def custom_write(file_name: str, strings: list[str]):
    """
    Функция записи списка строк в файл

    :param str file_name: Имя файла
    :param list[str] strings: Строки для записи
    :return: Словарь, ключом которого является кортеж вида (номер строки, первый байт строки), а значением -
    записанная строка
    """

    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = dict()
    for i in range(0, len(strings)):
        cursor_position = file.tell()
        file.write(f'{strings[i]}\n')
        strings_positions[(i + 1, cursor_position)] = strings[i]

    file.close()

    return strings_positions

# Code
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)