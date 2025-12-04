# EMPRESA = "DIAMBA CONNECTION LTDA"

# def imprimir_cabecalho(x):
#     print(EMPRESA)
#     print("-" * len(EMPRESA))

# imprimir_cabecalho(EMPRESA)

#-------------------------------------#

# a = 5
# def muda_e_imprime():
#     a = 7
#     print(f"A dentro da função: {a}")
# print(f"a antes de mudar: {a}")
# muda_e_imprime()
# a = 8
# print(f"a depois de mudar: {a}")


#-------------------------------------#

# import random
# for x in range(10):
#     print(random.randint(1, 10000))

#-------------------------------------#

# import random

# tentativas = 3
# n = random.randint(1, 20)


# while tentativas > 0:
#     x = int(input("Escolha um numero entre 1 e 20: "))

#     if x == n:
#         print("Voce acertou!")
#         break
#     else:
#         tentativas -= 1
#         if tentativas > 0:
#             print(f"Voce errou. Restam {tentativas} tentativas.")
#         else:
#             print("Voce perdeu as 3 tentativas!")
#             print(f"O numero correto era {n}.")

#-------------------------------------#

import random
for x in range(10):
    print(random.uniform(10, 20))
