a = float(input("Qual a velocidade atingida: "))
b = a - 80
b = b * 5
if a > 80:
    print("Você foi multado!")
    print(f"Deverá pagar o valor total de: R$ {b} ")
if a < 80:
    print("Você não foi multado. Pode seguir seu caminho")
