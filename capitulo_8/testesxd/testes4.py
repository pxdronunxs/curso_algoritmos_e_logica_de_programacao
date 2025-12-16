# # L = [x for x in range(10)]
# # print(L)

#-------------------------------------#

# L = []
# for x in range(10):
#     L.append(x)

# print(L)

#-------------------------------------#

# Z = [x * 2 for x in [0, 1, 2, 3]]
# print(Z)

#-------------------------------------#

# y = [(x, x * 2) for x in [1, 2, 3]]
# print(y)

#-------------------------------------#

# z = [s.upper() for s in "abcdf"]
# print(z)

#-------------------------------------#

# pares = [x for x in range(10) if x % 2 == 0]
# print(pares)

#-------------------------------------#

# d = [(y, x) for x, y in [(4, 3), (1, 2), (8, 9)]]
# print(d)

#-------------------------------------#

# g = [(x, y) for *x, y in [(4, 2, 3), (5, 1, 2), (7, 8, 9)]]
# print(g)

#-------------------------------------#

import math
# I = [math.sqrt(z) for z in range(0, 10)]
# print(I)

#-------------------------------------#

# H = [z for z in range(0, 10) if math.sqrt(z) % 1 == 0]
# (print(H))

#-------------------------------------#

# L = [1, 2, 3]
# i = iter(L)
# print(next(i))
# print(next(i))
# print(next(i))

#-------------------------------------#

# def gerador_de_numeros():
#     i = 0
#     while True:
#         yield i
#         i += 1

# g = gerador_de_numeros()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#-------------------------------------#

# def gerador_fibonacci():
#     p = 0
#     s = 1
#     while s < 10:
#         yield s
#         p, s = s, s + p

# [x for x in gerador_fibonacci()]

# fibonacci = list(gerador_fibonacci())
# print(fibonacci)


#-------------------------------------#


# def gerador_fibonacci(fim):
#     p = 0
#     s = 1
#     while s < fim:
#         yield s
#         p, s = s, s + p

# [x for x in gerador_fibonacci(30)]

# fibonacci = list(gerador_fibonacci(30))
# print(fibonacci)

#-------------------------------------#

# [x for x in range(10) if x % 3 == 0]


#-------------------------------------#

# [x for x in range(2, 100) if all(x % i != 0 for i in range(2, x))]

print(1, 12, 25)