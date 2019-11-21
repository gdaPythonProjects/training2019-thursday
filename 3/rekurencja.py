def fun(n):
    if n == 0:
        return 1
    else:
        return n * fun(n - 1)


print(fun(5))
print(fun(4))
