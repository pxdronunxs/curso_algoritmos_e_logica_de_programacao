a = float(input("Informe a quantidade de kWh foram consumidos no total: "))

print("[R] RESIDENCIAL")
print("[I] INDUSTRIAL")
print("[C] COMERCIAL")

b = (input("Informe qual o tipo de instalação: "))

if b == "R":
    if a <= 500:
        a = a * 0.40
    else:
        a = a * 0.65
elif b == "I":
    if a <= 5000:
        a = a * 0.55
    else:
        a = a * 0.60
elif b == "C":

    if a <= 1000:
        a = a * 0.55
    else:
        a = a * 0.60
print(f"O valor total a se pagar é de: R$ {a:.2f}")
