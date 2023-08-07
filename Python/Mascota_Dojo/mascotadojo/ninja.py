from mascota import mascota

class Ninja(mascota):
    
    def __init__( self, nombre, apellido, mascota, premio, comida_mascota ):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        self.mascota.jugar()
        return self
    
    def alimentar(self):
        for comida in self.comida_mascota:
            print(f"Dar de comer a {self.mascota.name} un {comida}")
            self.mascota.comer()
        return self
        
    def bañar(self):
        self.mascota.sonido()
        return self
        
golosinas = ["Atún", "Trocitos jugosos"]
comida_mascota = ["Pellet", "churu", "croquetas"]
premio = ["ratón"] 

Rami = mascota ("Rami", "Gato", golosinas, "Miau")
javiera = Ninja("Javiera", "Del Solar", Rami, premio, comida_mascota)

javiera.alimentar()
