# 1.-Cuenta regresiva:
def cuenta_regresiva( num ):
    resultado = []
    resultado.append( num )
    num -= 1

    for i in range ( num, -1, -1 ): 
        resultado.append( i )

    return resultado    

lista= cuenta_regresiva(5)

print(lista)

# 2.-Imprimir y devolver:
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimir_devolver ():
    a = 1
    print(a)
    if a < 2:
        return 2
    else:
        return 10
print(imprimir_devolver())

# 3.- Primero más longitud: 

def primero_mas_longitud( lista ):
    resultado = lista[0] + len( lista )
    return resultado
resultado = primero_mas_longitud( [1, 2, 3, 4, 5] )

print( resultado) 

# 4.- Valores mayores que el segundo:

def valores_mayores_que_el_segundo(lista):
    resultado = []
    if len( lista ) >=2:
        for numero in lista:
            if numero > lista [1]:
                resultado.append( numero )
    
    print ( len( resultado ) )
    if len( resultado ) < 2:
        return False
    else:
        return resultado
    
lista = valores_mayores_que_el_segundo( [5, 2, 3, 2, 1, 4] )
print( lista )

# 5.- Esta longitud, ese valor: 

def longitud_valor( longitud, valor ):
    lista= []
    i = 1
    while i <= longitud:
        lista.append( valor )
        i+= 1
    return lista

resultado = longitud_valor( 4, 7 )
print( resultado )
resultado1 = longitud_valor( 6, 2 ) 
print( resultado1 )

#El valor se repite en la lista tantas veces como indique la longitud proporcionada al llamar a la función longitud_valor.