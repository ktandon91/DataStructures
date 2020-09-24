class X:
    def __init__(self, val):
        self.children = list(range(1,val+1))


    def __iter__(self):
        iter(self.children)

    def __next__(self):
        while self.children:
            c = self.children.pop()
            return c

x = X(3)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

