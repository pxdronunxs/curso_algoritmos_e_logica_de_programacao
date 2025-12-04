import sys

if len(sys.argv) != 4:
    print("uso correto = python 9.4.py arquivo1 arquivo2 arquivo_saida")
    sys.exit(1)

arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]
arquivo_saida = sys.argv[3]

try:
    with open(arquivo1, "r", encoding='utf-8') as a1:
        conteudo1 = a1.readlines()

    with open(arquivo2, "r", encoding='utf-8') as a2:
        conteudo2 = a2.readlines()

    with open(arquivo_saida, "w", encoding='utf-8') as a_saida:
        a_saida.writelines(conteudo1)
        a_saida.writelines(conteudo2)

    print(f"combinados com sucesso em '{arquivo_saida}'.")

except FileNotFoundError as e:
    print(f"Erro: {e.filename} não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

