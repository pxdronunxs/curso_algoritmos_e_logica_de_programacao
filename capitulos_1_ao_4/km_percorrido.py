km = float(input("Informe a quilometragem percorrida: "))
dias = int(input("Informe a quantidade de dias alugados: "))

preco_km = km * 0.15
preco_dia = dias * 60
total = preco_km + preco_dia

print(f"O valor total do aluguel é R$ {total:.2f}")


