a = int(input("Digige o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
maior = a
if b > a and b > c:
    maior = b
if c > a and c >= b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c <= b:
    menor = c
print(f"O menor número digigato foi {menor}")
print(f"O maior número digitado foi {maior}")
