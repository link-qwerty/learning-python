# Init
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # grades list
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # students set
average = dict() # empty dict for average grade

# Code
for key in list(sorted(students)): # iterate sorted collection
    average[key] = sum(grades[0])/len(grades.pop(0)) # sum all values in grades[0] than dev on count of values than pop first element from list grades and repeat

# Result
print(average)
