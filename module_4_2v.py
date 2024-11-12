# Defines
from inspect import stack


def test_function(x):
    a = x ** 2
    def inner_function():
        b = a + 2
        return b
    print(f'Вывод результата работы функции test_function: {a}')
    print(f'Вывод результата работы функции inner_function из test_function: {inner_function()}')
    return inner_function

# Code
test_function(2) # normal call a = (2 ** 2) + 2
inner_function = test_function(1)
print(f'Вывод результата работы функции inner_function из глобального пространства: {inner_function()}')

print(test_function)
print(inner_function)