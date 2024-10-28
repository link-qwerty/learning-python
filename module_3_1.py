# Defines
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    t_info = len(string), string.upper(), string.lower()
    return t_info

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.lower() == item.lower():
            return True
    return False

calls = 0

# Code
print(string_info('Marie Delacroix'))
print(string_info('Von Braun'))
print(is_contains('Abyrvalg', ['aByrvalg', 'GlavRyba', 'empty']))
print(is_contains('Linux', ['penguin', 'Torvalds', 'Linus']))
print(calls)