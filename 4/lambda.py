import math

a = lambda x: x * x
b = lambda x, y: y - math.sqrt(x)


print(a(4))
print(b(2, 4))
print(b(4, 2))

