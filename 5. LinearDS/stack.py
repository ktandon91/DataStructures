class Stack:
    def __init__(self):
        self.items=[]

    def push(self,ele):
        self.items.append(ele)

    def pop(self):
        return self.items.pop()

    def peek(self):
        """To check last element of the stack."""
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


