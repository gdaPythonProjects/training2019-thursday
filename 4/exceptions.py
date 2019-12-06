dictionary = {"dog": "Bazyli"}

try:
    del dictionary["dog"]
    print("Coś tam robię po usunięciu kota")
except KeyError:
    print("Nie ma takiego klucza!")
except NameError:
    print("Nie ma takiej zmiennej")
else:
    print("Super! Wszystko w bloku try zadziałało")
finally:
    print("Mimo wszystko robię rzeczy")

x = input("Podaj liczbę")
if not x.isdigit():
    raise TypeError("Miała być cyfra cymbale!")
