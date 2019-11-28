def is_odd(value):
    return value % 2

numbers = [1, 5, 3, 6, 2, 6, 2, 5, 2, 8]
x = list(filter(is_odd, numbers))
print(x)

