def tribonacci(signature, n):
    a = signature[0]
    b = signature[1]
    c = signature[2]
    e = []
    for i in range(n):
        if i < 3:
            e.append(signature[i])
        else:
            d = a+b+c
            e.append(d)
            a = b
            b = c
            c = d
    return e