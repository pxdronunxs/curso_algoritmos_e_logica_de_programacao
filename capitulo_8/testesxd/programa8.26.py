# imprimindo uma lista de inteiros com multiplos niveis (de espaços)

def imprime_listas(lista, nivel=0):
    for x in lista:
        if isinstance(x, int):
            print(f"{x:{nivel * 2}}")
        else:
            imprime_listas(x, nivel + 1)

imprime_listas([1, [2, 3, 4], [5, 6, [7, 8, 9]], 10])