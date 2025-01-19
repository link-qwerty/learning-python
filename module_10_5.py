# Defines
from datetime import datetime
from multiprocessing import Pool


def read_info(name: str):
    """
    Функция чтения данных из файла

    Функция читает построчно данные из файла, задаваемого аргументом name
    :param str name: Имя файла
    :return: None
    """

    all_data = list()

    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != '':
            line = file.readline()
            all_data.append(line)

# Code

# Generate list
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Linear calls
"""start = datetime.now()
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
end = datetime.now()
print(end-start, 'Линейный вызов')"""

# Multiprocessing calls

if __name__ == '__main__':
    start = datetime.now()
    with Pool(4) as pl:
        pl.map(read_info, filenames)
    end = datetime.now()
    print(end-start, 'Мультипроцессный вызов')

