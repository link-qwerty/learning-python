# Defines
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in data_set:
                file.write(f'{str(line)}\n')

    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)
# Code

# Lambda-function
result = map(lambda x, y: x == y,first, second)
print(list(result))

# Enclosure
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# __call__ method
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
