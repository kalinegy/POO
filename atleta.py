class Atleta():
    def __init__(self,peso,aposentado= False):
        self.peso= peso
        self.aposentado= aposentado

    def aposentar(self):
        self.aposentado= True
        print("O atleta foi aposentado")

    def aquecer(self):
        print("O atleta está aquecendo")

    def atletaAposentado(self):
        if self.aposentado:
            print("Atleta aposentado!")
        else:
            print("Atleta ativo")

class Corredor(Atleta):
    def __init__(self, peso, aposentado= False):
        super().__init__(peso, aposentado)
    def correr(self):
       if self.aposentado == False:
           print("O corredor está correndo.")
       else:
           print("O corredor se aposentou,portanto,não pode correr.")

class Nadador(Atleta):
    def __init__(self, peso, aposentado= False):
        super().__init__(peso, aposentado)
    def nadar(self):
       if self.aposentado == False:
           print("O nadador está nadando.")
       else:
           print("O nadador se aposentou,portanto,não pode nadar.")

class Ciclista(Atleta):
    def __init__(self, peso, aposentado= False):
        super().__init__(peso, aposentado)
    def pedalar(self):
       if self.aposentado == False:
           print("O ciclista está pedalando.")
       else:
           print("O ciclista se aposentou,portanto,não pode pedalar.")

class TriAtleta(Corredor,Nadador, Ciclista):
    def __init__(self, peso, aposentado= False):
        Atleta.__init__(self,peso, aposentado)
