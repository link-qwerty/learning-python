# Defines

class Car:
    """
    Класс машины

    Объекты класса хранят данные о машинах, включая vin-кода и регистрационного номера

    Атрибуты объекта
    ----------------
        model [str]
            Модель машины
        __vin [int]
            VIN-код машины
        __numbers [str]
            Регистрационные номера машины

    Методы объекта
    ----------------
        __init(model: str, vin: int, numbers: str)
            Конструктор: Инициализация
        __is_valid_vin(vin_number: int)
            Проверка валидности vin-кода
        __is_valid_numbers(numbers: str)
            Проверка валидности регистрационного номера
    """

    def __init__(self, model: str, vin: int, numbers: str):
        """
        Конструктор: Инициализация

        Инициализирует объект-машину. Проводит ФЛК, при передаче некорректных данных вызывает исключения
        :param str model: Модель машины
        :param int vin: VIN-код
        :param str numbers: Регистрационный номер
        """

        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else 0
        self.__numbers = numbers if self.__is_valid_numbers(numbers) else ''

    def __is_valid_vin(self, vin_number: int):
        """
        Проверка валидности vin-кода

        Метод проверяет vin-кода на валидность. Вызывает исключения, если проверки не пройдены
        :param int vin_number: VIN-код
        :return: True, если проверка успешна
        """

        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif not vin_number in range(1000000, 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def __is_valid_numbers(self, numbers: str):
        """
        Проверка валидности регистрационного номера

        Метод проверяет регистрационный номер на валидность. Если проверка не пройдена, вызывает исключения
        :param str numbers: Регистрационный номер
        :return: True, если проверка успешна
        """

        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) > 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else:
            return True

class IncorrectVinNumber(Exception):
    """
    Пользовательское исключение

    Некорректный vin-номер
    """

    def __init__(self, message: str):
        """
        Конструктор: Инициализация

        :param str message: Сообщение об ошибке
        """

        self.message = message

class IncorrectCarNumbers(Exception):
    """
    Пользовательское исключение
    
    Некорректный номер машины
    """

    def __init__(self, message: str):
        """
        Конструктор: Инициализация

        :param str message: Сообщение об ошибке
        """

        self.message = message

# Code
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)

except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')