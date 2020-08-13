

def decorator_func(function, a='abc'):
    def inner_function():
        print(a)
        function()
    return inner_function

@decorator_func
def greet_me():
    return "hi"

print(greet_me())