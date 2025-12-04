
L = [10, 20, 25, 30]

def pesquisa(lista, valor):
    posicao = 0
    for elemento in lista:
        if elemento == valor:
            return f"{valor} encontrado na posição {posicao}"
        posicao += 1
    return f"{valor} não encontrado"

print(pesquisa(L, 20))
print(pesquisa(L, 50))
