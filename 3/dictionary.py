x = {
    "kot": ["Stefan", "Bubuś"],
    "pies": {"rasa": "pitbull",
             "name": "puszek"},
    "rybka": "Złota"
}

print(x["kot"])
print(x.get("nie istnieje", []))
print(x.get("kot"))
print(x.get(":("))
if "rybka" in x:
    del x["rybka"]

for i, j in x.items():
    print(i, j)

for i in x.keys():
    print(i)

for i in x.values():
    print(i)
