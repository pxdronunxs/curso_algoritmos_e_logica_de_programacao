class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

    def __str__(self):
        return f"{self.nome} - {self.populacao:,} habitantes"