# Defines

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return inner_function

# Code
test_function() # normal call
#inner_function() # abnormal call, got error
inner_function = test_function() # works! but seems ugly