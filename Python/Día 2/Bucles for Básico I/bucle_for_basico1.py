#Básico: imprime todos los números enteros del 0 al 150.
for bsc in range(150):
    print(bsc)

for bsc in range(151):
    print(bsc)

for bsc in range(0, 151):
    print(bsc)

print( "----------" )
#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

for bsc in range(5, 1001): #Condicionales
    if (bsc % 5 == 0):
        print(bsc)

for bsc in range(5, 1001, 5): #Saltos
        print(bsc)

print( "----------" )

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
#Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

for bsc in range(1, 101):
    if bsc % 5 ==0:
        if bsc % 2 ==0:
              print("Coding Dojo")
        else:
             print("Coding")
    else:
         print(bsc)

print( "----------" )

#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

suma = 0
for bsc in range(0, 500001):
    if bsc % 2 != 0:
         suma += bsc
print(suma) 

suma=0
for bsc in range(1, 500001, 2):
         suma += bsc
print(suma) 

print( "----------" )

#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4

num = 2018

while num > 0:
    print(num)
    num -= 4

print( "----------" )

#Contador flexible: establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
#Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)