#La función nos ayuda a reciclar códigos 

def suma_dos_numeros ( num1=10, num2=15 ): #Se dan valores a los num para ver el resultado3
    total = num1 + num2
    return total

#def suma_dos_numeros ( num1, num2 ):
    return total
#resultado = suma_dos_numeros ( 20, 30 )
#print ( resultado )

#resultado2 = suma_dos_numeros ( resultado, 50 )
#print ( resultado2 )

resultado3 = suma_dos_numeros ( 80 ) #En esta función el 80 fue enviado al num1 "Se sobreescribe en elnparametro num1"
print ( resultado3 )

resultado4 = suma_dos_numeros () #En esta función como no tenemos un parametro, el resultado será la suma de los num de la función 
print ( resultado4 )

resultado5 = suma_dos_numeros( num2 = 80 ) #En esta función el 80 se le indica que se sobrescriba en el num2 
print( resultado5 )

resultado6 = suma_dos_numeros( num2 = 80, num1 = 30 ) #En esta función el 80 se le indica que se sobrescriba en el num2 y 30 en el num1
print( resultado6 )

#resultado4 = suma_dos_numeros()
#print( resultado4 )

def suma_numeros( num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0, num6 = 0 ):
    suma_total = num1 + num2 + num3 + num4 + num5 + num6
    return suma_total

suma_dos = suma_numeros( 20, 50 )
print( f"Suma dos {suma_dos}" )
suma_tres = suma_numeros( 20, 30, 40 )
print( f"Suma tres {suma_tres}" )
suma_cuatro = suma_numeros( 10, 10, 10, 10 )
print( f"Suma cuatro {suma_cuatro}" )
suma_cinco = suma_numeros( 1, 2, 3, 4, 5 )
print( f"Suma cinco {suma_cinco}" )


