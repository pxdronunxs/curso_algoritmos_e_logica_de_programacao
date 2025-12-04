#pesquisa de todas ocorrencias
s = "um tigre, dois tigres, tres tigres"
p = 0

while(p > -1):
    p = s.find("tigre", p)
    if p >= 0:
        print(f"Posição: {p}")
        p += 1
