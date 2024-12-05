# Defines

class Vehicle:
    """
    Базовый класс для всех автомобилей

    Атрибуты класса
    _________________
    __COLOR_VARIANTS:List(str) - Список возможных цветов, в которые можно окрасить автомобиль

    Атрибуты объектов
    _________________
    owner:str - Владелец авто

    model:str - Модель авто

    engine_power:int - Мощность двигателя

    color:str - Цвет кузова
    """

    __COLOR_VARIANTS = ['серый', 'темно-серый', 'черный', 'темно-синий', 'синий', 'салатовый', 'баклажан', 'белый', 'оранжевый', 'желтый']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        """
        Инициализация автомобиля

        :param owner: Владелец
        :param model: Модель авто
        :param engine_power: Мощность двигателя
        :param color: Цвет кузова
        """

        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        """
        Выводит в консоль модель автомобиля
        :return: None
        """

        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        """
        Выводит в консоль мощность двигателя
        :return: None
        """

        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        """
        Выводит в консоль цвет кузова
        :return: None
        """

        print(f'Цвет: {self.__color}')

    def print_info (self):
        """
        Печатает сведения по автомобилю
        :return: None
        """

        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        """
        Задает новый цвет кузова из списка имеющихся
        :param new_color: Новый цвет кузова автомобиля
        :return: None
        """
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    """
    Производный от Vehicle класс седана

    Атрибуты класса
    _________________
    __PASSENGERS_LIMIT:int - Максимальная вместимость автомобиля
    """
    __PASSENGERS_LIMIT = 5

# Code

# Create vehicle
vehicle1 = Sedan('Пупкин Василий', 'Lada Priora', 120, 'баклажан')
# Print info about vehicle
vehicle1.print_info()
# Change attr
vehicle1.set_color('Зеленый')
vehicle1.set_color('ЧеРнЫй')
vehicle1.owner = 'Саркисян Гамлет'
# Print info about vehicle
vehicle1.print_info()