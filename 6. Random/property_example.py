class MyClass:
    def __init__(self):
        self.a = 1

    def b(self):
        print("b is here")

    @property
    def c(self):
        return "c is here"

myObj = MyClass()

print(myObj.a)
print(myObj.b)
print(myObj.c)