
local_val = "unicornios mágicos" #variable local
def square(x):
    return x * x                 #Función
class Usuario:                   #Clase
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"
    
print(square(5))
user = Usuario("Anna")
print(user.name)
print(user.di_hola())

print(__name__)







