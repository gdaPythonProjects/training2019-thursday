def check_name(name, names):
    if name in names:
        print(name, " Obecny!")
    else:
        print(name, " Nie ma!")


t = int(input("t cases...\n"))
names = []

while t:
    names.append(input("Podaj imię: "))
    t -= 1

check_name("Andrzej", names)
