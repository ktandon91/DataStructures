from itertools import zip_longest

a = [1,2,3,4,5]
b = ["one", "two"]
    
c = zip_longest(a,b)

for i in c:
    print(i)