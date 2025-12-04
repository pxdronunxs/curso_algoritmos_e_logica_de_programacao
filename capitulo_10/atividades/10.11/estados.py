class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def listar_cidades(self):
        print(f"\nCidades de {self.nome} ({self.sigla}):")
        for cidade in self.cidades:
            print(f"  - {cidade.nome}: {cidade.populacao:,} habitantes")

    def __str__(self):
        return f"{self.nome} ({self.sigla}) - {len(self.cidades)} cidades"
        





