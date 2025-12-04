import sys

if len(sys.argv) != 4:
    print("Uso: python nomeprograma.py <arquivo> <linha_inicial> <linha_final>")
    sys.exit(1)

arquivo = sys.argv[1]
linha_inicial = int(sys.argv[2])
linha_final = int(sys.argv[3])

with open(arquivo, "r", encoding="utf-8") as original:
    conteudo = original.readlines()

for linha_texto in conteudo[linha_inicial-1:linha_final]:
    print(linha_texto, end="")

