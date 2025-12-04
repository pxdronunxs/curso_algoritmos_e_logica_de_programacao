a = float(input("Qual o valor do salário? "))
novo_salario = 0
if a > 1250:
    novo_salario = a + (a * 10) / 100
if a <= 1250:
    novo_salario = a + (a * 15) / 100
print(f"O novo salário será de: R$ {novo_salario:.2f}.")
