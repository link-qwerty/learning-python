# Defines
from threading import Thread
from time import sleep


class Knight(Thread):
    """
    Класс потока Рыцарь

    Объекты этого класса описывают некоего рыцаря (как-бы реконструктора, а иногда и просто сатаниста), который
    сражается с воображаемыми врагами в воображаемом фэнтезийном мире

    Методы класса
    ---------------
        __init__(self, name: str, power: int, weapon: str)
            Конструктор: инициализация
        fight(self)
            Сражение с врагами
        run(self)
            Запуск потока

    Атрибуты объекта
    ---------------
        :ivar str name: Имя рыцаря
        :ivar int power: Сила рыцаря
        :ivar str weapon: Оружие рыцаря
    """

    def __init__(self, name: str, power: int, weapon: str):
        """
        Конструктор: инициализация

        Инициализация класса переданными аргументами
        :param str name: Имя рыцаря
        :param int power: Сила рыцаря
        :param str weapon: Оружие рыцаря
        """

        Thread.__init__(self)
        self.name = name
        self.power = power
        self.weapon = weapon

    def fight(self):
        """
        Сражение с врагами

        Метод запускает процесс боя. Рыцарь сражается до тех пор, пока не победит всех врагов
        """

        warriors = 100
        days = 0

        while warriors > 0:
            warriors -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {days} дней(дня) используя {self.weapon}..., осталось '
                  f'{0 if warriors < 0 else warriors} ветряных мельниц.')


        print(f'{self.name} одержал победу спустя {days} дней(дня)! Благостно!')


    def run(self):
        """
        Запуск потока

        Метод запускает поток. Дополнительно может выполнять иные действия
        """

        print(f'{self.name}, на нас напали!')
        self.fight()

# Code
first_knight = Knight('Сир Вёдер', 30, 'Кирпич')
second_knight = Knight('Сир Артур', 20, 'Экскалибур')
third_knight = Knight('Дон Кихот', 15, 'Копье')

first_knight.start()
second_knight.start()
third_knight.start()

first_knight.join()
second_knight.join()
third_knight.join()

print("Все битвы закончились!")