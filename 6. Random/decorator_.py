from functools import wraps

def decorate_name(func):
    @wraps(func)
    def wrapper_function(*args,**kwargs):
        return "Inside wrapper {} ".format(func(*args,**kwargs))
    return wrapper_function

@decorate_name
def function1(first_name, last_name="Tandon"):
    """
    This is the docstring of function 1
    :param first_name:
    :param last_name:
    :return: formatted name
    """
    return "I am {0} {1}".format(first_name, last_name)


print(function1("Karan"), function1.__name__, function1.__doc__)