from functools import total_ordering
@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.nome} Chave: {self.__chave}>"
    
    def __eq__(self, outro):
        resultado = self.nome == outro.nome
        print(f"__eq__ chamado: {resultado}")
        return resultado
    
    def __lt__(self, outro):
        resultado = self.nome < outro.nome
        print(f"__lt__ chamado: {resultado}")
        return resultado
    
    @property
    def chave(self):
        return self.__chave
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Nome nao pode ser nulo nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)
    
    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()