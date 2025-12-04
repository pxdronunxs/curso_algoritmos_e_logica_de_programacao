# def map_1(funcao, valores):
#     retorno = []
#     for v in valores:
#         retorno.append(funcao(v))
#     return retorno

# print(map_1(lambda x: x/2, [1, 2, 3]))

#======================================================#

# funcao_map_e_list = list(map(lambda x: x/2, [1, 2, 3]))
# print(funcao_map_e_list)

#======================================================#

# somar_listas_com_map = list(map(lambda a, b: a + b, [1, 2, 3], [4, 5, 6]))
# print(somar_listas_com_map)

# PRA FICAR MAIS FACIL DE ENTENDER

# tupla_com_os_parametros = list(map(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6]))
# print(tupla_com_os_parametros)

#======================================================#

# funca_zip = list(zip([1, 2, 3], [4, 5, 6]))
# print(funca_zip)

#======================================================#

# def map_2(funcao, *valores):
#     retorno = []
#     for v in zip(*valores):
#         retorno.append(funcao(*v))
#     return retorno

# print(map_2(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6]))

#======================================================#

# def map_3(funcao, *valores):
#     for v in zip(*valores):
#         yield funcao(*v)

# funcao_map3 = list(map_3(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6]))
# print(funcao_map3)

#OOOOOOOOOOOOOOOUUUUUUUUUUUU

# usando_comprehension = [e for e in zip([1, 2, 3], [4, 5, 6])]
# print(usando_comprehension)

#OOOOOOOOOOOOOOOUUUUUUUUUUUU

# usando_comprehensio_e_list = list(zip([1, 2, 3], [4, 5, 6]))
# print(usando_comprehensio_e_list)

#======================================================#

from functools import reduce
#funcao reduce
# imprimir = reduce(min, [2, 1, 9, 4])
# print(imprimir)

# imprimir = reduce(max, [1, 0, 9, 4])
# print(imprimir)

#======================================================#

precos_produtos = [
    1000,
    2000,
    3000,
    6000,
    7500,
    7800,
    9200,
    9450
]

def aplicar_aumento(preco):
    if preco > 5000:
        return preco * 1.15
    else:
        return preco
novos_precos = list(map(aplicar_aumento, precos_produtos))
for preco in novos_precos:
    print(f"{preco:,.2f}")
