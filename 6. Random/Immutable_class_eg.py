class ImmutableClass:
    __slots__= 'a','b','c'

    def __init__(self):
        self.a=1
        self.b=2
        self.c=3

    def __setattr__(self, key, value):
        raise ValueError


immObj= ImmutableClass()

d1={}
d1[immObj]=1

print(d1[immObj])

immObj.a=56
print(immObj.a)