x = int(input("Podaj liczbę\n"))
z = True
if x == 1:
    z = False
else:
    for i in range(2,x):
        z = True
        if x % i == 0:
            z = False
            break


if z:
    print(x, "jest liczbą pierwszą")
else:
    print(x, "nie jest liczbą pierwszą")