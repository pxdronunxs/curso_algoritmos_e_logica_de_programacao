def validacao(frase, vogais=["a", "e", "i", "o", "u"]):
    while True:
        string = input(frase).lower().strip()

        if string == "sair":
            print("Encerrando o programa...")
            break

        tem_vogal = False
        for letra in string:
            if letra in vogais:
                tem_vogal = True
                break

        if tem_vogal:
            print("O texto possui vogais")
        else:
            print("O texto não possui vogais")

validacao("Digite um texto: ")
