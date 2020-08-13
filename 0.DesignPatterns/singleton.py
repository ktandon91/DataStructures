class Sample(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


# class Singleton2(type):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance

# class Sample()
#     def __int__(cls, name, bases, attrs, **kwargs):
#         print("__init__")
#         super().__init__(name, bases, attrs)
#         cls._instance = None
#
#     def __call__(cls, *args, **kwargs):
#         print("__call__")
#         if cls._instance is None:
#             cls._instance = super().__call__(*args, **kwargs)
#         return cls._instance
#
#
#
# class MyClass(metaclass=Sample):
#     pass

s1 = Sample()
s2 = Sample()

print(s1 == s2)



