# Defines
from math import prod, pi, sqrt


class Figure:
    """
    Базовый класс для геометрических фигур

    Содержит атрибуты и методы, общие для всех геометрических фигур

    Атрибуты класса
    ---------------
    sides_count int: Число сторон

    Атрибуты объекта
    ---------------
    __color tuple(int, int, int): Цвет фигуры

    __sides list[int]: Стороны фигуры

    Методы класса
    ---------------
    __init__(color: (int, int, int), *args) - Конструктор: инициализация

    __is_limit_lay(number: int, base: int =0 , end: int = 255) - Проверка вхождения числа в предел

    __is_valid_color(r: int, g: int, b: int) - Проверка корректности цвета

    __is_valid_sides(*args) - Проверка корректности сторон

    get_color() - Взять цвет фигуры

    set_color(r: int, g: int, b: int) - Задать цвет фигуры

    get_sides() - Взять стороны

    set_sides(*new_sides) - Задать стороны

    __len__() - Узнать периметр фигуры
    """
    sides_count = 0

    def __init__(self, color: (int, int, int), *args):
        """
        Конструктор: инициализация

        Инициализирует фигуру переданными параметрами цвета и размерами сторон. Если параметры переданы неверно,
        то фигура инициализируется параметрами по умолчанию

        :param tuple(int, int, int) color: Цвет фигуры
        :param args: Стороны фигуры
        """

        self.__color = color if self.__is_valid_color(color[0], color[1], color[2]) else [255, 255, 255]
        self.__sides = args if self.__is_valid_sides(*args) else [1] * self.sides_count
        self.filled = False

    def __is_limit_lay(self, number: int, base: int =0 , end: int = 255):
        """
        Проверка вхождения числа в предел

        Простая сервисная функция для определения лежит ли число в определенных границах
        :param int number: Искомое число
        :param int base: Нижняя граница поиска
        :param int end: Верхняя граница поиска
        :return: True, если число находится в границах указанного диапазона и False - если нет
        """

        return True if number in range(base, end) else False

    def __is_valid_color(self, r: int, g: int, b: int):
        """
        Проверка корректности цвета

        Проверяет переданные в параметрах числовые компоненты цвета на корректность. Значения должны лежат в
        диапазоне от 0 до 255 и быть целыми неотрицательными числами

        :param int r: Красная компонента цвета
        :param int g: Зеленая компонента цвета
        :param int b: Синяя компонента цвета
        :return: True если переданные параметры корректны и False в противном случае
        """
        if self.__is_limit_lay(r) and self.__is_limit_lay(r) and self.__is_limit_lay(b) and r * g * b >= 0:
            if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
                return True
            else:
                return False
        else:
            return False

    def __is_valid_sides(self, *args):
        """
        Проверка корректности сторон

        Производит проверку переданных размеров сторон на корректность. Если число сторон не равно количеству
        сторон фигуры, размер сторон это не целые неотрицательные числа - возвращает False

        :param args: Список сторон, содержащий целые неотрицательные числа (ну так должно быть)
        :return: True, если переданные в параметрах стороны корректны, и False - в противном случае
        """

        if len(args) == self.sides_count and prod(args) >= 0 and isinstance(prod(args), int):
            return True
        else:
            return False

    def get_color(self):
        """
        Взять цвет фигуры

        Возвращает цвет фигуры в формате RGB (в виде списка)

        :return: Список, содержащий цвет фигуры в формате RGB[red, green, blue]
        """

        return list(self.__color)

    def set_color(self, r: int, g: int, b: int):
        """
        Задать цвет фигуры

        Задает цвет фигуры согласно переданным параметрам. Компоненты цвета должны лежат в пределах от 0 до 255

        :param int r: Красная компонента цвета
        :param int g: Зеленая компонента цвета
        :param int b: Синяя компонента цвета
        :return: True если цвет установлен и False в противном случае
        """

        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            return True
        else:
            return False

    def get_sides(self):
        """
        Взять стороны

        Метод возвращает числовые значения сторон в виде списка
        :return: Список сторон, содержащий числовые значения сторон
        """

        return list(self.__sides)

    def set_sides(self, *new_sides):
        """
        Задать стороны

        Устанавливает новые длины сторон. Если количество переданных сторон равно таковому у фигуры, то происходит
        замена сторон на новые. Если количество переданных сторон не совпадает с количеством сторон у фигуры, то
        замена сторон не происходит
        :param new_sides: Новые стороны фигуры
        :return: True, если операция успешна, False в ином случае
        """

        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
            return True
        else:
            return False

    def __len__(self):
        """
        Узнать периметр фигуры

        Возвращает сумму всех сторон фигуры
        :return: Сумма сторон фигуры
        """
        return sum(self.__sides)

class Circle(Figure):
    """
    Класс, описывающий круг

    Фигура лежит на плоскости и обладает методами, свойственными для 2D фигур

    Атрибуты класса
    ---------------
    sides_count int: Число сторон

    Атрибуты объекта
    ---------------
    __radius int: Радиус окружности

    Методы класса
    ---------------
    get_square() - Узнать площадь круга
    """

    sides_count = 1

    def __init__(self, color: (int, int, int), *args):
        """
        Конструктор: инициализация

        Инициализирует круг переданными параметрами цвета и размерами сторон (передача управления в суперкласс).
        Если параметры переданы некорректно, то фигура инициализируется параметрами по умолчанию. Дополнительно считает
        радиус окружности

        :param list[int, int, int] color: Цвет фигуры
        :param args: Стороны фигуры
        """

        self.__radius = args[0] / pi if args[0] > 0 else 1 / pi
        super().__init__(color, *args)

    def get_square(self):
        """
        Узнать площадь круга

        Рассчитывает площадь круга по его радиусу

        :return: Площадь круга
        """

        return self.__radius * 2 * pi

class Triangle(Figure):
    """
    Класс, описывающий треугольник

    Фигура лежит на плоскости и обладает методами, свойственными для 2D фигур

    Атрибуты класса
    ---------------
    sides_count int: Число сторон

    Методы класса
    ---------------
    get_square() - Узнать площадь треугольника
    """

    sides_count = 3

    def __init__(self, color: (int, int, int), *args):
        """
        Конструктор: инициализация

        Инициализирует треугольник переданными параметрами цвета и размерами сторон (передача в суперкласс).
        Если передается одна сторона, то создается равносторонний треугольник. В ином случае создается фигура
        по умолчанию

        :param tuple(int, int, int) color: Цвет фигуры
        :param args: Стороны фигуры
        """

        if len(args) == self.sides_count:
            super().__init__(color, args)
        else:
            if len(args) == 1:
                super().__init__(color, *tuple([args[0]] * self.sides_count))
            else:
                super().__init__(color, args)

    def get_square(self):
        """
        Возвращает площадь треугольника

        Рассчитывает площадь треугольника по формуле Герона

        :return: Площадь треугольника
        """

        p = self.__len__()/2
        return sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))

class Cube(Figure):
    """
    Класс, описывающий куб

    Фигура находится в 3D пространстве и обладает методами, свойственными для 3D фигур

    Атрибуты класса
    ---------------
    sides_count int: Число сторон

    Методы класса
    ---------------
    get_volume() - Узнать объем куба
    """

    sides_count = 12

    def __init__(self, color: (int, int, int), *args):
        """
        Конструктор: инициализация

        Инициализирует куб переданными параметрами цвета и размерами сторон (передача в суперкласс).
        Если количество передаваемых сторон равно количеству сторон фигуры, то выбирается наибольшее значение и
        по нему создаются все стороны. Если передается одна сторона, то все стороны куба будут равны ее значению.
        В ином случае создается фигура по умолчанию

        :param tuple(int, int, int) color: Цвет фигуры
        :param args: Стороны фигуры
        """

        if len(args) == self.sides_count:
            super().__init__(color, max(args))
        else:
            if len(args) == 1:
                super().__init__(color, *tuple([args[0]] * self.sides_count))
            else:
                super().__init__(color, args)

    def get_volume(self):
        """
        Узнать объем куба

        Возвращает объем куба, рассчитанный по формуле Герона
        :return: Объем фигуры
        """

        return self.get_sides()[0] ** 3

    def set_sides(self, *new_sides):
        """
        Устанавливает новые стороны (перегружен)

        Устанавливает новые длины сторон куба. У куба все ребра равны, поэтому будет установлена наибольшая
        по длине сторона. Если число переданных параметров меньше, чем число сторон, то изменение не произойдет

        :param new_sides: Новые стороны фигуры
        :return: True, если операция успешна и False в противном случае
        """
        if len(new_sides) == self.sides_count:
            super().set_sides(max(new_sides))
            return True
        else:
            return False

    def __len__(self):
        """
        Узнать периметр фигуры (перегружен)

        Периметр может существовать только у фигур, лежащих на плоскости. У куба периметра нет
        :return: None
        """

        return None0

# Code
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(cube1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Прочие проверки
triangle1 = Triangle((23.23, 45.7, 23), 12)
print(triangle1.get_color())
print(triangle1.get_sides())
triangle1.set_color(23, 45, 23)
triangle1.set_sides(4, 3, 5)
print(triangle1.get_color())
print(triangle1.get_sides())
print(triangle1.get_square())
