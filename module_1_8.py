# Init
my_dict = {'Melanie Bronson': 2035, 'Grassi': 1939, 'James Watts': 1941, 'Marie Delacroix': 2043}
my_set = {1, 2, 3, 4, 5, 3, 1, 'string', 6.1, 8, 2, 4, 6.1, 'string', (1, 0.2, 45.1)}

# Code - dict
print('Dict:', my_dict)
print('Existing value:', my_dict['Grassi'])
print('Non-existing value:', my_dict.get('Malick', False))
print('Delete value:', my_dict.pop('James Watts'))
print('Modified dictionary:', my_dict, '\n')

# Code - set
print('Set:', my_set)
my_set.add(10)
my_set.add(22)
my_set.remove(4)
print('Modified set:', my_set)