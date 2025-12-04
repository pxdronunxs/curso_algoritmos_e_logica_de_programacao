# aplicação parcial de funções, ser usar partial

import operator

# def executa(operacao, simbolo, operando1, operando2):
#     resultado = operacao(float(operando1), float(operando2))
#     print(f"{operando1} {simbolo} {operando2} = {resultado}")

# operando1 = input("Operador 1: ")
# operando2 = input("Operador 2: ")
# operacao = input("Operacao: ").strip()

# if operacao == "+":
#     executa(operator.add, operacao, operando1, operando2)
# elif operacao == "-":
#     executa(operator.sub, operacao, operando1, operando2)
# elif operacao == "*":
#     executa(operator.mul, operacao, operando1, operando2)
# elif operacao == "/":
#     executa(operator.truediv, operacao, operando1, operando2)

#======================================================#

# aplicação parcial de funções, usando partial

# from functools import partial

# def executa(operacao, simbolo, operando1, operando2):
#     resultado = operacao(float(operando1), float(operando2))
#     print(f"{operando1} {simbolo} {operando2} = {resultado}")

# operacoes = {
#     "+": partial(executa, operator.add, "+"),
#     "-": partial(executa, operator.sub, "-"),
#     "*": partial(executa, operator.mul, "x"),
#     "/": partial(executa, operator.truediv, "÷")}

# operando1 = input("Operador 1: ")
# operando2 = input("Operador 2: ")
# operacao = input("Operacao: ").strip()

# if operacao in operacoes:
#     operacoes[operacao](operando1, operando2)
# else:
#     print("Operacao Inválida!")

#======================================================#

import math

teste_ceil = math.ceil(4.2), math.floor(4.2)
print(teste_ceil)
