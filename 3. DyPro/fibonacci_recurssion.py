def fib_rec(n):
    if n==1 or n < 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(4))