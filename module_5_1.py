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

# Code
h1 = House('ЖК Горский', 25)
h2 = House('Домик в деревне', 2)
h1.go_to(15)
h2.go_to(10)