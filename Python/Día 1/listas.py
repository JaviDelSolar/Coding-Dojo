#Lista es igual a un arreglo
#Acá la variable va con []
nombres = ['Alejandro', 'Martha', 'Roger', 'Julieta', 'Lucia', 'Fernanda', 'Alan']

print( nombres )
print( nombres[1] )

nombres[3] = 'Julie' #Si queremos modificar algún nombre, tenemos que indicar en que indice queremos usar.
print( nombres)

#Si yo quisiera agredar un nombre a mi lista, ocupo .append

nombres.append( 'Ana' )
print( nombres, len( nombres ) ) #len nos da la longitud de nuestra lista

#nombres.pop() #pop elimina algun elemento de mi lista.
print( nombres, len( nombres ) )

#nombres.pop(1) #elimina que indice yo quiero remover
print( nombres, len( nombres ) )

print( nombres[1:4] ) 
"""
Esta sintaxis me permite seleccionar los valores de mi lista
que no deseo. 1 sería de donde comienza y 4 sería hasta donde 
termina, es decir hasta donde quiero que me imprima de mi variable.
"""
"""
1. ()
2. * / %
3. + -
4. += -=
5. = 

&& ---> and 
|| ---> or
! ---> not


"""