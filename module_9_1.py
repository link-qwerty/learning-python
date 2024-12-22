# Defines
def filter_list_handlers(arg: any):
    """
    Функция-обработчик для функции filter

    Функция-фильтр принимает на вход один аргумент любого типа и выполняет проверки над ним. Если аргумент является
    функцией и входит в список разрешенных функций, то возвращается True. Если аргумент не является функцией, но
    является целым числом, функция также возвращает True. В прочих случаях возвращается False
    :param any arg: Один аргумент любого типа
    :return: True, если проверки успешны. В противном случае - False
    """

    if callable(arg): # Защита от дурака
        if arg.__name__ in ('min', 'max', 'len', 'sum', 'sorted'):
            return True
        else:
            return False
    elif isinstance(arg, int):
        return True
    else:
        return False

def apply_all_func(int_list: list[int], *functions):
    """
    Выполнить все функции, обрабатывающие списки

    Функция принимает на вход список целочисленных значений, а также кортеж, содержащий функции, работающие со списками.
    Принятые аргументы фильтруются с помощью функции filter на предмет того, что в списке целочисленных значений
    содержатся именно целые числа, а в кортеже функций - именно определенные функции.
    :param list[int] int_list: Список целочисленных значений
    :param functions: Кортеж функций
    :return: Словарь, в котором результаты вычислений индексированы именем функции
    """

    results = dict()
    int_list = list(filter(filter_list_handlers, int_list))
    functions = filter(filter_list_handlers, functions)

    for func in functions:
        results [func.__name__] = func(int_list)

    return results

# Code
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
