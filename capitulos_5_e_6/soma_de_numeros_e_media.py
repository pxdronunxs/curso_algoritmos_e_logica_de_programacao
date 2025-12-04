contador = 0
soma = 0
media = 0
valores = 1

while valores > 0:
    if valores == 0:
        break
    valores = int(input("Informe os valores a serem somados: "))
    soma = soma + valores
    contador = contador + 1

media = soma / contador
print(f"\nQuantidade de números digitados: {contador}")
print(f"Soma dos valores digitados: {soma}")
print(f"Média dos valores: {media}")
