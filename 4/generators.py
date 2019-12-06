def multiply_two(lst):
    for num in lst:
        yield num * 2


numbers = [1, 2, 8, 4]
results = multiply_two(numbers)
print(next(results))
print("Coś innego")
print(next(results))
print(next(results))
print(next(results))

results = multiply_two(numbers)
print(list(results))

results = multiply_two(numbers)
for i in results:
    print(i)
