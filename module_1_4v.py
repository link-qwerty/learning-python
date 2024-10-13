# Variant with input

# Init
quantity_of_exes = 12
hours_spent = 1.5
course_name = 'Python'

# Code
quantity_of_exes = input('Введите количество выполненных заданий:')
hours_spent = input('Введите количество затраченных часов:')

print('Курс:', course_name, '| Выполнено работ:', quantity_of_exes, '| Потрачено часов:', hours_spent, '| Среднее время выполнения задания, час:', float(hours_spent)/int(quantity_of_exes))