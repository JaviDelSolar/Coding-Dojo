# este es un comentario de una línea
"""
Este es
un comentario
de varias líneas
"""

num1 = 42 #declaración de variables, numero
num2 = 2.3 #declaración de variables, numero
boolean = True #declaración de variables, Booleano
string = 'Hello World' #declaración de variables, cadena (Strings) #declaración de variables, lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declaración de variables, diccionario
fruit = ('blueberry', 'strawberry', 'banana') #declaración de variables, lista
print(type(fruit)) #Función que imprime de la variable fruit ('blueberry', 'strawberry', 'banana')
print(pizza_toppings[1]) #Función que imprime de la variable pizza_toppings ('Sausage')
pizza_toppings.append('Mushrooms') #añadir valor. Agrega un nuevo elemento al final de la lista
print(person['name']) #Función imprime el nombre John
person['name'] = 'George' #valor de cambio. Se cambia el nombre John por el nombre de George
person['eye_color'] = 'blue' #Se agrega un nuevo valor a la variable, donde ahora la perona tiene los ojos blue
print(fruit[2]) #Función imprime Banana

#Condicionales
if num1 > 45:    
    print("It's greater")
else:
    print("It's lower") #It's lower

if len(string) < 5: 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #Just right!

#Bucles con argumentos
for x in range(5): 
    print(x) #Imprimira del 0,1,2,3,4
for x in range(2,5): 
    print(x) #Imprimira del 2,3,4
for x in range(2,10,3): #Bucles que van del 2 al 10, pero van en 3 en 3
    print(x) #Imprimira del 2,5,8 
x = 0 
while(x < 5): #Bucle While
    print(x)
    x += 1 ##Imprimira del 0,1,2,3,4

pizza_toppings.pop() #Elimina el ultimo valor de la lista que sería Olives
pizza_toppings.pop(1) ##Elimina el valor de la lista que sería Sausage

print(person) #Imprimira toda la variable  {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': blue,}
person.pop('eye_color') # ##Elimina el valor de la lista que sería 'eye_color': blue
print(person) #Imprimira nuevamente toda la variable sin 'eye_color': blue {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}


#Bucle que recorre lista
for topping in pizza_toppings: 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement') #Imprimira cuatro veces After 1st if statement
    if topping == 'Olives':
        break

def print_hello_ten_times(): #Función
    for num in range(10): #Bucle
        print('Hello')

print_hello_ten_times() #Imprimira 10 veces Hello

def print_hello_x_times(x): #Función con parámetro
    for num in range(x): #Bucle
        print('Hello')

print_hello_x_times(4) #Imprimira 4 veces Hello

def print_hello_x_or_ten_times(x = 10): #Función con argumento
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #Imprimira 10 veces Hello
print_hello_x_or_ten_times(4) #Imprimira 4 veces Hello


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)