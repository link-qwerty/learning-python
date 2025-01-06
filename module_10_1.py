# Defines
from time import time, sleep
import threading

def write_words(word_count: int, file_name: str):
    """
    Запись массива слов в файл

    Функция записывает некоторое количество слов в файл, производя дополнительную нумерацию записанных строк
    :param int word_count: Количество записываемых слов
    :param str file_name: Имя файла для записи
    """

    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

# Code
start_time = time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200,"example3.txt")
write_words(100,"example4.txt")

elapsed_time = time() - start_time
print("Работа потоков %d:%02d:%02.06f" % (elapsed_time // 120, elapsed_time // 60 , elapsed_time))

start_time = time()

second_thread = threading.Thread(target = write_words, args = (10, "example5.txt"))
third_thread = threading.Thread(target = write_words, args = (30, "example6.txt"))
fourth_thread = threading.Thread(target = write_words, args = (200, "example7.txt"))
fifth_thread = threading.Thread(target = write_words, args = (100, "example8.txt"))

second_thread.start()
third_thread.start()
fourth_thread.start()
fifth_thread.start()

second_thread.join()
third_thread.join()
fourth_thread.join()
fifth_thread.join()

elapsed_time = time() - start_time
print("Работа потоков %d:%02d:%02.06f" % (elapsed_time // 120, elapsed_time // 60 , elapsed_time))
