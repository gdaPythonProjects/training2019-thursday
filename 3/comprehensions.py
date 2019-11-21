ip = "10.102.45.13"
x = ip.split(".")
print(x)

y = []
for i in x:
    y.append(int(i))
print(y)

z = [int(i) for i in x]
print(z)

a = [int(i) for i in x if int(i) % 2 == 0]
print(a)

print(z[1:2])
print(z[1::])
print(z[:2])
print(z[::1])
print(z[::-1])
