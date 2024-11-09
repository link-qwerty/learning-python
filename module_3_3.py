# Defines
def print_params(a=1, b='String', c=True):
    print(a, b, c)


values_list = [42, 'String', False]
values_dict = {'a': False, 'b': 42, 'c': 'String'}
values_list_2 = ['Von Braun', 3.24]

# Code
print_params()                          #call by default
print_params(b=25)                      #1st call
print_params(c=[1, 2, 3])               #2nd call
print_params(a='String')                #3rd call
print_params(*values_list)              #unpack list of values
print_params(**values_dict)             #unpack dict of values
print_params(*values_list_2, 42)     #unpack 2nd list of values