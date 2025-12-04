import sqlite3

dados = [
    ["AC", "Norte", "Acre"],
    ["AL", "Nordeste", "Alagoas"],
    ["AP", "Norte", "Amapá"],
    ["AM", "Norte", "Amazonas"],
    ["BA", "Nordeste", "Bahia"],
    ["CE", "Nordeste", "Ceará"],
    ["DF", "Centro-Oeste", "Distrito Federal"],
    ["ES", "Sudeste", "Espírito Santo"],
    ["GO", "Centro-Oeste", "Goiás"],
    ["MA", "Nordeste", "Maranhão"],
    ["MT", "Centro-Oeste", "Mato Grosso"],
    ["MS", "Centro-Oeste", "Mato Grosso do Sul"],
    ["MG", "Sudeste", "Minas Gerais"],
    ["PA", "Norte", "Pará"],
    ["PB", "Nordeste", "Paraíba"],
    ["PR", "Sul", "Paraná"],
    ["PE", "Nordeste", "Pernambuco"],
    ["PI", "Nordeste", "Piauí"],
    ["RJ", "Sudeste", "Rio de Janeiro"],
    ["RN", "Nordeste", "Rio Grande do Norte"],
    ["RS", "Sul", "Rio Grande do Sul"],
    ["RO", "Norte", "Rondônia"],
    ["RR", "Norte", "Roraima"],
    ["SC", "Sul", "Santa Catarina"],
    ["SP", "Sudeste", "São Paulo"],
    ["SE", "Nordeste", "Sergipe"],
    ["TO", "Norte", "Tocantins"],
]

with sqlite3.connect("brasil.db") as conexao:
    conexao.executemany("""UPDATE estados
                        set sigla = ?,
                        regiao = ?
                        where nome = ?""", dados)