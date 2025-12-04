lista = []

while True:
    nome_arquivos = input("Digite o nome do arquivo (ou 'fim' para encerrar): ")
    if nome_arquivos.lower() == "fim":
        break
    else:
        lista.append(nome_arquivos)

print("\nArquivos digitados:")
for nome in lista:
    print(nome)