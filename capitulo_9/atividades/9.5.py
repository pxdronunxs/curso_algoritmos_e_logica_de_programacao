with open("pares.txt", "r", encoding="utf-8") as arquivo:
    lista_pares = [int(linha.strip()) for linha in arquivo]
lista_invertida = lista_pares[::-1]
with open("C:/Users/Pedro Nunes/Desktop/atividades livro/capitulo9/atividades/pares_invertidos.txt", "w", encoding="utf-8") as novo_arquivo:
    for numero in lista_invertida:
        novo_arquivo.write(f"{numero}\n")