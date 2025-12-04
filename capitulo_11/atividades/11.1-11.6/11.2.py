import sqlite3
conexao = sqlite3.connect("precos.db")
cursor = conexao.cursor()
cursor.execute("select * from precos")
resultado = cursor.fetchone()
print(f"Produto: {resultado[0]}\nPreço: {resultado[1]}")
cursor.close()
conexao.close()