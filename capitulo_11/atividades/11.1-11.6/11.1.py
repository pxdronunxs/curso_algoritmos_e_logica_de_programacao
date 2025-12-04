import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""create table precos(
                       produto text,
                       valor text)
                       """)
        cursor.execute("""
insert into precos (produto, valor)
                       values(?, ?)
                       """, ("prensado", "10"))
conexao.commit()