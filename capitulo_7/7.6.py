string1 = "AATTCGAA"
string2 = "TG"
string3 = "AC"
string4 = ""

for letra in string1:
    if letra in string2:
        i = string2.index(letra)
        string4 += string3[i]
    else:
        string4 += letra

print("Resultado:", string4)
