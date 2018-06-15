class BaseA:
    def __init__(self):
        self.a = 1

    def basea_function1(self):
        return "In function1 of base A"


class SubA(BaseA):
    def __init__(self):
        pass

    def basea_function1(self):
        return super().basea_function1()

objSubA=SubA()

print(objSubA.a)
print(objSubA.basea_function1())

