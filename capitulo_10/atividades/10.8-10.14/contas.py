class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        if saldo > 0:
            self.deposito(saldo)

    def resumo(self):
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nome}  Tel.:  {cliente.telefone}")
            print(f"CC Nº:   {self.numero}   Saldo: {self.saldo:10.2f}\n")

    def pode_sacar(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            print("Transação autorizada!")
            return True
        else:
            print("Transação negada!")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        for operacao in self.operacoes:
            if operacao[0] == "DEPOSITO":
                print(f"{operacao[0]:10s} +{operacao[1]:9.2f}")
            else:
                print(f"{operacao[0]:10s} -{operacao[1]:9.2f}")
        print(f"\n      Saldo: {self.saldo:10.2f}\n")




class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
    
    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor
    
    def saque(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            print("Transação autorizada!")
            return True
        else:
            print("Transação negada!")
            return False
        
    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        print(f"Limite de conta especial: {self.limite:10.2f}")
        print(f"Saldo disponível para saque: {self.saldo + self.limite:10.2f}\n")
        for operacao in self.operacoes:
            if operacao[0] == "DEPOSITO":
                print(f"{operacao[0]:10s} +{operacao[1]:9.2f}")
            else:
                print(f"{operacao[0]:10s} -{operacao[1]:9.2f}")
        print(f"\n      Saldo: {self.saldo:10.2f}\n")