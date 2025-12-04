# import sys

# params = sys.argv[1:]
# print(f"Número de parâmetros: {len(params)}")
# for n, p in enumerate(params, start=1):
#     print(f"Parâmetro {n} = {p}")


import sys

# Verifica se o usuário passou o nome do arquivo
if len(sys.argv) < 2:
    print("Uso: python le_arquivo.py <nome_do_arquivo>")
    sys.exit(1)  # Encerra o programa com código de erro

# O nome do arquivo é o segundo argumento (índice 1)
nome_arquivo = sys.argv[1]

try:
    # Abre o arquivo no modo de leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Lê e imprime cada linha
        for linha in arquivo:
            print(linha, end='')  # 'end' evita linhas em branco extras
except FileNotFoundError:
    print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")