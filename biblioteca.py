class pessoa():
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


