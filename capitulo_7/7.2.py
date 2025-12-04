string1 = "AAACTBF"
string2 = "CBT"
string3 = ""
for e in string1:
    if e in string2 and e not in string3:
        string3 += e

print(f"Caracteres em comum: {string3}")

