# Los controladores nos ayudan a desplegar la ruta
# Despliega el HTML del dojo

from flask import render_template, request, redirect
from app_dojos_ninjas import app
from app_dojos_ninjas.modelos.modelo_dojos import Dojo

# Crear las rutas
@app.route('/dojos', methods = ['GET'] )
def obtener_dojos():
    lista_dojos = Dojo.obtener_todos()
    return render_template( 'dojos.html', lista_dojos = lista_dojos ) #Esta es la primera ruta para mostrar 

@app.route('/nuevo/dojo', methods=['POST'])
def crear_dojo():
    nuevo_dojo = {
        "nombre": request.form['nombre']
    }
    Dojo.crear_uno(nuevo_dojo)
    return redirect('/dojos')

@app.route('/dojo/<int:id>', methods = ['GET'] ) #Aca despliega dojos con ninjas
def obtener_dojo( id ):
    data = {
        "id" : id
    }
    lista_postres = Dojo.obener_uno_con_ninjas( data )
    return render_template( 'pies.html', lista_postres = lista_postres )