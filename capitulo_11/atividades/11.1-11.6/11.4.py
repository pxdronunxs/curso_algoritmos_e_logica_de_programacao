import sqlite3
from contextlib import closing

preco_min = float(input("Preço mínimo: "))
preco_max = float(input("Preço máximo: "))

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(
            "SELECT * FROM precos WHERE valor BETWEEN ? AND ?",
            (preco_min, preco_max)
        )
        
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada encontrado nesse intervalo de valores.")
                break
            
            print(f"Produto: {resultado[0]}\nPreço: {resultado[1]}\n")
            x += 1