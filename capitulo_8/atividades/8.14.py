while tentativas > 0:
    x = int(input("Escolha um numero entre 1 e 20: "))

    if x == n:
        print("Voce acertou!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Voce errou. Restam {tentativas} tentativas.")
        else:
            print("Voce perdeu as 3 tentativas!")
            print(f"O numero correto era {n}.")
