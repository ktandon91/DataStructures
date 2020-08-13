class ListIterator:
    children = []

    def __init__(self, value):
        self._value = value
        self.children.append(value)

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return str(self._value)

a = [1,2,3,4,5]

for i in a:
    list_iterator = ListIterator(i)

for element in list_iterator:
    print(list_iterator)

#TODO list of all elements