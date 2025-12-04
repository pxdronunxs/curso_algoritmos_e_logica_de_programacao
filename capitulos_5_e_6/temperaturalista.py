L = [-10, -8, 0, 1, 2, 5, -2, -4]

# menor temperatura
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(f"\nA temperatura mínima é igual a: {minimo}")

# maior temperatura
maximo = L[0]
for e in L:
    if e > maximo:
        maximo = e
print(f"\nA temperatura máxima é igual a: {maximo}")

# temperatura média
media = 0
for e in L:
    media += e
media = media / (len(L))
print(f"\nA temperatura média é igual a: {media:.2f}")

