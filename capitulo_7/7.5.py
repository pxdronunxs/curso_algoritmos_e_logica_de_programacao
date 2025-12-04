string1 = "AATTGGAA"
string2 = "TG"
string3 = ""
cont = 0

for letra in string1:
    if letra not in string2:
        string3 += letra
print(f"{string3}")
