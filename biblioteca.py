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


         #herença
class Animal(): #superclasse
    def __init__(self, nome, cor): #metodo construtor
            self.nome= nome
            self.cor= cor
    def comer(self): #metodo
            print(f"O/A {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O/A {self.nome} , de cor {self.cor} está miando...")

class Vaca(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f"A vaca chamada {self.nome} , de cor {self.cor} está mugindo...")
    def comer(self):
            print(f"A vaca {self.nome} está comendo capim...")

class Coelho(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def pular(self):
        print(f"O coelhinho chamado {self.nome} , de pelo {self.cor} está pulando na fazenda...")

class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O cachorro chamado {self.nome}, de cor {self.cor} está latindo...")



class Ingresso(): #superclasse
    def __init__(self, valor): #metodo construtor
            self.valor=valor
    def imprimeValor(self):
            print(f"O valor do ingresso é {self.valor}")
class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *=1.5
    def imprimeValor(self): #polimorfismo
        print(f"O valor do seu ingresso VIP é de {self.valor}")




class Forma():
    def __init__(self):
        self.base= 0
        self.altura= 0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea (self, base, altura):
        self.area= base * altura
        print(f"O da área é de {self.area}")
    def calcularPerimetro(self, base, altura):
            self.perimetro= (base*altura)/2
            print(f"O valor da perímetro é de {self.perimetro}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea (self, base, altura):
        self.area= (base * altura)/2
        print(f"O valor da área é de {self.area}")
    def calcularPerimetro(self, base):
            self.perimetro = base * 3
            print(f"O valor do perímetro é de {self.perimetro}")















