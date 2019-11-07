even = 0
odd = 0
for i in range(101):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print("Suma parzystych: ", even)
print("Suma NIE parzystych: ", odd)
