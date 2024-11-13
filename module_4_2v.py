# Defines
def test_function(x):
    a = x ** 2
    def inner_function(x):
        b = a + x
        return b
    print(f'Вывод результата работы функции test_function: {a}')
    print(f'Вывод результата работы функции inner_function из test_function: {inner_function(x)}')
    return inner_function

# Code
test_function(2) # normal call a = (2 ** 2) + 2
inner_function = test_function(0) # copy id of inner function from return statement
print(f'Вывод результата работы функции inner_function из глобального пространства: {inner_function(4)}')
print(f'Пространства имен: {test_function} и {inner_function}')
"""
При копировании id вложенного объекта из локального пространства имен в стеке создаются как вложеннная
так и локальная функции. Помимо того в процессе возврата id внутренней функции код локальной функции так же выполняется.
Если мы выполним операцию присваивания без вызова test_function, то никакого возврата внутреннего объекта не произойдет.
У нас просто будет два имени, ссылающихся на один id (test_function).
"""

###

# let's try something else
a = 2           #1st operand
b = 5           #2nd operand
print(id(a))    #id of 1st operand
print(id(b))    #id of 2nd operand
print('=' * 10)
b = a           #assignment operation
print(id(a))    #id of 1st operand d'not change (expected)
print(id(b))    #id of 1nd operand copied into id 2nd operand (poor little b-object was killed by garbage collector
# Dr.Plague -  now we have two variables reffered on the same object)
print('=' * 10)
b = a + 5       #assigment operation with expression on the right
print(id(a))    #id of 1st operand d'not change
print(id(b))    #id of 2nd operand seems changed (that object was deleted and we got new with same name and with value
# of expression result - now we have two objects with different names)
print('=' * 10)
print(id(a))    #verification! and there is!
print('=' * 10)
a = a + 5       #assigment operation with expression on the right
print(id(a))    #id of 1st operand seems changed (that object was deleted and now we got new with same name and with
# value of expression result)
print(id(b))    #id of 2nd operand do not changed... wait! what?! after calculating the expression for the 1st operand,
# we will have the same identifiers for both of them
print(a)        #hmm.. we have 7
print(b)        #and there
# i remember something. python store values for base int type objects in some struct (set as i remember) and we reffer
# on elements in that struct. if we do this way...
a = 2.45
b = 5.36
b = a
b = a + 95.46
a = a + 10.45
b = 12.899999999999999
print(id(a))
print(id(b))
print(a)
print(b)
# yes. now everything is correct.

"""
let's make a conclusion. the id is not equal to the address link in c-plus-plus. this is not a "place in memory".
it's just a resource identifier in python's internal structures. and we need to be very careful about using ID 
comparisons for some of the "dirty tricks" that c-plus-plus users like to use.
"""