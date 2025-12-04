def validacao(frase, minimo, maximo):
    while True:
        string = str(input(frase))
        if len(string) > maximo or len(string) < minimo:
            print(f"Digite palavras com caracteres entre {minimo} e {maximo}")
        else:
            print("OK")
            break

validacao("Digite um texto: ", 1, 2)
