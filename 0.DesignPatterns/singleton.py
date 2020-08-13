class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance



class Singleton2(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            
        return cls._instances[cls]



class MyClass(metaclass=Singleton2):
    pass



s1 = Singleton()
s2 = Singleton()

print(s1 == s2)

S1 = MyClass()
S2 = MyClass()

print(S1 == S2)


