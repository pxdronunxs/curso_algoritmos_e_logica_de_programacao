from collections import UserList

# class ListaÚnica:
#     def __init__(self, elem_classe):
#         self.lista = []
#         self.elem_classe = elem_classe
    
#     def __len__(self):
#         return len(self.lista)
    
#     def __iter__(self):
#         return iter(self.lista)
    
#     def __getitem__(self, posicao):
#         return self.lista[posicao]
    
#     def indiceValido(self, indice):
#         return indice >= 0 and indice < len(self.lista)
    
#     def adiciona(self, elem):
#         if self.pesquisa(elem) == -1:
#             self.lista.append(elem)

#     def remove(self, elem):
#         self.lista.remove(elem)

#     def pesquisa(self, elem):
#         self.verifica_tipo(elem)
#         try:
#             return self.lista.index(elem)
#         except ValueError:
#             return -1
        
#     def verifica_tipo(self, elem):
#         if not isinstance(elem, self.elem_classe):
#             raise TypeError("Tipo inválido")
        
#     def ordena(self, chave=None):
#         self.lista.sort(key=chave)


class ListaÚnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe
    
    def append(self, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().append(elem)
    
    def extend(self, lista_elementos):
        for elem in lista_elementos:
            self.verifica_tipo(elem)
            if elem not in self.data:
                super().append(elem)
        
    def __setitem__(self, posicao, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().__setitem__(posicao, elem)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo inválido")