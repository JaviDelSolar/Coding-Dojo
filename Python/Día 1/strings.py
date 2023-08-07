
edad = 25 
nombre = "Alejandro"
apellido = 'Venegas'  

resultado = f'Hola como estás {nombre} {apellido}. ¡Hoy cumples {edad} años!' #Está es la más sencilla 
resultado2 = "Hola como estás" + " " + nombre + " " + apellido + ". ¡Hoy cumples" + " " + str(edad) + " " + "años!"
resultado3 = "Hola como estás {} {}. !Hoy cumples {} años!" .format( nombre, apellido, edad )

print(resultado)
print(resultado2)
print(resultado3)

print( nombre.upper(), len(nombre) )
print( len(nombre), nombre.upper() )


"""
El fomato f, nos ayuda a convertir una variable que no es
strins a strings
"""

name = "Zen"
print("Mi nombre es", name)

name = "Zen"
print("Mi nombre es " + name)

