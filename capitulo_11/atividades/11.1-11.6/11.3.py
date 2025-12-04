import sqlite3
from contextlib import closing

produto = input("Produto a selecionar: ")
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("select * from precos where produto = ?", (produto,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada encontrado.")
                break
            print(f"Produto: {resultado[0]}\nPreço: {resultado[1]}")
            x += 1