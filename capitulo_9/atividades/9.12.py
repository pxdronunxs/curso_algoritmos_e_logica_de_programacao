# with open("texto_formatado.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()
#     ocorrencias = {}
#     for numero_linha, linha in enumerate(linhas, start=1):
#         palavras = linha.split()
#     conteudo = arquivo.read()

#     posicao = 0    
#     for palavra in palavras:
#         coluna = linha.find(palavra, posicao) + 1
#         posicao = coluna + len(palavra)

#         if palavra not in ocorrencias:
#             ocorrencias[palavra] = []
#         ocorrencias[palavra].append((numero_linha, coluna))


# with open("texto_formatado.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# ocorrencias = {}

# for numero_linha, linha in enumerate(linhas, start=1):
#     palavras = linha.split()
#     posicao = 0  # zera a posição no início de cada linha

#     for palavra in palavras:
#         coluna = linha.find(palavra, posicao) + 1  # +1 para não começar no 0
#         posicao = coluna + len(palavra)

#         palavra_limpa = palavra.strip(".,!?;:()[]{}").lower()

#         if palavra_limpa not in ocorrencias:
#             ocorrencias[palavra_limpa] = []
#         ocorrencias[palavra_limpa].append((numero_linha, coluna))


with open("texto_formatado.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

ocorrencias = {}

for numero_linha, linha in enumerate(linhas, start=1):
    palavras = linha.split()
    posicao = 0  

    for palavra in palavras:
        coluna = linha.find(palavra, posicao) + 1  
        posicao = coluna + len(palavra)

        palavra_limpa = palavra.strip(".,!?;:()[]{}").lower()

        if palavra_limpa not in ocorrencias:
            ocorrencias[palavra_limpa] = []
        ocorrencias[palavra_limpa].append((numero_linha, coluna))

with open("ocorrencias_de_palavras_com_linhas_e_colunas.txt", "w", encoding="utf-8") as novo:
    for palavra, posicoes in ocorrencias.items():
        novo.write(f"{palavra}:\n")
        for linha, coluna in posicoes:
            novo.write(f"    linha {linha}, coluna {coluna}\n")
        novo.write("\n")  