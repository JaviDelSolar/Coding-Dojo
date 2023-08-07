from flask import Flask
import re

app = Flask(__name__) 
app.secret_key = "esto es secreto" # Esto en necesario para cuando utilicemos sessiones para que funcione
BASE_DATOS = "esquema_recetas"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[A-Z]{1}[a-zA-Z]+$')


# Acá es donde importamos flask
# Ponemos nuestra base de datos (BASE_DATOS) y despues lo que vayamos necesitando
# importamos nuestra expresión regular 