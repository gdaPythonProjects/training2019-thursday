from itertools import zip_longest

pets = ["Dog", "Cat", "Turtle"]
name = ["Bazyli", "Stefan", "Tuptuś"]
colors = ["Black", "Black"]

print(list(zip(pets, name)))
print(list(zip(pets, name, colors)))
print(list(zip_longest(pets, name, colors)))

