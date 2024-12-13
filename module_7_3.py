# Defines
from re import sub

class WordsFinder:
    """
    Класс поисковика

    Объект этого класса принимает список файлов, открывает их и собирает все строки, в них содержащиеся, в список.
    Методы класса позволяют найти первое вхождение слова в файле и подсчитать количество вхождений.

    Атрибуты объекта
    -----------------
    file_names: tuple(str)
        Имена файлов

    Методы класса
    -----------------
    __init__(*args)
        Конструктор: Инициализация
    get_all_words()
        Собрать все слова
    find(word: str)
        Поиск слова
    count(word: str)
        Подсчет вхождений
    """

    def __init__(self, *args):
        """
        Конструктор: Инициализация

        Метод инициализирует объект переданным кортежем, содержащим имена файлов, в которых юудет производится
        поиск
        """

        self.file_names = args

    def get_all_words(self):
        """
        Собрать все слова

        Метод собирает все слова из переданных объекту файлов и возвращает словарь, индексируемый именем файлов и
        содержащий все слова из каждого файла. В процессе составления словаря из текстовых строк вырезаются спецсимволы
        :return: Словарь всех слов, содержащихся в переданных объекту файлах
        """

        all_words = dict()

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                all_words[file_name] = sub("[,|.|=|!|?|;|:|-]", '', file.read()).lower().split()

        return all_words

    def find(self, word: str):
        """
        Поиск слова

        Метод ищет слово в словаре всех слов и возвращает позицию первого вхождения слова по всем переданным объекту
        файлам

        :param str word: Искомое слово
        :return: Позиция из словаря первого вхождения слова в файле
        """

        retval = dict()

        for key, words in self.get_all_words().items():
            for i in range(0, len(words)):
                if words[i] == word.lower():
                    retval[key] = i +1
                    break

        return retval

    def count(self, word: str):
        """
        Подсчет вхождений

        Метод подсчитывает число вхождений искомого слова в каждом файле
        :param str word: Искомое слово
        :return: Словарь, содержащий количество вхождений слова по каждому файлу
        """

        retval = dict()

        for key, words in self.get_all_words().items():

            retval[key] = 0

            for i in range(0, len(words)):
                if words[i] == word.lower():
                    retval[key] += 1

        return retval

# Code
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TExt'))
print(finder.count('teXt'))

finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('Child'))
print(finder2.count('cHilD'))

finder3 = WordsFinder('Rudyard Kipling - If.txt')
print(finder3.get_all_words())
print(finder3.find('YOU'))
print(finder3.count('yoU'))

finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder4.get_all_words())
print(finder4.find('captaIn'))
print(finder4.count('cAptaIn'))