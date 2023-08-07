from flask import Flask

app = Flask(__name__)
app.secret_key = "Esto es un secreto" #Se ocupa solo cuando utilizamos session  
BASE_DATOS = "esquema_dojos_y_ninjas"  #Acá tiene que ir el nombre del proyecto que esta en la BD