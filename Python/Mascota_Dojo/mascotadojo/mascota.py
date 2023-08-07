
class mascota():
    def __init__( self, name, tipo, golosina, sonido ):
        self.name = name
        self.tipo = tipo
        self.golosina = golosina
        self.salud = 100
        self.energia = 100
        self.sonido = sonido

    def dormir(self):
        self.energia += 25
        return self
        
    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        return self

    def sonido(self):
        self.sonido += 50


