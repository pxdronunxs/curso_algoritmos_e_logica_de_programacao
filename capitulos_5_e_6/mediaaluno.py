notas = 0
cont = 0

while True:
    x = float(input("Informe as notas do aluno, (0) para mostrar a média."))
    if x == 0:
        break
    notas += x
    cont += 1

media = notas / cont

print(f"\nA média do aluno é igual a: {media:.2f}")




