# Defines

class StepValueError(ValueError):
    """
    Класс исключения

    Класс пользовательского исключения, вызываемого при неверном указании значения шага итерации
    """

    pass

class StartStopValueError(ValueError):
    """
    Класс исключения

    Класс пользовательского исключения, вызываемого при неверном указании значений начала и конца итерации
    """

    pass

class Iterator:
    """
    Класс целочисленного итератора

    Класс пользовательского итератора для целочисленных периодов. Ситуации с неверным указанием начальных значений
    отрабатываются пользовательскими исключениями

    Атрибуты объекта
    ----------------
        start: int
            Начало периода итерации
        stop: int
            Конец периода итерации
        step: int
            Шаг итерации

    Методы класса
    ----------------
        __init__(self, start: int, stop: int, step: int = 1)
            Конструктор: Инициализация
        __iter__(self)
            Инициализация итератора
        __next__(self)
            Выполнить итерацию
    """

    def __init__(self, start: int, stop: int, step: int = 1):
        """
        Конструктор: Инициализация

        :param int start: Начало периода итерации
        :param int stop: Конец периода итерации
        :param int step: Шаг итерации
        """

        self.start = start
        self.stop = stop
        self.pointer = start

        if step == 0:
            raise StepValueError('шаг не может быть равен нулю')
        elif start > stop and step > 0:
            raise StartStopValueError('значение старта не может быть больше значения конца итерации при положительном '
                                      'шаге итерации')
        elif start < stop and step < 0:
            raise StartStopValueError('значение старта не может быть меньше значения конца итерации при положительном '
                                      'шаге итерации')
        else:
            self.step = step

    def __iter__(self):
        """
        Инициализация итератора

        Метод инициализирует итератор, сбрасывая счетчик к начальному значению
        :return: Объект итератора
        """

        self.pointer = self.start
        return self

    def __next__(self):
        """
        Выполнить итерацию

        Метод выполняет шаг итерации, в процессе увеличивая счетчик на шаг итерации до момента достижения конца периода
        :return: Счетчик итерации
        """

        retval = self.pointer

        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
            else:
                self.pointer += self.step
        elif self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration()
            else:
                self.pointer += self.step

        return retval

# Code
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')

except StepValueError as err:
    print(f'Шаг указан неверно, {err}')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StartStopValueError as err:
    print(f'Начало и конец итерации заданы неверно, {err}')

try:
    iter6 = Iterator(-10, 1, -1)
    for i in iter6:
        print(i, end=' ')
except StartStopValueError as err:
    print(f'Начало и конец итерации заданы неверно, {err}')