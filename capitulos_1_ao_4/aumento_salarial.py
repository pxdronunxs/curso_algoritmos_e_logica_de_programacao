a = float(input("Informe o salário atual: "))
b = float(input("Informe a porcentagem de do ajuste: "))
aumento = ((a * b) / 100)
print(f"O valor do ajuste é de: {aumento}")
novo_salario = a + aumento
print(f"O seu novo salário é de: {novo_salario}")
