t = int(input("Podaj liczbę przypadków (wyrazów sumy): \n"))
s = 0
for i in range(t):
    x = int(input("podaj wyraz sumy:\n"))
    s = s + x
print("Suma ",t," wyrazów wynosi: ",s)
