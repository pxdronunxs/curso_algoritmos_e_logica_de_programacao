juros = 0
mes = 1


deposito_inicial = float(input("Digite o valor do depósito inicial: "))
deposito_mensal = float(input("Digite o valor a ser depositado mensalmente: "))
taxa_de_juros = float(input("Digite a taxa de juros: "))


while mes <= 24:
    juros = ((deposito_inicial * taxa_de_juros) / 100) + deposito_mensal
    print(f"Mês {mes} rendeu: R$ {juros:.2f}")
    total_juros = juros + deposito_inicial
    deposito_inicial = deposito_inicial + juros + deposito_mensal
    mes = mes + 1
print(f"O total acumulado do juros foi de: R$ {total_juros:.2f}")
