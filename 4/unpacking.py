def add_values(x, y):
    print(x + y)


add_values(3, 2)

tuple_values = (2, 4)
add_values(*tuple_values)
list_values = [2, 7]
add_values(*list_values)

dictionary_values = {'x': 1, 'y': 9}
add_values(**dictionary_values)


def printer(*lst):
    for i in lst:
        print(i)


x = ["1", "2", "3"]
printer(x)
