# def fibonacci(n):
#     print(f"Calculando fibonacci {n}")
#     if n <= 1:
#         print(f"    Fibonacci de {n} = {n}")
#         return n
#     else:
#         print(f"Fibonacci de {n} = fibonacci {n - 1} + fibonacci {n - 2} = ...")
#         resultado = fibonacci(n - 1) + fibonacci(n - 2)
#         print(f"    Fibonacci de {n} = fibonacci {n-1} + fibonacci {n-2} = {resultado}")
#         return resultado

# # chamada fora da função
# fibonacci(5)

#-------------------------------------#

# def mdc(a, b, nivel=0):
#     print("  " * nivel + f"mdc({a}, {b}) chamado")

#     if b == 0:
#         print("  " * nivel + f"b = 0 → retorno {a}")
#         return a
#     else:
#         resto = a % b
#         print("  " * nivel + f"Calculando: mdc({b}, {resto})")
#         return mdc(b, resto, nivel + 1)

# # Exemplo de uso
# resultado = mdc(56, 42)
# print(f"\nMDC final = {resultado}")

#-------------------------------------#

# def mdc(a, b, nivel=0):
#     indent = "  " * nivel  # só para deixar a saída mais organizada
#     print(f"{indent}Calculando mdc({a}, {b})")

#     if b == 0:
#         print(f"{indent}Como b = 0, mdc({a}, {b}) = {a}")
#         return a
#     else:
#         print(f"{indent}Como b != 0, vamos calcular mdc({b}, {a} % {b}) = mdc({b}, {a % b})")
#         return mdc(b, a % b, nivel + 1)

# # Exemplos
# print("Resultado final:", mdc(56, 42))

#-------------------------------------#

# def barra(caractere="-", qtd=40):
#     print(caractere * qtd)

# barra()

#-------------------------------------#


# def soma(a, b, imprime=False):
#     s = a + b
#     if imprime:
#         print(s)
#     return s

# print(soma(4, 5, False))

#-------------------------------------#

# def retangulo(altura, largura, caractere="*"):
#     linha = caractere * largura
#     for i in range(altura):
#         print(linha)

# retangulo(10, 100, "@")

#-------------------------------------#

#-----funcoes como parametro----------#

# def soma(a, b):
#     return a + b
# def subtracao(a, b):
#     return a - b
# def imprime(a, b, foper):
#     print(foper(a, b))

# imprime(5, 4, subtracao)

#-------------------------------------#

# def soma(*numeros):
#     soma = 0
#     for e in numeros:
#         soma += e
#     print(soma)

# soma(2, 3, 4, 8, 6, 7, 56, 5)

#-------------------------------------#

#------------funcoes lambda-----------#

aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5))

