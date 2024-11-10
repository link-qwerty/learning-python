# Defines
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    count = 0
    if isinstance(data, int) or isinstance(data, float):
        count += data
    elif isinstance(data, str):
        count += len(data)
    elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for value in data:
            count += calculate_structure_sum(value)
    elif isinstance(data, dict):
        for key, value in data.items():
            count += calculate_structure_sum(key)
            count += calculate_structure_sum(value)
    return count

# Code
result = calculate_structure_sum(data_structure)
print(result)
