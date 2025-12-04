string = "TTAAC"

t = 0
a = 0
c = 0

for e in string:
        if e == "T":
            t += 1
        elif e == "A":
            a += 1
        elif e == "C":
            c += 1
            print(f"T = {t}x")
            print(f"A = {a}x")
            print(f"C = {c}x")
