#1
def number_of_food_groups(): 
    return 5
print(number_of_food_groups())

"""
La función no tiene ningún argumento, solo tiene una instrucción de retorno.
"return" lo que esta haciendo es que al momento de llamar a la función, retorna el valor 5
Entonces print llama la función y retorna el valor 5, lo que hará que se imprima el valor 5
"""
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

"""
Al igual que la función anterior, la función number_of_military_branches() no tiene ningún argumento, 
solo tiene una instrucción de retorno que retornará en el valor de 5.
Pero la función number_of_days_in_a_week_silicon_or_triangle_sides(), no está en la función principal, por lo que no 
sabemos el valor que devuelve, entonces no hay suma.
Si number_of_days_in_a_week_silicon_or_triangle_sides() estuviera en el código, ahí print podría realizar la función de imprimir
la suma de ambas funciones. 
"""
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

"""
En esta función tenemos dos instrucciones de retorno, pero al momento de ejecutar el primer return la función termina, 
donde el valor que se va a imprimir es 5, ya que solo se devuelve una vez.
"""
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

"""
Al igual que el ejercicio número 3, solo se va a imprimir el valor de 5, ya que ahí termina la función 
porque se ejecuto la instrucción de retorno y solo se devuelve una vez.
"""
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

"""
En la funcion number_of_great_lakes() solo va a imprimir el valor de 5, pero como no hay un return 
no va asignar ningun valor a la variable. Entonces al momento de dar un valor x = number_of_great_lakes(),
no se le asignara ningún valor, porque no se devolvio ningún valor. 
Se imprime None, porque no hay un resultado específico en la función.
"""
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

"""
En este código a la función add(b,c), posee dos llamadas de argumentos que son el add(1,2) y add(2,3). Al llamar la primera
función va a imprimir 3, y al llamar la segunda función imprimirá 5.
Después se tratará de imprimir la suma de las dos funciones, pero como no hay la función de return para add, no será factible
realizar esta función, porque no devolvio ningún valor. Por eso al momento de ejecutar la terminal sale TypeError, porque no
hay ningún valor que asignar a ese print. 
Al llamar add va a devolver None en lugar de un valor numérico y la suma de none + none va a dar un error de typeError.
"""
#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

"""
En este código, la función concatenate lo que realiza es que toma los dos argumentos y los convierte en cadena
para luego concatena para formar una nueva cadena. Como esta la función return, devuelve el valor como cadena que
sería 25.
"""
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

"""
En ese código se imprimira con primera parte el resulta de 100, ya que print(b), es 100. Luego se ve la condición si
100< a 10, pero es falso, entonces se pasa a la siguiente condición que es donde se termina la funcón. Entonces imprime 
100 y luego 10.
"""
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) 
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

"""
En este código va a imprimir 7, 14 y 21, ya que en la primera condición al llamar a if b<c return 7 es verdadero, entonces imprime 7.
En la segunda condición al llamar a if b<c return 7 es falso, entonces pasa a else y ahí esa condición se cumple, imprimiendo 14.
Luego la suma de ambas funciones da el resultado de 21.
"""
#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

"""
El resultado es 8 de la suma de 3+5 que toman los argumentos de b y c. Al tener un primer return la función se ejecuta,
devuelve el valor indicado y se termina la función, dejando al segundo return sin ejecutarse.
"""
#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

"""
Tenemos una variable con valor de 500 que al momento de ejecutar print(b) imprimirá 500. Después tenemos la función def foobar(),
que tiene una variable de 300, que que al momento de ejecutar print(b), dentro de está función se imprimirá el valor de 300.
Nuevamente se llama a la primera variable y se imprimirá 500, entonces hasta ahora tenemos 500, 500. 
Ahora se llama a la segunda función foobar(), que imprimirá dentro de la función 300 y luego ese valor se imprimira en la terminal, 
dando ahora los valores de 500, 500 y 300. Y por último nuevamente se llama a la primera variable donde se imprimerá 500 en la terminal.
Los valores son: 500, 500, 300, 500
"""
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

"""
En este código pasa lo mismo que el códig anterior, la única diferencia que el
valor de return se devuelve a la función pero no se utiliza en ningún lugar. 
"""
#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

"""
En este código pasa lo mismo que en los ejercicios anteriores, pero ahora en la función foobar() se imprime nuevamente el valor de 300,
realizá la función de return devolviendo el valor de 300 a (b) y ahora fuera de la función en b=foobar() se le asigna el valor de 300
del return y ahora imprime fuera de la función el valor de return. Resultado 500, 500, 300, 300
"""
#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

"""
En este código tenemos dos funciones foo y bar, donde en la primera función def foo(), se indica que debe imprimir 1. Luego pasamos
a las segunda función donde se le indica que debe imprimir 3. Cuando se ejecuta la segunda función ahora vuelve a la funcion foo(),
para seguir ejecutando el código que sigue y se le da la instrucción de ejecutar bar(), imprimiendo el valor de 2. 
El resultado final: 1, 3, 2.
"""
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

"""
Nuevamente tenemos dos funciones foo() y bar(), donde en la primera función def foo() indica que debe imprimir 1. Luego pasamos a la
segunda función def bar(), donde se imprime 3, pero acá tenemos un return que retorna el valor de 5 que se le asignará a la función
bar(), de la primera función. Hasta ahora tenemos impreso los valores de 1 y 3. Ahora volvemos a la funcion foo(), donde se sigue 
ejecutando el código pero ahora bar se le asigna a la variable "x" el valor de 5 e imprimirá ese valor. La funcion foo() retorna 
el valor de 10 del return y se le asigna ahora  ala variable "y", imprimiendo al final 10. Resultado: 1, 3, 5, 10. 
"""