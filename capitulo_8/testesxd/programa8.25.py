# navegando listas a partir do tipo de seus elementos

L = ["a", ["b", "c", "d"], "e"]

for e in L:
    if isinstance(e, str):
        print(e)
    else:
        print("Lista:", end="")
        for x in e:
            print(f" {x}", end="")
        print()
