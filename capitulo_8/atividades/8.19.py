# [x for x in range(2, 100) if all(x % i != 0 for i in range(2, x))]

def gerador_primos(n):
    primos = []
    for x in range(2, n):
        if all(x % i != 0 for i in range(2, x)):
            primos.append(x)
    return primos

print(gerador_primos(101))