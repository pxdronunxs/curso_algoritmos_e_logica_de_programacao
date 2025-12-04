import sys

if len(sys.argv) != 4:
    print("Uso: python formatador.py <arquivo> <largura_linha> <linhas_pagina>")
    sys.exit(1)

nome_arquivo = sys.argv[1]
largura_linha = int(sys.argv[2])
linhas_pagina = int(sys.argv[3])

with open(nome_arquivo, "r", encoding="utf-8") as texto:
    conteudo = texto.read()
    palavras = conteudo.split()

linha_atual = ""
contador_linhas = 0
numero_pagina = 1

with open("texto_formatado.txt", "w", encoding="utf-8") as texto_formatado:
    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 <= largura_linha:
            linha_atual += palavra + " "
        else:
            texto_formatado.write(linha_atual.strip() + "\n")
            contador_linhas += 1

            if contador_linhas == linhas_pagina:
                texto_formatado.write(f"\n--- Página {numero_pagina} - {nome_arquivo} ---\n\n")
                numero_pagina += 1
                contador_linhas = 0

            linha_atual = palavra + " "

    if linha_atual:
        texto_formatado.write(linha_atual.strip() + "\n")
        contador_linhas += 1

    if contador_linhas > 0:
        texto_formatado.write(f"\n--- Página {numero_pagina} - {nome_arquivo} ---\n")