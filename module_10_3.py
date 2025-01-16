# Defines
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:
    """
    Класс банка

    Объекты класса описывают банк, на счетах которого происходят движения средств

    Методы класса
    ---------------
        __init__(self)
            Конструктор: Инициализация
        deposit(self)
            Внесение средств
        take(self)
            Снятие средств

    Атрибуты объекта
    ---------------
        :ivar int balance: Баланс счета
        :ivar Lock lock: Блокировка
    """

    def __init__(self):
        """
        Конструктор: Инициализация
        """

        self.balance = int(0)
        self.lock = Lock()

    def deposit(self):
        """
        Внесение средств

        Метод вносит средства на депозит
        """

        for i in range(100):
            rand_val = randint(50, 500)
            self.balance += rand_val

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            print(f'Пополнение: {rand_val}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        """
        Снятие средств

        Метод снимает средства с депозита
        """

        for i in range(100):
            rand_val = randint(50, 500)

            print(f'Запрос на {rand_val}')

            if rand_val <= self.balance:
                self.balance -= rand_val
                print(f'Снятие: {rand_val}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

# Code
bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')