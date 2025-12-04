with open("texto.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    ocorrencias = {}
    for palavra in palavras:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1

with open("ocorrencias_de_palavras.txt", "w", encoding="utf-8") as novo:
                for palavra, quantidade in ocorrencias.items():
                      novo.write(f"{palavra}: {quantidade}\n")
                      