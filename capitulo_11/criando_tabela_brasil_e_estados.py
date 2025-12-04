import sqlite3
from contextlib import closing

dados = [
    ["São Paulo", 46081801],
    ["Minas Gerais", 21393441],
    ["Rio de Janeiro", 17223547],
    ["Bahia", 14870907],
    ["Paraná", 11890517],
    ["Rio Grande do Sul", 11233263],
    ["Pernambuco", 9562007],
    ["Ceará", 9268836],
    ["Pará", 8711196],
    ["Santa Catarina", 8187029],
    ["Goiás", 7423629],
    ["Maranhão", 7018211],
    ["Paraíba", 4164468],
    ["Amazonas", 4321616],
    ["Espírito Santo", 4126854],
    ["Mato Grosso", 3893659],
    ["Rio Grande do Norte", 3455236],
    ["Piauí", 3384547],
    ["Alagoas", 3220848],
    ["Mato Grosso do Sul", 2924631],
    ["Distrito Federal", 2996899],
    ["Sergipe", 2299425],
    ["Rondônia", 1751950],
    ["Tocantins", 1586859],
    ["Acre", 884372],
    ["Amapá", 806517],
    ["Roraima", 738772],
]

with sqlite3.connect("brasil.db") as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""CREATE TABLE estados(
                       id integer primary key autoincrement,
                       nome text,
                       populacao integer
                       )""")
        cursor.executemany("INSERT into estados (nome, populacao) values(?, ?)", dados)
    conexao.commit()