t = 5
sentences = []
while t:
    sentences.append(input("Dej jakieś zdanie: ")+"\n")
    t -= 1

f = open("sentences.txt", "w")
for i in sentences:
    f.write(i)
f.close()

f = open("sentences.txt", "a")
f.writelines(sentences)
f.close()

f = open("sentences.txt", "r")
for i in sentences:
    print(f.readline(), end="")
f.close()

f = open("sentences.txt", "r")
print(f.readlines())
f.close()

with open("sentences.txt", "r") as f:
    print(f.readlines())
