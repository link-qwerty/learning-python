# Defines
class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor in range(1, self.number_of_floors + 1):
            print(f'Лифт отправился на этаж № {new_floor}, приятной поездки.')
            for i in range(1, new_floor + 1):
                print(i)
            print(f'Мы прибыли на этаж № {new_floor}, будьте осторожны при выходе из лифта.')
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __lt__(self, other):
        if not isinstance(other, House): return False
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House): return False
        return self.number_of_floors <= other.number_of_floors

    def __eq__(self, other):
        if not isinstance(other, House): return False
        return self.number_of_floors == other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House): return False
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House): return False
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House): return False
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

# Code
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__