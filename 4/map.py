from math import sqrt


def int_sqrt(value):
    return int(sqrt(value))


numbers = [1, 7, 14, 21]
results = []
for i in numbers:
    results.append(int_sqrt(i))
print(results)

x = [int_sqrt(i) for i in numbers]
print(x)

print(list(map(int_sqrt, numbers)))
