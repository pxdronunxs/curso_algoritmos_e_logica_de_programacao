frase = input("Digite uma frase: ")
print(f"Frase: {frase}")

frase_lower = frase.lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in frase_lower:
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1

print(f"A frase contém: {a} : a")
print(f"{e} : e")
print(f"{i} : i")
print(f"{o} : o")
print(f"{u} : u")

