import abc
from abc import ABC, abstractclassmethod, ABCMeta

class MyClass(ABC):
    # @classmethod
    @abc.abstractmethod
    def print_num(self):
        print('hi')

    def you_hoo(self):
        print("youhoo")

class SubMyClass(MyClass):
    pass

myObj = SubMyClass().print_num()