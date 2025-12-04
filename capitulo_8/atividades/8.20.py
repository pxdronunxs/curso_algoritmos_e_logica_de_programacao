def gerador_fatorial(n):
    f = 1
    for e in range(1, n + 1):
        f *= e
        yield f
fatorial = list(gerador_fatorial(7))

print(fatorial)