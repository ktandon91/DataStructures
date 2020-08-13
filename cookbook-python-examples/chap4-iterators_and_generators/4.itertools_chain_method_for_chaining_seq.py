from itertools import chain

a = [1,2,3,4]
b = ['x', 'y']
c= chain(a,b)


for i in c:
    print(i)