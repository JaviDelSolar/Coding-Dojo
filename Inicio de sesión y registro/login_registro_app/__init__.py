from flask import Flask 
import re

app=Flask(__name__)
app.secret_key = "esto es secreto"
BASE_DATOS = "bd_login_registro"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
#Este es para el formulario de email

NOMBRE_REGEX = re.compile(r'^[A-Z]{1}[a-zA-Z ]+$')
#Funcion regular que tenga una cantidad de letras (se busca en internet y hay varias opciones)
#Poner espacio para tener sepacion de nombres al lado de la Z mayúscula
 