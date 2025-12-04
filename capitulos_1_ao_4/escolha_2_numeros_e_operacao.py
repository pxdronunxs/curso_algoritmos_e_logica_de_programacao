print("[1] ADIÇÃO")
print("[2] SUBTRAÇÃO")
print("[3] DIVISÃO")
print("[4] MULTIPLICAÇÃO")


a = float(input ("Escolha uma operação: "))

if a == 1:
    print("Você escolheu ADIÇÃO")
    a = 1
elif a == 2:
    print("Você escolheu SUBTRAÇÃO")
    a = 2
elif a == 3:
    print("Você escolheu DIVISÃO")
    a = 3
else:
    print("Você escolheu MULTIPLICAÇÃO")
    a = 4

b = float(input("Digite o primeiro número: "))
c = float(input("Digite o segundo número: "))

if a == 1:
    result = b + c
    print(f"A soma entre os dois valores é igual a: {result}")
elif a == 2:
    result = b - c
    print(print(f"A subtração entre os dois valores é igual a: {result}"))
elif a == 3:
    result = b / c
    print(f"A divisão entre os dois valores é igual a: {result}")
else:
    result = b * c
    print(f"A multiplicação entre os dois valores é igual a: {result}")

