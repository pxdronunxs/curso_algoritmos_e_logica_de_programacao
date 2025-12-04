valores = list(range(1, 100))
pares = []
impares = []

for e in valores:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)

print("Pares: ", pares)
print("\nImpares: ", impares)

