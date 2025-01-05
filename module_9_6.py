# Defines
from uuid import uuid4

def all_variants(text: str):
    """
    Функция-генератор для строк

    Функция возвращает итератор, который перебирает все варианты подстрок в переданной строке
    :param str text: Переданная строка
    :return: Строковый итератор
    """

    for i in range(0, len(text) + 1):
        yield text[i:i + 1]

    for i in range(0, len(text) - 1):
        yield text[i:i + 2]

    yield text

    # Того же результата можно добиться следующим кодом, но вывод будет не отсортированным
    """for i in range(0, len(text) + 1):
        for j in range(0, len(text) + 1):
            yield text[i:j]"""

# Следующий генератор написал просто для примера
def gen_rnd_guid(n: int):
    """
    Функция генератор для GUID

    Функция генерирует заданное число идентификаторов GUID
    :param int n: Число генерируемых GUID
    :return: Генератор GUID
    """

    i = 0
    while i != n:
        yield uuid4()
        i += 1


# Code
a = all_variants("abc")

for i in a:
    print(i)

guids = gen_rnd_guid(10)

for i in guids:
    print(i)