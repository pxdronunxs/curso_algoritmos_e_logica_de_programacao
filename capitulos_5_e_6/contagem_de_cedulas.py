valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 10000
apagar = int(valor * 100)

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas > 0:
            print(f"{cedulas} cédula(s)/moeda(s) de R${atual/100:.2f}")
        if apagar == 0:
            break
        if atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0

