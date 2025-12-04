valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o seu salário: R$ "))
anos = int(input("Digite a quantidade de anos para pagar: "))

meses = anos * 12
prestacao = valor_casa / meses

limite = salario * 0.30

print(f"Valor da prestação: R$ {prestacao:.2f}")
print(f"Limite permitido: R$ {limite:.2f}")

if prestacao <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")
