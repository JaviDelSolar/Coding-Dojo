from app_dojos_ninjas import app #escribir el paquete que contiene la estructura modularizada
from app_dojos_ninjas.controladores import controlador_dojos, controlador_ninja #escribir el archivo python que esta en controladores


if __name__=="__main__":
    app.run(debug=True, port= 5001)