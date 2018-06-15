class Reverse:
    def __init__(self, ele):
        self.data = ele
        self.index = len(self.data)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


myRev = Reverse([1,2,3])
print(next(myRev))
print(next(myRev))
print(next(myRev))
print(next(myRev))






