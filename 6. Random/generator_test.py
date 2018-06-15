def num_print(n):
    i = 0
    try:
        while i < n:
            yield i
            i +=1
    except StopIteration:
        print("end here")


f = num_print(4)

for i in f:
    print(i)

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

