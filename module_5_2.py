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

# Code
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))