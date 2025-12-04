# 10 primeiros multiplos de 3

a = 3
while a <= 30:
    if a % 3 == 0:
        print(a)
        a = a + 3
    else:
        a = a + 1
    print(a)
    a = a + 2
