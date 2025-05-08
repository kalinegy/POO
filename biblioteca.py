class Pessoa():
    def __init__(self, peso, nome, idade):
        self.nome= nome
        self.peso= peso
        self.idade= idade
        self.comendo= False
        self.falando= False
        self.dormindo= False
    def comer(self, comida):
        if self.comendo == True:
            print(f"{self.nome} está comendo")
        elif self.falando==True:
            print(f"{self.nome} não pode comer {comida} pq está falando")
        elif self.dormindo==True:
            print(f"{self.nome} não pode comer porque está dormindo")
        else:
            self.comendo=True
            print(f"{self.nome} já está comendo")

    def falar(self):
        if self.comendo == True:
            print(f"{self.nome}, não pode falar pq está comendo")
        elif self.falando == True:
            print(f"{self.nome} está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pq está dormindo")
        else:
            self.falando = True
            print(f"{self.nome} já está falando")

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} está dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir pq está falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir porque está comendo")
        else:
            self.dormindo = True
            print(f"{self.nome} já está dormindo")

    def pararcomer(self):
        if self.comendo == True:
            print(f"{self.nome} tem que parar de comer")
            self.comendo == False
        else:
            print(f"Ele já parou de comer")

    def calar(self):
        if self.falando == True:
            print(f"{self.nome} tem que calar a boca")
            self.falando == False

    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} tem que acordar")
            self.dormindo == False


class ContaBancaria():
    def __init__(self, num, nome, tipo):
        self.num = num
        self.nome = nome
        self.tipo = tipo
        self.saldo = 0
        self.limite = 0
        self.status= False


    def ativarConta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada com sucesso!")
        else:
            print("Necessario ativar conta")

    def depositar(self, deposito):
        if self.status == False:
            print("É necessário ativar a conta")
        else:
            print(f"O valor depositado foi de R$ {deposito}")

    def sacar(self, saque):
        if self.status == False:
            print("É necessário ativar a conta")
        else:
            if self.limite + self.saldo < saque:
                print("Não é possível sacar")
            else:
                self.saldo -=  saque
                print(f"Seu saldo atual é de {self.saldo}")

    def verificarSaldo(self):
        if self.status == False:
            print("É necessário ativar a conta")
        else:
            print(f"Seu saldo é {self.saldo}")

    def ajustarLimite(self,limite):
        if self.status == False:
            print("É necessário ativar a conta")
        else:
            self.limite += limite
            print(f"Seu limite foi ajustado para {self.limite}")










