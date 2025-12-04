string1 = "AABBEFAATT"
string2 = "BE"

posicao = 0
while(posicao > -1):
  posicao = string1.find(string2, posicao)
  if posicao >= 0:
    print(f"{string2} encontrado na posição {posicao}")
    posicao += 1
  else:
    print(f"{string2} não encontrado")
