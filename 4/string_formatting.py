a, b = 4, 7
s = a + b

print("Suma ", a, " + ", b, " = ", s)
print("Suma " + str(a) + " + " + str(b) + " = " + str(s))

# Klasyczny
print("Suma %d + %d = %d" % (a, b, s))
print("Suma %(value_a)d + %(value_b)d = %(value_s)d"
      % {"value_a": a, "value_b": b, "value_s": s})

# New style
print("Suma {} + {} = {}".format(a, b, s))
print("Suma {value_a} + {value_b} = {suma}".
      format(value_a=a, value_b=b, suma=s))

# f-string
#print(f"Suma {a} + {b} = {s}")

x = ["Romek", "Tomek", "Atomek"]
print(" ".join(x))
print(" ".join(x), end=".")

