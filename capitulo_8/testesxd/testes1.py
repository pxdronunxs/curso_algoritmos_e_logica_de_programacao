# -------------------------------------#

# def soma(a, b):
#     print(a + b)

# soma(2, 9)
# soma(7, 8)
# soma(10, 15)

# # no caso de nao precisar printar, apenar realizar a funcao. se precisar printar, faz como no exemplo abaixo # #
# def soma(a, b):
#     return a + b
# print(soma(2, 9))
# -------------------------------------#
# def épar(x):
#     return x % 2 == 0
# print(épar(2))
# print(épar(3))
# print(épar(10))

# -------------------------------------#

# def épar(x):
#     return x % 2 == 0

# def parOuImpar(x):
#     if épar(x):
#         return "par"
#     else:
#         return "ímpar"

# print(parOuImpar(4))
# print(parOuImpar(5))

# -------------------------------------#

# def fatorial(n):
#     print(f"Calculando o fatorial de {n}")
#     if n == 0 or n == 1:
#         print(f"Fatorial de {n} = 1")
#         return 1
#     else:
#         fat = n * fatorial(n - 1)
#         print(f"Fatorial de {n} = {fat}")
#         return fat

# fatorial(4)

# -------------------------------------#

# x1, y1 = -2.5, 0.4
# x2, y2 = 12.1, 7.3

# distancia = float(((x2 - x1)) ** 2 + ((y2 - y1)) ** 2) ** 0.5
# print(f"{distancia:.4f}")

# -------------------------------------#

# distancia = int(input())
# tempo = distancia * 2
# print(f"{tempo} minutos")

# -------------------------------------#

# horas = 0
# minutos = 0
# segundos = 0

# segundos_totais = int(input())
# if segundos_totais >= 3600:
#     horas = segundos_totais // 3600
#     segundos_totais = segundos_totais - (horas * 3600)
# if segundos_totais >= 60:
#     minutos = segundos_totais // 60
#     segundos_totais = segundos_totais - (minutos * 60)
# segundos = segundos_totais
# print(f"{horas}:{minutos}:{segundos}")

# -------------------------------------#

# codigo_do_item, quantidade = map(int, input().split())
# preco = float(0)

# if codigo_do_item == 1:
#     preco = 4 * quantidade
# elif codigo_do_item == 2:
#     preco = 4.5 * quantidade
# elif codigo_do_item == 3:
#     preco = 5 * quantidade
# elif codigo_do_item == 4:
#     preco = 2 * quantidade
# elif codigo_do_item == 5:
#     preco = 1.5 * quantidade

# print(f"Total: R$ {preco:.2f}")

# -------------------------------------#

# for e in range(2, 101, 2):
#     print(e)

# -------------------------------------#

# a = "abc"
# print(type(a))

# -------------------------------------#

# positivos = 0

# for e in range(6):
#     valor = float(input())
#     if valor > 0:
#         positivos += 1

# print(f"{positivos} valores positivos")

# -------------------------------------#

# pares = 0

# for e in range(5):
#     valor = int(input())
#     if valor % 2 == 0:
#         pares += 1

# print(f"{pares} valores pares")

# -------------------------------------#

# pares = 0
# impares = 0
# positivos = 0
# negativos = 0


# for e in range(5):
#     valor = int(input())
#     if valor % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if valor > 0:
#         positivos += 1
#     elif valor < 0:
#         negativos += 1

# print(f"{pares} valor(es) par(es)")
# print(f"{impares} valor(es) impar(es)")
# print(f"{positivos} valor(es) positivo(s)")
# print(f"{negativos} valor(es) negativo(s)")

# -------------------------------------#

# valor = int(input())

# contador = 0
# while contador < 6:
#     if valor % 2 != 0:
#         print(valor)
#         contador += 1
#     valor += 1

# -------------------------------------#

# valor = int(input())

# dentro = 0
# fora = 0

# for e in range(valor):
#     valores = int(input())
#     if 10 <= valores <= 20:
#         dentro += 1
#     else:
#         fora += 1

# print(f"{dentro} in")
# print(f"{fora} out")

# -------------------------------------#

# numero = int(input())

# for e in range(1, numero + 1):
#     if e % 2 == 0:
#         print(f"{e}^2 = {e * e}")

# -------------------------------------#

# numero = int(input())

# contador = 1

# while contador <= 10:
#     print(f"{contador} x {numero} = {contador * numero}")
#     contador += 1

# --------------------------------------#

# notas = int(input())

# for e in range(notas):
#     a, b, c = map(float, input().split())
#     media = (a * 2 + b * 3 + c * 5) / 10
#     print(f"{media:.1f}")

# --------------------------------------#

i = 1
j = 60

while j >= 0:
    print(f"I={i} J={j}")
    i += 3
    j -= 5
