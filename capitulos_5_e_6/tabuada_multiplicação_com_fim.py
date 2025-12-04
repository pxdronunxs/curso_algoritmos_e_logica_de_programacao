# tabuada multiplicação com fim
multiplicando = int(input("Escolha o multiplicando: "))
inicio = int(input("Digite o primeiro multiplicador: "))
fim = int(input("Digite o último multiplicador: "))

while inicio <= fim:
    resultado = multiplicando * inicio
    print(f"{inicio} x {multiplicando} = {resultado}")
    inicio = inicio + 1
