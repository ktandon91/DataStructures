class ListIterator:
    children = []

    def __init__(self, value):
        self._value = value
        self.children.append(value)
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i+=1
        if self.i >= 5:
            raise StopIteration
        return self.children[self.i]

    def __repr__(self):
        if self.i < 0:
            return "ListIterator with elements {}".format(str(self.children))
        return str(self.children[self.i])

a = [1,2,3,4,5]

for i in a:
    list_iterator = ListIterator(i)

for element in list_iterator:
    print(list_iterator)

#TODO list of all elements