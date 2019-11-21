import sys


def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(fib(5))
print(fib(4))
#print(fib(1400))
