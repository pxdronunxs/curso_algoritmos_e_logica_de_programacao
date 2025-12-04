L = []
while True:
    n = int(input("Digite um numero (0 para sair): "))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1
