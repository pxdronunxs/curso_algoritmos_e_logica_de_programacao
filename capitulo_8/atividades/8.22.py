from functools import partial
import operator
import math

def executa(operacao, simbolo, operando1, operando2=None):
    if operando2 is None:
        resultado = operacao(float(operando1))
        print(f"{simbolo}{operando1} = {resultado}")
    else:
        resultado = operacao(float(operando1), float(operando2))
        print(f"{operando1} {simbolo} {operando2} = {resultado}")

operacoes = {
    "+": partial(executa, operator.add, "+"),
    "-": partial(executa, operator.sub, "-"),
    "*": partial(executa, operator.mul, "x"),
    "/": partial(executa, operator.truediv, "÷"),
    "**": partial(executa, operator.pow, "^"),
    "√": partial(executa, math.sqrt, "√")
}

operacao = input("Operação (+, -, *, /, **, √): ").strip()

if operacao == "√":
    operando1 = input("Número: ")
    operacoes[operacao](operando1)
elif operacao in operacoes:
    operando1 = input("Operando 1: ")
    operando2 = input("Operando 2: ")
    operacoes[operacao](operando1, operando2)
else:
    print("Operação inválida!")
