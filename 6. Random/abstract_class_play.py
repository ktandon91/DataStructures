from abc import ABC, abstractclassmethod

class MyClass(ABC):
    @abstractclassmethod
    def print_num(self):
        pass

    def you_hoo(self):
        print("youhoo")


myObj = MyClass()