# exemplo sem usar

# soma = 0.0
# valor = input("Digite fim para terminar ou um numero para somar: ")
# while valor != "fim":
#     soma += float(valor)
#     valor = input("Digite fim para terminar ou um numero para somar: ")
# print(f"A soma é: {soma}")

#======================================================#

soma = 0.0
while (valor := input("Digite fim para terminar ou um numero para somar: ")) != "fim":
    soma += float(valor)
print(f"A soma é: {soma}")