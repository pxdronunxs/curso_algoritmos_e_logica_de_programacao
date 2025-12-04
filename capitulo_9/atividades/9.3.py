with open("impares.txt", "w") as impares:
    with open("pares.txt", "w") as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")


with open("impares.txt") as impares, open("pares.txt") as pares, open("imparesepares.txt", "w") as imparesepares:
                    for impar, par in zip(impares, pares):
                           imparesepares.write(par)
                           imparesepares.write(impar)
                           
                        