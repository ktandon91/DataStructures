class MyClass:
    def __init__(self,ele):
        self._x=ele

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,ele):
        if self._x < ele:
            self._x = ele


myObj = MyClass(5)
print(myObj.x)
myObj.x = 24
print(myObj.x)
myObj.x = 7
print(myObj.x)