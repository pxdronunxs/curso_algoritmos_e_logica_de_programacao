a = float(input("Informe o valor da mercadoria: "))
b = float(input("Informe o percentual de desconto: "))
desconto = (a * b) / 100
print(f"O valor do desconto é de: {desconto}")
preço_a_pagar = a - desconto
print(f"Valor a ser pago: {preço_a_pagar}")
