#Esto es un comentario en línea
"""
Esto
es 
un
comentario
en 
bloque
"""

#Vamos a declarar todos los tipos de  datos primitivos variables python

edad = 25 #Número entero
calificación= 9.6 #Número flotante
nombre = "Alejandro"
apellido = 'Venegas'  
tiene_hermanos = False #Boleeano
aprobado_bootcamp = None #Este es un tipo de dato que aún no tiene un valor

nombre_completo = nombre + " " + apellido #Esta es la forma de nombrar una variables, funciones 

#edad += 4.3

print( edad, calificación ) #Print palabra reservada 

print ( edad, type( edad ) ) #Imprime <class 'int'>
print ( calificación, type( calificación ) ) #Imprime <class 'float'> 
print (nombre, type(nombre) ) #Imprime <class 'str'> 
print (nombre + " " + apellido ) #Concatenar dos variables

"""
Python no nos deja concatenar un str con un número entero, es mucho mas estricto.
Pero para concatenar un numero entero con un str, debemos convertir el n° entero,
en str y eso se realiza así: str(edad)
"""

print (nombre + " " + apellido + " " + str(edad) + " " + str(calificación) )
