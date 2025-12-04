import sqlite3
dados = [("Joao", "999999999"),
         ("Andre", "988888888"),
         ("Maria", "977777777")]

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.executemany("""
insert into agenda (nome, telefone)
                   values(?, ?)
                   """, dados)

conexao.commit()
cursor.close()
conexao.close()
