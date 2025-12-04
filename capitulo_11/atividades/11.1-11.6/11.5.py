import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""update precos set valor = valor * 1.1  """)
        print("Registros alterados: ", cursor.rowcount)