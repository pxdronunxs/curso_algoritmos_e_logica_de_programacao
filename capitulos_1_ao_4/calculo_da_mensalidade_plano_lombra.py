plano = input("Qual é o seu plano de celular? ")
if plano == "lombrapouca":
    mins_no_plano = 100
    extra = 0.20
    preço = 50
else:
    mins_no_plano = 500
    extra = 0.15
    preço = 99
if plano != "lombrapouca" and plano != "lombramuita":
    print("Não conheço esse plano")
else:
    mins_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar: ")
    print(f"Preço do plano R${preço:10.2f}")
    suplemento = 0
    if mins_consumidos > mins_no_plano:
        suplemento = extra * (mins_consumidos - mins_no_plano)
    print(f"Suplemento     R${suplemento:10.2f}")
    print(f"Total          R${preço + suplemento:10.2f}")
