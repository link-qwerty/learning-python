# Defines

def is_prime(func):
    """
    Функция-декоратор

    :param func: Обертываемая функция
    :return: Обернутая функция
    """

    def wrapper(*args, **kwargs):
        """
        Обертка декоратора

        Переменная func замкнута, поэтому не передается в обертку в качестве аргумента
        """

        number = func(*args, **kwargs)
        f_prime = False

        for delimiter in range(2, number):
            if number % delimiter == 0:
                f_prime = False
                break
            else:
                f_prime = True

        if number == 2 or f_prime:
            print("Простое")
        elif number != 1:
            print("Составное")

        return number
    return wrapper

@is_prime
def sum_three(*args: int):
    """
    Функция, возвращающая сумму трех чисел

    :return: Сумма трех чисел
    """

    retval = 0
    for i in range(0, 3):
        retval += args[i]

    return retval

# Code
result = sum_three(2, 3, 6)
print(result)

result = sum_three(3, 3, 6)
print(result)