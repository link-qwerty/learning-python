# Defines

class Product:
    """
    Класс, описывающий продуктовый набор определенной категории

    Объекты класса содержат некий набор продуктов из определенной продуктовой категории

    Атрибуты объекта
    ---------------
        name : str
            Наименование продукта
        weight : float
            Вес продукта
        category : str
            Категория продукта

    Методы класса
    ---------------
        __init__(name: str, weight: float, category: str)
            Конструктор: инициализация
        __str__()
            Преобразование объекта в строку
    """

    def __init__(self, name: str, weight: float, category: str):
        """
        Конструктор: инициализация

        Метод инициализирует объекты класса Product, задавая наименование, вес и категорию продукта
        :param str name: Наименование продукта
        :param float weight: Вес продукта
        :param str category: Категория продукта
        """

        self.name = name
        self. weight = weight
        self.category = category

    def __str__(self):
        """
        Преобразование объекта в строку

        Метод возвращает строковое представление объекта класса Product, выводя все его поля в виде
        отформатированной строки
        :return: Строковое представление объекта
        """

        return f'{self.name}, {self. weight}, {self.category}'

class Shop:
    """
    Класс, описывающий некий магазин

    Объекты класса описывают некий магазин, торгующий товарами из определенных категорий

    Атрибуты объекта
    ---------------
        __name : str
            Название магазина
        __file_name : str
            Имя файла

    Методы класса
    ---------------
        __init__(name: str)
            Конструктор: инициализация
        get_products()
            Получить список продуктов со склада
        add(*products: Product)
            Добавить продукт на склад
        clear()
            Очистить склад
        get_name()
            Возвратить наименование магазина
    """

    def __init__(self, name: str):
        """
        Конструктор: инициализация

        Метод инициализирует объекты класса Shop, задавая название магазина. На этапе инициализации так же создается
        именованный файл склада, связанный с магазином.
        :param str name: Название магазина
        """

        self.__name = name
        self.__file_name = f'{name}_storage.txt'
        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):
        """
        Получить список продуктов со склада

        Метод открывает файл для чтения в текстовом режиме, считывает всю информацию и возвращает ее одной строкой
        :return: Строка, содержащая все имеющиеся в магазине продукты
        """

        file = open(self.__file_name, 'r')
        store_products = file.read()
        file.close()
        return store_products

    def add(self, *products: Product):
        """
        Добавить продукт на склад

        Метод записывает перечень принятых продуктов на склад. Если такой продукт уже есть на складе - он игнорируется
        :param Product products: Список продуктов, добавляемых на склад
        :return: None
        """

        store_products = self.get_products()
        file = open(self.__file_name, 'a')

        for product in products:
            if product.name not in store_products:
                file.write(f'{str(product)}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

        file.close()

    def clear(self):
        """
        Очистить склад

        Метод очищает текущий склад от продуктов. Реализовано простым открытием файла на запись (в этом момент
        происходит урезка файла до нулевой длины)
        :return: None
        """

        file = open(self.__file_name, 'w')
        file.close()

    def get_name(self):
        """
        Возвратить наименование магазина

        Метод возвращает наименование магазина. Поскольку атрибут наименования магазина создается защищенным, необходим
        метод, который его вернет пользователю. Существует лишь для того, чтобы пользователь мог узнать с чем он имеет
        дело, не листая код до момента создания магазина
        :return: Наименование магазина
        """

        return self.__name

# Code
s1 = Shop('Рога и копыта')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

# Let's try something else
print(s1.get_name())
s1.clear()
s1.add(p1, p2, p3)
print(s1.get_products())

