def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

print("MMC(6, 8) =", mmc(6, 8))
print("MMC(21, 6) =", mmc(21, 6)) 
