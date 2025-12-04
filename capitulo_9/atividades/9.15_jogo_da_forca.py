import random
import os
import time


def formatar_tempo(segundos):
    minutos = int(segundos // 60)
    segundos = int(segundos % 60)
    return f"{minutos:02d}:{segundos:02d}"


def limpar_arquivo_palavras():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]

        palavras = sorted(set(palavras))

        with open("palavras.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(palavras))
    except FileNotFoundError:
        pass


def adicionar_palavra():
    nova_palavra = input("Digite a nova palavra: ").strip().lower()
    try:
        with open("palavras.txt", "r", encoding="utf-8") as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]

        if nova_palavra in palavras:
            print("Essa palavra já existe na lista!")
            return False

        with open("palavras.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{nova_palavra}")
        print("Palavra adicionada com sucesso!")
        return True
    except FileNotFoundError:
        with open("palavras.txt", "w", encoding="utf-8") as f:
            f.write(nova_palavra)
        print("Palavra adicionada com sucesso!")
        return True


def atualizar_ranking(jogador, pontos, tempo):
    ranking = []
    try:
        with open("ranking.txt", "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(":")
                nome = partes[0].strip()
                pts = int(partes[1].strip())
                tempo_anterior = float(
                    partes[2].strip()) if len(partes) > 2 else 0
                ranking.append((nome, pts, tempo_anterior))
    except FileNotFoundError:
        pass

    jogador_encontrado = False
    for i, (nome, pts, tempo_anterior) in enumerate(ranking):
        if nome.lower() == jogador.lower():
            # Se o jogador já existe, soma os pontos e atualiza o tempo médio
            novo_tempo = (tempo_anterior * pts + tempo) / (pts + pontos)
            ranking[i] = (jogador, pts + pontos, novo_tempo)
            jogador_encontrado = True
            break

    if not jogador_encontrado:
        ranking.append((jogador, pontos, tempo))

    ranking.sort(key=lambda x: x[1], reverse=True)
    ranking = ranking[:5]

    with open("ranking.txt", "w", encoding="utf-8") as f:
        for nome, pts, tempo_medio in ranking:
            f.write(f"{nome}: {pts}: {tempo_medio}\n")
    return ranking


def verificar_nome_existente(nome):
    try:
        with open("ranking.txt", "r", encoding="utf-8") as f:
            for linha in f:
                nome_existente = linha.split(":")[0].strip()
                if nome_existente.lower() == nome.lower():
                    return True
    except FileNotFoundError:
        pass
    return False


def jogar_forca():
    while True:
        jogador = input("Digite seu nome: ").strip().title()
        if verificar_nome_existente(jogador):
            opcao = input(
                f"Já existe um jogador chamado '{jogador}'. É você mesmo? (S/N): ").strip().upper()
            if opcao == 'N':
                sobrenome = input(
                    "Por favor, digite seu sobrenome também: ").strip().title()
                jogador = f"{jogador} {sobrenome}"
        break

    while True:
        tempo_inicio = time.time()
        try:
            with open("palavras.txt", "r", encoding="utf-8") as f:
                palavras = [linha.strip().lower()
                            for linha in f if linha.strip()]
        except FileNotFoundError:
            print("Arquivo 'palavras.txt' não encontrado!")
            return

        palavra = random.choice(palavras)
        digitadas = []
        acertos = []
        erros = 0

        os.system('cls' if os.name == 'nt' else 'clear')

        desenho = [
            """
        X==:==
        X  :
        X
        X
        X
        X
        ===========
        """,
            """
        X==:==
        X  :
        X  O
        X
        X
        X
        ===========
        """,
            """
        X==:==
        X  :
        X  O
        X  |
        X
        X
        ===========
        """,
            """
        X==:==
        X  :
        X  O
        X \|
        X
        X
        ===========
        """,
            """
        X==:==
        X  :
        X  O
        X \|/
        X
        X
        ===========
        """,
            """
        X==:==
        X  :
        X  O
        X \|/
        X /
        X
        ===========
        """,
            """
        X==:==
        X  :
        X  O
        X \|/
        X / \\
        X
        ===========
        """
        ]

        palavra_acertada = False
        while True:
            senha = ""
            for letra in palavra:
                senha += letra.upper() if letra in acertos else "."
            print(senha)
            print(
                f"\nLetras já tentadas: {', '.join(sorted(x.upper() for x in digitadas))}")

            if senha == palavra.upper():
                print(
                    f"Parabéns, {jogador}! Você acertou a palavra: {palavra.upper()}")
                palavra_acertada = True
                break

            tentativa = input("Digite uma letra: ").lower().strip()

            if tentativa in digitadas:
                print("Você já tentou essa letra!")
                continue
            else:
                digitadas.append(tentativa)
                if tentativa in palavra:
                    acertos.append(tentativa)
                else:
                    erros += 1
                    print("Você errou!")

            print(desenho[erros])

            if erros == 6:
                print("Enforcado! A palavra era:", palavra)
                break

        tempo_final = time.time()
        tempo_total = tempo_final - tempo_inicio

        if palavra_acertada:
            print(f"\nTempo de jogo: {formatar_tempo(tempo_total)}")
            ranking = atualizar_ranking(jogador, 1, tempo_total)
            print("\nRanking atual:")
            for nome, pts, tempo_medio in ranking:
                tempo_formatado = formatar_tempo(tempo_medio)
                print(
                    f"{nome} - {pts} palavra(s) acertada(s) - Tempo médio: {tempo_formatado}")

        continuar = input(
            "\nDeseja continuar jogando? (S/N): ").strip().upper()
        if continuar != 'S':
            return


def menu_principal():
    limpar_arquivo_palavras()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== JOGO DA FORCA ===")
        print("1. Jogar")
        print("2. Adicionar palavra")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '1':
            jogar_forca()
        elif opcao == '2':
            adicionar_palavra()
            input("\nPressione ENTER para continuar...")
        elif opcao == '3':
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    menu_principal()
