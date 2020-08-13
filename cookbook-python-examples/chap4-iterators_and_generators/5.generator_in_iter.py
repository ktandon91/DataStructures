class GeneratorFromIterator:

    children=[]

    def __init__(self,a):
        self.children.append(a)
        self.index = -1

    def __iter__(self):
        while self.index < len(self.children) - 1:
            self.index += 1
            yield self.children[self.index]

for i in range(10):
    obj = GeneratorFromIterator(i)

for element in obj:
    print(element)
