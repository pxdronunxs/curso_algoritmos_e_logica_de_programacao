fim = int(input("Digite o limite de onde os números pares devem ser impressos: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1
