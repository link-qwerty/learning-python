# Defines
from queue import Queue
from random import randint
from threading import Thread
from time import sleep

class Table:
    """
    Класс столиков

    Объекты класса описывают столики в неком кафе

    Атрибуты объекта
    ----------------
        number (int):
            Номер столика
        guest (Guest):
            Обслуживаемый гость

    Методы класса
    ----------------
        __init__(self, number: int)
            Конструктор: Инициализация
    """

    def __init__(self, number: int):
        """
        Конструктор: Инициализация

        Метод инициализирует объект столика. По-умолчанию за столиком никого нет
        :param int number: Номер столика
        """

        self.number = number
        self.guest = None


class Guest(Thread):
    """
    Класс гостя

    Объекты класса описывают гостей кафе

    Атрибуты объекта
    ----------------
        name (str):
            Имя гостя

    Методы класса
    ----------------
        __init__(self, name: str)
            Конструктор: Инициализация
        run(self)
            Запуск потока
    """

    def __init__(self, name: str):
        """
        Конструктор: Инициализация

        Метод инициализирует объект гостя
        :param str name: Имя гостя
        """

        super().__init__()
        self.name = name

    def run(self):
        """
        Запуск потока

        Метод запускает поток-гостя
        :return: None
        """

        sleep(randint(3, 10))

class Cafe:
    """
    Класс кафе

    Объекты класса описывают некое кафе, обладающее материальными средствами (столиками) для обслуживания гостей.
    Обслуживающий персонал виртуален и в целях выполнения задания опускается

    Атрибуты объекта
    ----------------
        queue (Queue):
            Очередь обслуживания
        tables (Table)
            Свободные столики
        occupy_tables (Table)
            Занятые столики
        guests (int):
            Количество гостей

    Методы класса
    ----------------
        _init__(self, *tables: tuple[Table])
            Конструктор: Инициализация
        guest_arrival(self, *guests: tuple[Guest])
            Прибытие гостей
        discuss_guests(self)
            Обслуживание гостей
    """

    def __init__(self, *tables: tuple[Table]):
        """
        Конструктор: Инициализация

        Метод инициализирует объекты класса Cafe, записывая в атрибут tables столики, принадлежащие данному кафе.
        В целях сокращения и упрощения кода дополнительно введен атрибут occupy_tables, который отвечает за столики,
        занятые в данный момент. Две коллекции обмениваются объектами, в коде используется всегда первый элемент
        любой коллекции, что позволяет обойтись без лишних циклов перебора. Дополнительно введен счетчик гостей в
        кафе, чтобы программа знала когда завершать рабочий день (гостей нет - можно закрываться)
        :param tuple[Table] tables: Список столиков
        """

        self.queue = Queue()
        self.tables = list(tables)
        self.occupy_tables = list()
        self.guests = int(0)

    def guest_arrival(self, *guests: tuple[Guest]):
        """
        Прибытие гостей

        Метод имитирует прибытие гостей и рассадку их за свободные столики. Если свободных столиков нет, гость
        отправляется в очередь ожидания
        :param tuple[Guest] guests: Список прибывших гостей
        :return: None
        """
        self.guests = len(guests)

        for guest in guests:
            if len(self.tables) > 0:
                self.tables[0].guest = guest
                guest.start()
                guest.join()
                print(f'{guest.name} сел(-а) за стол номер {self.tables[0].number}')
                self.occupy_tables.append(self.tables.pop(0))
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        """
        Обслуживание гостей

        Метод имитирует обслуживание гостей. Процесс обслуживания запускается, если очередь не пуста и хотя бы
        один стол занят. Процесс обслуживания завершается, если все гости обслужены, довольны и ушли
        :return: None
        """

        while self.guests > 0:
            if len(self.occupy_tables) > 0:
                if not self.occupy_tables[0].guest.is_alive():
                    print(f'{self.occupy_tables[0].guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.occupy_tables[0].number} свободен')
                    self.occupy_tables[0].guest = None
                    self.guests -= 1
                    self.tables.append(self.occupy_tables.pop(0))
            if not self.queue.empty() and len(self.tables) > 0:
                self.tables[0].guest = self.queue.get()
                print(f'{self.tables[0].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[0].number}')
                self.tables[0].guest.start()
                self.tables[0].guest.join()
                self.occupy_tables.append(self.tables.pop(0))

# Code

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

# Завершение работы кафе
print("Обслуживание гостей завершено, кафе закрыто")