from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.usuario import Usuario

#app = Flask(__name__)
app.secret_key = "esto es secreto"

@app.route('/')
def index():
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/usuarios/nuevo')
def nuevo():
    return render_template("crear_usuario.html") #Agregar un nuevo usuario

@app.route('/usuarios/crear', methods=['POST'])
def crear():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    
    # Crear un diccionario con los datos del nuevo usuario
    data = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email
    }
    
    # Guardar el nuevo usuario en la base de datos
    Usuario.save(data)
    
    # Redirigir a la página de usuarios
    return redirect('/usuarios')

@app.route('/usuario/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        # Obtener los datos del formulario de edición
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']

        # Crear un diccionario con los nuevos datos del usuario
        data = {
            'id': id,
            'nombre': nombre,
            'apellido': apellido,
            'email': email
        }

        # Actualizar el usuario en la base de datos
        Usuario.update(data)

        # Redirigir a la página de usuarios
        return redirect('/usuarios')
    else:
        # Obtener el usuario a editar
        data = {'id': id}
        usuario = Usuario.obtener_uno(data)
        print(usuario)  # Imprimir el objeto usuario en la consola para verificar los datos

        # Renderizar la plantilla de edición de usuario con los datos actuales del usuario
        return render_template("editar_usuario.html", usuario=usuario)

@app.route('/usuario/mostrar/<int:id>')
def mostrar(id):
    data = {"id": id}

    # Muestra el usuario de la base de datos
    usuario = Usuario.obtener_uno(data)

    # Redirigir a la página de usuarios
    return render_template("mostrar_usuario.html", usuario=usuario)

@app.route('/usuario/eliminar/<int:id>')
def eliminar(id):
    data = {'id': id}
    
    # Eliminar el usuario de la base de datos
    Usuario.eliminar(data)
    
    # Redirigir a la página de usuarios
    return redirect('/usuarios')


if __name__ == "__main__":
    app.run(debug=True)



