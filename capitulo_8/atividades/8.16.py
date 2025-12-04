# jogo do alienigena

import random

MAX_TENTATIVAS = 20
vida = 100

arvore = random.randint(1, 100)

print("Um alienigena esta encondido atras de uma arvore")
print("Cada arvore foi enumerada de 1 a 100.")
print("Você iniciará o jogo com 100 de vida.")
print("Voce perderá entre 1 e 20 de vida por cada tentatida errada")


for tentativa in range(1, MAX_TENTATIVAS + 1):
    if vida <= 0:
        print("Voce perdeu toda a sua vida")
        break
    print(f"Voce está com {vida} de vida")
    palpite = int(input(f"Arvore {tentativa}/{MAX_TENTATIVAS}: "))
    if palpite == arvore:
        print(f"Voce acertou na {tentativa}\u00aa tentativa")
        break
    elif palpite > arvore:
        ataque = random.randint(5, 20)
        vida -= ataque
        print("Muito alto")
    else:
        ataque = random.randint(5, 20)
        vida -= ataque
        print("Muito baixo")
else:
    print("Voce nao conseguiu acertar.")
    print(f"O alienigena estava escondido no arvore {arvore}")
