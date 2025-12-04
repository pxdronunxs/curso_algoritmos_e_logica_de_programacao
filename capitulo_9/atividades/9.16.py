agenda = []


def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    print(f"Nome: {nome} | Telefone: {telefone}")


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def apaga():
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("------\n")


def grava():
    nome_arquivo = "lista_telefonica.txt"  # usa nome fixo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
    print(f"Agenda salva em '{nome_arquivo}' com sucesso!")


def lê():
    global agenda
    nome_arquivo = "lista_telefonica.txt"
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = []
            for linha in arquivo:
                linha = linha.strip()
                if "#" in linha:  # só divide se a linha estiver correta
                    nome, telefone = linha.split("#")
                    agenda.append([nome, telefone])
        print(f"Agenda carregada de '{nome_arquivo}' com sucesso!")
    except FileNotFoundError:
        print(
            f"Arquivo '{nome_arquivo}' não encontrado. Começando agenda vazia.")


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
            else:
                print(f"Valor inválido, favor digitar entre {inicio} e {fim}")
        except ValueError:
            print("Por favor, digite um número válido.")


def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
0 - Sai
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


# Loop principal
while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
