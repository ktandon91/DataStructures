def abc(n):
    while n > 0:
        yield n
        n-=1

a = iter(abc(3))

for i in a:
    print(i)
