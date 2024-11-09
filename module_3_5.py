# Defines
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n

# Code
print(f'Перемножение элементов числа 40203: {get_multiplied_digits(40203)}')
print(f'Факториал 10: {factorial(10)}')
