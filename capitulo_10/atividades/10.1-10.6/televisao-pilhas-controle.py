class Televisao:
    def __init__(self, canal, canal_min=2, canal_max=14):
        self.ligada = False
        self.canal = canal
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.tamanho = 0
        self.marca = ""

    
    def muda_canal_para_baixo(self):
        if self.ligada == True:
            if self.canal - 1 >= self.canal_min:
                self.canal -= 1
            else:
                self.canal = self.canal_max
        else:
            print("Tv Desligada!")

    
    def muda_canal_para_cima(self):
        if self.ligada == True:
            if self.canal + 1 <= self.canal_max:
                self.canal += 1
            else:
                self.canal = self.canal_min
        else:
            print("Tv Desligada!")   
                 


class Pilha:
    def __init__(self, energia=100):
        self.energia = energia


    def consuma(self, consumo):
        if self.energia >= consumo:
            self.energia -= consumo
            return True
        return False
    


class ControleRemoto:
    def __init__(self, televisao, pilha=None):
        self.televisao = televisao
        self.pilha = pilha if pilha is not None else Pilha()

    
    def liga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = True

    
    def desliga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = False

    
    def canal_mais(self):
        if self.pilha.consuma(1):
            self.televisao.muda_canal_para_cima()
    
    
    def canal_menos(self):
        if self.pilha.consuma(1):
            self.televisao.muda_canal_para_baixo()