# Defines

def personal_sum(numbers: tuple[int]):
    """
    Функция суммирования элементов кортежа

    Функция принимает на вход кортеж и пытается произвести суммирование всех элементов типов (int, float), которые
    в него входят. Если встреченный в кортеже элемент не относится к указанным типам, то он пропускается, а счетчик
    некорректных данных увеличивается на 1
    :param numbers: Кортеж элементов, принимаемых для суммирования
    :return: Кортеж, содержащий результат суммирования и количество некорректных данных
    """

    result = 0
    incorrect_data = 0

    try:
        for number in numbers:
            result += number
    except TypeError as te:
        incorrect_data += 1
        print(f'В процессе перебора значений вызвано исключение: {te}, аргументы {te.args}\n'
              f'Количество некорректных данных: {incorrect_data}')
    return result, incorrect_data

def  calculate_average(numbers: tuple[int]):
    """
    Функция вычисления средней суммы

    Функция принимает кортеж чисел и пытается вычислить среднюю сумму значений по элементам, входящим в кортеж
    :param numbers: Кортеж элементов, принимаемых для суммирования
    :return: Результат - средняя сумма всех значений, входящих в кортеж
    """

    result = 0
    summ = personal_sum(numbers)
    try:
        result = summ[0] / len(numbers) - summ[1]
    except ZeroDivisionError as zde:
        print(f'В процессе вычисления выражения вызвано исключение: {zde}, аргументы {zde.args}\n'
              f'Передан пустой кортеж чисел')
        return 0
    except TypeError as te:
        print("В numbers записан некорректный тип данных")
        return None
    return result

# Code
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
