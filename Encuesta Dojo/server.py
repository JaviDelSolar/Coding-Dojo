from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="clave secreta"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicacion']
    session['idioma'] = request.form['idioma']
    session['comentarios'] = request.form['comentarios']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route("/nueva/encuesta", methods =['POST'])
def agregar_encuesta():
    nueva_encuesta ={
        "nombre": request.form["nombre"],
        "unicacion": request.form["ubicación"],
        "idioma": request.form["idioma"],
        "comentarios": request.form["comentarios"]
    }
    print(request.form)
    index.append(nueva_encuesta)
    return redirect("/index")


if __name__=="__main__": 
    app.run(debug=True)  