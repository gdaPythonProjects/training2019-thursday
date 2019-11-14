import math

x = int(input("Podaj liczbę\n"))
prime = 1
if x:
    prime = 0
else:
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            prime = 0
            break

if prime == 1:
    print("PRIME")
else:
    print("NOT PRIME")
