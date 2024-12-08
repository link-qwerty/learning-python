# Defines
from random import randint

class Animal:
    """
    Базовый класс для представителей царства животных

    Объект этого класса обладает атрибутами и методами, общими для всех представителей царства животных, будь-то
    зверь, рыба или птица. Все животные обладают скоростью передвижения, рейтингом опасности и издают звуки

    Атрибуты класса
    ---------------
    live: bool - Признак того что животное живо

    sound: str - Звук, издаваемый животным

    _DEGREE_OF_DANGER: int - Рейтинг опасности животного

    Атрибуты объекта
    ---------------
    _cords: list[int] - Координаты животного

    _speed: int - Скорость животного

    Методы класса
    ---------------
    __init(speed: int = 6) - Конструктор: инициализация

    move(dx: int, dy: int, dz: int) - Действие движения

    get_cords() - Текущие координаты животного

    attack() - Действие атаки

    speak() - Сказать что-то свободным действием

    info() - Вывод информации о животном
    """

    live: bool = True
    sound: str = None
    _DEGREE_OF_DANGER: int = 0

    def __init__(self, speed: int = 6, sound: str = None):
        """
        Конструктор: инициализация

        Метод инициализирует животное, обладающее общими признаками для всех представителей царства животных
        :param speed: Скорость передвижения
        """

        self._cords = [0, 0, 0]
        self._speed = speed
        self.sound = sound

    def move(self, dx: int, dy: int, dz: int):
        """
        Действие движения

        По умолчанию животное перемещается на 6 клеток. Если оно не роющее, то под землю перемещаться не может
        :param dx: дельта по координате x
        :param dy: дельта по координате y
        :param dz: дельта по координате z
        :return: None
        """
        if self.live:
            if dz > 3:
                print("I can't climb too far")
            else:
                if dz * self._speed >= 0:
                    self._cords = [self._cords[0] + (dx * self._speed),
                                   self._cords[1] + (dy * self._speed),
                                   self._cords[2] + (dz * self._speed)]
                    print("Oscar mike")
                else:
                    print("It's too deep, i can't dive underground")
        else:
            print("Dead can't dance")

    def get_cords(self):
        """
        Текущие координаты животного

        Вывод в консоль координаты животного и возвращает их вызывающему
        :return: list[x: int, y: int, z: int]
        """

        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
        return self._cords

    def attack(self):
        """
        Действие атаки

        Выводит в консоль результаты атаки животного и нанесенный урон
        :return: None
        """

        if self._DEGREE_OF_DANGER >= 5:
            print(f'Be careful, i\'m attacking you 0_0. You took {randint(1, self._DEGREE_OF_DANGER)} damage')
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        """
        Сказать что-то свободным действием

        Выводит в консоль крик животного
        :return: None
        """

        print(f'{self.sound if self.sound else "This animal is mute"}')

    def info(self):
        """
        Вывод информации о животном

        Выводит в консоль информацию о животном
        :return: None
        """

        print(f'This animal {'live' if self.live else 'dead'} '
              f'and it\'s degree of danger equal: {self._DEGREE_OF_DANGER}')

class Bird(Animal):
    """
    Класс, описывающий птиц

    Объекты этого класса обладают атрибутами и методами, характерными для представителей рода птиц

    Атрибуты класса
    ---------------
    beak: bool - Наличие ключа

    Методы класса
    ---------------
    lay_eggs() - Отложить яйца

    flight(dx: int, dy: int, dz: int) - Действие полета
    """

    beak = True

    def lay_eggs(self):
        """
        Отложить яйца

        Животное откладывает яйца в количестве от 1 до 4
        :return: None
        """

        print(f'Here are(is) {randint(1, 4)} eggs for you')

    def move(self, dx: int, dy: int, dz: int):
        """
        Действие движения для птиц

        Птицы хорошо летают, но неуклюже передвигаются на своих двоих (не берем в расчет нелетающих птиц)
        :param dx: дельта по координате x
        :param dy: дельта по координате y
        :param dz: дельта по координате z
        :return: None
        """

        super().move(dx / 2, dy / 2, dz / 2)

    def flight(self, dz: int):
        """
        Действие полета

        Птицы умеют летать. Перемещение действием полета производится с увеличенной вдвое скоростью
        :param dz: дельта по координате z
        :return: None
        """

        if self.live:
            if dz * self._speed >= 0:
                self._cords[2] += dz * self._speed * 2
                print("I'm fly!")
            else:
                print("It's too deep, i can't fly underground")
        else:
            print("Dead can't fly")

    def info(self):
        """
        Вывод информации о птице

        Выводит в консоль информацию о животном
        :return: None
        """

        print(f'This animal is bird and has {'beak' if self.beak else 'feathers'}')
        super().info()

class AquaticAnimal(Animal):
    """
    Класс, описывающий водных животных

    Объекты этого класса обладают атрибутами и методами, характерными для водных животных

    Атрибуты класса
    ---------------
    _DEGREE_OF_DANGER: int - Рейтинг опасности водного животного (достаточно опасны)

    Методы класса
    ---------------
    dive_in(dz: int) - Действие погружения для водных животных
    """

    _DEGREE_OF_DANGER = 3

    def move(self, dx: int, dy: int, dz: int):
        """
        Действие движения для водных животных

        Водные животные хорошо плавают, но неуклюже передвигаются на своих двоих (не берем в расчет рыб и китов)
        :param dx: дельта по координате x
        :param dy: дельта по координате y
        :param dz: дельта по координате z
        :return: None
        """

        super().move(dx / 3, dy / 3, dz / 3)

    def dive_in(self, dz: int):
        """
        Действие погружения для водных животных

        Перемещение действием нырка производится с уменьшенной вдвое скоростью
        :param dz: дельта по координате z
        :return: None
        """

        if self.live:
           self._cords[2] -= (abs(dz) * self._speed) / 2
           print("I'm dive!")
        else:
            print("Dead can't dive")

    def info(self):
        """
        Вывод информации о водном животном

        Выводит в консоль информацию о животном
        :return: None
        """

        print("This animal is aquatic and can dive")
        super().info()

class PoisonousAnimal(Animal):
    """
    Класс, описывающий ядовитых животных

    Атрибуты класса
    ---------------
    _DEGREE_OF_DANGER: int - Рейтинг опасности ядовитого животного (очень опасно)
    """

    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    """
    Класс, описывающий утконоса

    Утконос это водоплавающая птица, не умеющая летать, имеющая ядовитые когти на лапах
    """

    def move(self, dx: int, dy: int, dz: int):
        """
        Действие движения для утконоса (игнорирует переопределенные методы для птиц и водных животных)

        По умолчанию животное перемещается на 6 клеток. Если оно не роющее, то под землю перемещаться не может
        :param dx: дельта по координате x
        :param dy: дельта по координате y
        :param dz: дельта по координате z
        :return: None
        """

        Animal.move(self, dx, dy, dz)

    def flight(self, dz: int):
        """
        Утконос не может летать
        :param dz:
        :return:
        """
        print("I can't flight")

# Code

print("-" * 5, "Duckbill", "-" * 5)

# Создадим нашего утконоса и посмотрим на него
db = Duckbill(10,  "Click-click-click")
db.info()

# Как утконос перемещается по твердой поверхности
db.move(1, 2, -1) # Нельзя зарыться под землю
db.move(2, 2, 12) # Нельзя прыгнуть выше головы
db.flight(10) # Утконос не может летать
db.move(1, 2, 3) # Перемещение успешно
db.get_cords() # Где сейчас наш утконос
db.dive_in(6) # Утконос может нырять
db.get_cords() # Где сейчас наш утконос

# Что может утконос
db.lay_eggs() # Откладывает яйца
db.speak() # Песня утконоса
db.attack() # Утконос атакует

print("-" * 5, "Walrus", "-" * 5)

# Создадим моржа
wlr = AquaticAnimal(10, "Roar!")
wlr.info()

# Как морж перемещается по твердой поверхности
wlr.move(1, 2, -1) # Нельзя зарыться под землю
wlr.move(2, 2, 12) # Нельзя прыгнуть выше головы
wlr.move(1, 2, 3) # Перемещение успешно
wlr.get_cords() # Где сейчас наш морж
wlr.dive_in(6) # Морж может нырять
wlr.get_cords() # Где сейчас наш морж

# Что может морж
wlr.speak() # Рев моржа
wlr.attack() # Морж атакует

print("-" * 5, "Sparrow", "-" * 5)

# Создадим воробья
spr = Bird(10, "Kwick-kwick")
spr.info()

# Как воробей перемещается по твердой поверхности
spr.move(1, 2, -1) # Нельзя зарыться под землю
spr.move(2, 2, 12) # Нельзя прыгнуть выше головы
spr.move(1, 2, 3) # Перемещение успешно
spr.get_cords() # Где сейчас наш воробей
spr.flight(6) # Воробей может летать
spr.get_cords() # Где сейчас наш воробей

# Что может воробей
db.lay_eggs() # Откладывает яйца
spr.speak() # Чириканье воробья
spr.attack() # Воробей атакует