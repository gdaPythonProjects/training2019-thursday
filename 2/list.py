text = "cokolwiek"
list_text = list(text)
print(list_text)
names = ["Ala", "Andrzej", "Zygmunt"]

for i, j in enumerate(names):
    print(i, j)

names.append("Zbigniew")
names.remove("Andrzej")

for i in names:
    print(i)


if "Andrzej" in names:
    print("Jest z nami Andrzej! :)")
else:
    print("Kogo z nami nie ma? Andrzeja!")
