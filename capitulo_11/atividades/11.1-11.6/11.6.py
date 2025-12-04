import sqlite3
from contextlib import closing

produto = input("Nome do produto a atualizar: ").strip()
novo_valor = float(input("Novo valor: "))

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:

        cursor.execute("SELECT * FROM precos WHERE produto = ?", (produto,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Produto não encontrado no banco de dados.")
        else:
            cursor.execute(
                "UPDATE precos SET valor = ? WHERE produto = ?",
                (novo_valor, produto)
            )
            conexao.commit()
            print(f"Valor do produto '{produto}' atualizado para {novo_valor}.")