# 1.- Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ]
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1 1.- Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ]
x[ 1 ][ 0 ] = 15
print( x )

print("------")

#1 2.- Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [ {'first_name':  'Michael', 'last_name' : 'Jordan'}, {'first_name' : 'John', 'last_name' : 'Rosales'} ]

estudiantes[ 0 ][ 'last_name' ] = 'Bryant'

print( estudiantes )

print("------")

#1 3.- En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes[ 'fútbol' ][ 0 ] = 'Andrés' #Primero tomo el diccionario y despues lista

print( directorio_deportes )

print("------")

#1 4.- Cambia el valor 20 en z a 30.

z = [ {'x': 10, 'y': 20} ]

z[ 0 ]['y'] = 30 #Primero recorro la lista y luego el diccionario

print( z )

print ("-------")

# 2.-Iterar a través de una lista de diccionarios

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(estudiantes):
    for item in range(0, len(estudiantes)):
        lista = ""
        for key, value in estudiantes[item].items(): 
            lista += f" {key} - {value},"
        print(lista)

iterateDictionary(estudiantes)

print("------")

#3.- Obtener valores de una lista de diccionarios

#Imprimir 'first_name'
def iterateDictionary2(key_name, estudiantes):
    for item in range(0, len(estudiantes)):
        for key, value in estudiantes[item].items():
            if key == key_name:
                print(value)

iterateDictionary2('first_name', estudiantes)

print("------")

#Imprimir 'last_name'
iterateDictionary2('last_name', estudiantes)

print("------")

#4.- Iterar a través de un diccionarios con valores de lista

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print("--------------")
        print(f"{len(value)} {key.upper()}")
        for item in range(0, len(value)):
            print(value[item])

printInfo(dojo)
