# Defines

def add_everything_up(a, b):
    try:
        return round((a + b), 4)
    except TypeError as exc:
        print(f'Args type mismatch, {exc}\n Arg a is {type(a)}, arg b is {type(b)}')
        return str(a) + str(b)

# Code
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

