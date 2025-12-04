palavra = input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()

digitadas = []
acertos = []
erros = 0

# Lista com os desenhos do boneco
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

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("Digite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou essa letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    # Mostra o boneco conforme a quantidade de erros
    print(desenho[erros])

    if erros == 6:
        print("Enforcado!")
        break
