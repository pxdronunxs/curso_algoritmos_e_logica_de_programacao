estoque = {"Tomate": [1000, 2.30], "Alface": [ 500, 0.45], "Batata": [2001, 1.20], "Feijao": [ 100, 1.50]}

venda = [["Tomate", 5], ["Batata", 10], ["Alface", 5]]
total = 0
print("Vendas:\n")
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo total: {total:22.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preco: {dados[1]:6.2f}\n")

