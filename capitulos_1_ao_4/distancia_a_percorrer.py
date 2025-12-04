a = float(input("Qual a distância a percorrer? "))
passagem = 0
if a <= 200:
    passagem = a * 0.50
    print(f"Sua passagem será de: R${passagem}")
else:
    passagem = a * 0.45
    print(f"Sua passagem será de: R${passagem}")


