import sqlite3
from contextlib import closing

nome = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f"select * from agenda where nome = '{nome}'")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")

            