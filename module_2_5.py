# Def block

# Function for get matrix
def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix.append(list())
        for j in range(0, m):
            matrix[i].append(value)
    return matrix

# Function for print matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Code block
print("Matrix 3x3:")
print_matrix(get_matrix(3, 3, 10))
print("Matrix 4x5:")
print_matrix(get_matrix(4, 5, 21))