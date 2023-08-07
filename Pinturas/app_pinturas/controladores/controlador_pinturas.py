from flask import render_template, redirect, request, session
from app_pinturas.modelos.modelo_pinturas import Pintura

from app_pinturas import app

@app.route ('/pinturas', methods = ['GET']) 
def desplegar_pinturas():
    if "id_usuario" not in session:
        return redirect('/')
    else:
        lista_pinturas = Pintura.obtener_todas_con_usuarios()
        return render_template ('/pinturas.html', lista_pinturas = lista_pinturas)

@app.route('/formulario/pintura') 
def desplegar_formulario_pintura():
    if "id_usuario" not in session:
        return redirect('/')
    else:
        return render_template ('/formulario_pintura.html')
    
@app.route('/crear/pintura', methods=['POST'])
def nueva_pintura():
    data = {
        **request.form,
        "id_usuario": session['id_usuario']
    }
    if not Pintura.validar_formulario_pinturas(data):
        return redirect('/formulario/pintura')
    else:
        id_pintura = Pintura.crear_uno(data)
        return redirect('/pinturas')
    
@app.route ('/eliminar/pintura/<int:id>', methods = ['POST'])
def eliminar_pintura (id):
    data = {
        "id" : id
    }
    Pintura.elimina_uno (data)
    return redirect ('/pinturas')

@app.route('/pintura/<int:id>', methods =['GET'])
def desplegar_pintura(id):
    if "id_usuario" not in session:
        return redirect('/')
    else:
        data ={
            "id" : id
        }
        pintura = Pintura.obtener_uno_con_usuario(data)
        return render_template('pintura.html', pintura = pintura)

@app.route('/formulario/editar/pintura/<int:id>', methods =['GET'])
def desplegar_editar_pintura(id):
    if "id_usuario" not in session:
        return redirect('/')
    else:
        data ={
            "id" : id
        }
        pintura = Pintura.obtener_uno(data)
        return render_template('editar_pintura.html', pintura = pintura)

@app.route('/editar/pintura/<int:id>', methods =['POST'])
def editar_pintura(id):
    if Pintura.validar_formulario_pinturas (request.form) == False:
        return redirect ( f'/formulario/editar/pintura/{id}' )
    else:
        data = {
            **request.form,
            "id" : id
        }
        Pintura.editar_uno (data)
        return redirect ('/pinturas')

