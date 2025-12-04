divida = float(input("Digite o valor inicial da dívida: R$"))
juros = float(input("Informe a taxa de juro mensal: "))
pagamento = float(input("Quanto deseja pagar por mês: R$"))

mes = 0
total_pago = 0
total_juros = 0


while divida > 0:
    juros_mes = divida * (juros / 100)
    divida = divida + juros_mes
    total_juros = total_juros + juros_mes

    if pagamento > divida:
        pagamento = divida
    divida = divida - pagamento

    total_pago = total_pago + pagamento
    mes = mes + 1

print(f"\nNúmero de meses para pagar a dívida: {mes}")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pago: R$ {total_juros:.2f}")


