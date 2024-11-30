# Defines
from time import sleep

class User:
    """
    Объекты этого класса предназначены для хранения данных о пользователях

    Атрибуты
    --------
    nickname : str
        Имя пользователя
    password : int
        Пароль пользователя (хэширован)
    age : int
        Возраст пользователя
    """

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname    # Имя пользователя
        self.password = password    # Пароль (хэширован)
        self.age = age              # Возраст

class Video:
    """
    Объекты этого класса предназначены для хранения данных о видеороликах

    Атрибуты
    --------
    title : str
        Имя пользователя
    duration : int
        Длительность видео
    time_now : int
        Текущая отметка времени
    adult_mode : bool
        Возрастное ограничение видео
    """

    def __init__(self, title: str, duration: int, time_now: int=0, adult_mode: bool=False):
        self.title = title              # Заголовок
        self.duration = duration        # Длительность
        self.time_now = time_now        # Текущая отметка
        self.adult_mode = adult_mode    # Взрослый контент


class UrTube:
    """
    Класс-синглетон, реализует механизмы идентификации/аутентификации пользователей, работы с видеороликами

    Атрибуты
    --------

    __instance : object
        Экземпляр класса (синглетон)
    __users : dict{User}
        Пользователи системы
    __videos : dict{Video}
        Коллекция видео
    __current_user : object
        Текущий пользователь системы

    Методы
    --------
    log_in(nickname: str, password: str)
        Осуществляет вход пользователя в систему
    register(nickname: str, password:str, age: int)
        Регистрирует пользователя в системе
    log_out()
        Осуществляет выход пользователя из системы
    add(*args: tuple[Video])
        Добавляет видеоролик в коллекцию
    get_videos(keyword: str)
        Выводит список видеороликов по ключевому слову
    watch_video(keyword: str)
        Проигрывает выбранный видеоролик
    """

    __instance = None       # Экземпляр класса (синглетон)
    __users = {}            # Словарь всех пользователей
    __videos = {}           # Список всех видеороликов
    __current_user = None   # Текущий пользователь в системе

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def log_in(self, nickname: str, password: str):
        if nickname in self.__users:
            if self.__users[nickname].password == hash(password):
                if self.__current_user:
                    print(f'В системе работает пользователь {self.__current_user.nickname}. Попросите его выйти')
                else:
                    self.__current_user = self.__users[nickname]
                    print(f'Пользователь {nickname} вошел в систему')
            else:
                print(f'Пароль пользователя {nickname} указан неверно')
        else:
            print(f'Пользователь {nickname} не зарегистрирован')

    def register(self, nickname: str, password:str, age: int):
        if nickname in self.__users:
            print(f'Пользователь {nickname} уже существует')
        else:
            last_user_nickname = 'Noname' if not self.__current_user else self.__current_user.nickname
            self.__current_user = User(nickname, hash(password), age)
            self.__users[nickname] = self.__current_user
            print(f'Пользователь {nickname} успешно зарегистрирован. Вход в систему под новым пользователем произведен.'
                  f'\nДо свидания, {last_user_nickname}')


    def log_out(self):
        if self.__current_user:
            print(f'Пользователь {self.__current_user.nickname} вышел из системы.')
            self.__current_user = None

    def add(self, *args: tuple[Video]):
        for video in args:
            if video.title in self.__videos:
                print(f'Такой видеоролик уже есть в коллекции.')
            else:
                self.__videos[video.title] = (video)
                print(f'Видеоролик добавлен в коллекцию.')

    def get_videos(self, keyword: str):
        for title, video in self.__videos.items():
            if keyword.upper() in title.upper():
                print(f'Найден видеоролик "{title}"')

    def watch_video(self, keyword: str):
        if self.__current_user:
            for title, video in self.__videos.items():
                if keyword.upper() == title.upper():
                    if self.__current_user.age < 18 and video.adult_mode:
                        print(f'Ты слишком мал для этого видео, {self.__current_user.nickname}. Сначала отпразнуй свою'
                              f' 18ю весну')
                    else:
                        print(f'Просмотр видеоролика "{title}"')
                        for i in range(0, video.duration + 1):
                            video.time_now = i
                            print(video.time_now, ' ', end='')
                            sleep(1)
                        print('Конец видеоролика')
                        video.time_now = 0
                    break
        else:
            print('В системе отсутствует пользователь. Залогиньтесь для просмотра.')

# Code

# Создание экземпляра главного обработчика
urT = UrTube()

# Проверка на дурака
urT.watch_video('Python для чайников')

# Регистрация пользователй
urT.register('Белое перо', 'Abudfv!', 14)
urT.register('Вася Пупкин', 'Gfhjkm', 22)
urT.register('Вася Пупкин', 'Gfhjkm', 22)
urT.register('Джон Буль', 'Moon4U', 31)

# Добавление видеороликов
urT.add(Video('Как производить двойную перегрузку операторов в Си++, не привлекая внимание санитаров', 20, adult_mode = True),
        Video('Python для чайников', 10),
        Video('Python для чайников', 10),
        Video('Как связаны Си++ и Оруэл', 5),
        Video('Трюки и хаки языка Python', 25),
        Video('ЮМОР_НЕ_ДЛЯ_ВСЕХ: Как ходит конь', 5, adult_mode = True))

# Идентификация и аутентификация
urT.log_in('Белое перо', 'Abudfv')
urT.log_in('Белое перо', 'Abudfv!')
urT.log_out()
urT.log_in('Белое перо', 'Abudfv!')

# Поиск видеороликов
urT.get_videos('Си++')
urT.get_videos('Python')
urT.get_videos('юмор')

# Воспроизведение видеороликов
urT.watch_video('Python для чайников')
urT.watch_video('ЮМОР_НЕ_ДЛЯ_ВСЕХ: Как ходит конь')
urT.log_out()

# А теперь поприветствуем Васю
urT.log_in('Вася Пупкин', 'Gfhjkm')
urT.watch_video('Как производить двойную перегрузку операторов в Си++, не привлекая внимание санитаров')