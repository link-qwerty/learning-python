# Imports
import random

# Defines
# Func for mirror double pairs search
def find_doubles(pairs, first, second):
    for pair in pairs:
        if pair[0] == second and pair[1] == first:
            return True
        else:
            continue

# Func for pairs search
def find_pairs(number):
    list_pairs = []
    for first in range(1, number):
        for second in range(1, number):
            if first != second:
                if not find_doubles(list_pairs, first, second):
                    delimiter = first + second
                    if number % delimiter == 0:
                        list_pairs.append([first, second])
    return list_pairs

# Func for humanized print of pairs
def print_password(number, pairs):
    password = '| '
    for pair in pairs:
      password += str(pair[0]) + ' + ' + str(pair[1]) + ' | '
    print(f'{number} = > {password}')

list_numbers = random.sample(range(3, 21), 18) # random numbers

# Code
#print(list_numbers)
for number in list_numbers:
    print_password(number, find_pairs(number))