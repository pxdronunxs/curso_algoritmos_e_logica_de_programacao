# dic = {chave: valor * 2 for chave, valor in {"a": 1, "b": 2}.items()}
# print(dic)

#======================================================#

#dict comprehension com if interno

# dic_com_if = {valor: chave for chave, valor in {"a": 1, "b": 2}.items() if valor % 2 ==0}
# print(dic_com_if)

#======================================================#

set_comprehension = {x for x in [9, 2, 1, 3, 6, 9] if x % 3 == 0}
print(set_comprehension)