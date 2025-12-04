# pesquisa sequincial

L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))

# procurando o primeiro valor (p)
x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} foi encontrado na posição {x}")
        break
    x += 1
else:

    print(f"{p} não foi encontrado!")

# procurando o segundo valor (v)
y = 0
while y < len(L):
    if L[y] == v:
        print(f"{v} foi encontrado na posição {y}")
        break
    y += 1
else:
    print(f"{v} não foi encontrado!")

