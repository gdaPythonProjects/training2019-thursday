import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def print_result(result):
    if result:
        print("LICZBA PIERWSZA")
    else:
        print("LICZBA ZŁOŻONA")


t = int(input("Podaj liczbę przypadków"))
while t:
    x = int(input("Podaj liczbę do sprawdzenia"))
    result = is_prime(x)
    print_result(result)
    t -= 1
