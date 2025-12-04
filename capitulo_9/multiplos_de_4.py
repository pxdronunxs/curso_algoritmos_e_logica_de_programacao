with open("multiplos de 4.txt", "w") as multiplos4:
    with open("capitulo9\pares.txt") as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos4.write(linha)