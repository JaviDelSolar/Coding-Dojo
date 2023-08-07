# 1.-Cuenta regresiva:
def cuenta_regresiva( num ):
    resultado = []
    resultado.append( num )
    num -= 1

    for i in range ( num, -1, -1 ): #num >-1   num -=1
        resultado.append( i )

    return resultado    

lista1= cuenta_regresiva(5)
lista2= cuenta_regresiva(10)
lista3= cuenta_regresiva(20)


print(lista1)
print(lista2)
print(lista3)

# 2.-Imprimir y devolver:
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

resultado = imprimir_y_devolver([1, 2])
print(resultado)

#3.- Primero más longitud: 

def primero_mas_longitud( lista ):
    resultado = lista[0] + len( lista ) #Suma de del primer número de la lista (1) + la cantidad de numeros que hay en la lista (5) = 6
    return resultado
resultado = primero_mas_longitud( [1, 2, 3, 4, 5] )
resultado1 = primero_mas_longitud( [10, 20, 30, 40, 50, 60, 70] ) #Suma de del primer número de la lista (10) + la cantidad de numeros que hay en la lista (7) = 17

print( resultado ) 
print( resultado1 )

#Otra opción
def primero_mas_longitud( lista ):
    resultado = 1 + len( lista ) #Suma de del primer número de la lista (1) + la cantidad de numeros que hay en la lista (5) = 6
    return resultado
resultado = primero_mas_longitud( [1, 2, 3, 4, 5] )
resultado1 = primero_mas_longitud( [10, 20, 30, 40, 50, 60, 70] ) #Suma de del primer número de la lista (10) + la cantidad de numeros que hay en la lista (7) = 17

print( resultado ) 
print( resultado1 )

# 4.- Valores mayores que el segundo:
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]

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
lista1 = valores_mayores_que_el_segundo( [3] )
print( lista1 )
lista2 = valores_mayores_que_el_segundo( [8, 3, 2, 9, 7, 5, 1, 10, 6, 4] )
print( lista2 )

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