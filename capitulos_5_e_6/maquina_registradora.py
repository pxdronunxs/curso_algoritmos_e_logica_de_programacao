total = 0
subtotal = 0


while True:
     codigo = int(input("Digite o código do produto ou (0) para finalizar e exibir total: "))

     if codigo == 0:

        print(f"\nTotal da compra: R$ {total:.2f}")
        break
     
     if codigo == 1:
        preco = 0.50

     elif codigo == 2:
        preco = 1.00

     elif codigo == 3:
        preco = 4.00

     elif codigo == 5:
        preco = 7.00

     elif codigo == 9:
        preco = 8.00

     else:
        print("CÓDIGO INVÁLIDO!")
        continue

     quant = int(input("Informe a quantidade de produto(s): "))
     subtotal = quant * preco
     print(f"Subtotal deste produto: R$ {subtotal}")
     total = total + subtotal













