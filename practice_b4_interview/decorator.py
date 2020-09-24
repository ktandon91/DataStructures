def outer(func):
    def inner(*args):
        print(func)
        print(*args)
    return inner

@outer
def number(a=7):
    pass

number(8)


def outer_element(a):
    def inner_element(b):
        return a*b
    return inner_element

a_var = outer_element(5)
b = a_var(3)

print(b)