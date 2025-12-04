largura = 79
with open("C:/Users/Pedro Nunes/Desktop/atividades livro/capitulo9/atividades/entrada.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(largura))
        elif linha[0] == "*":
            print(linha[1:].center(largura))
        elif linha[0] == "=":
            print("=" * 40)
        else:
            print(linha)