class Complex:
    def __init__(self, a, b):
        self.r=a
        self.i=b

    def __add__(self, other):
        self.i = self.i + other.i
        self.r = self.r + other.r
        return self

    def __str__(self):
        return "{} + {}i".format(self.r, self.i)



c1 = Complex(2,3)
c2 = Complex(4,5)
c3 = Complex(4,5)
c4 = c1+c2+c3
print(c4)