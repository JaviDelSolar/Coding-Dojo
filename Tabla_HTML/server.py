from flask import Flask, render_template

app = Flask(__name__)

@app.route("/tabla")
def tabla():
    usuarios = [
        {'nombre' : 'Michael', 'apellido' : 'Choi', 'nombre completo' :'Michael Choi'},
        {'nombre' : 'John', 'apellido' : 'Supsupin', 'nombre completo' :'John Supsupin'},
        {'nombre' : 'Mark', 'apellido' : 'Guillen', 'nombre completo' :'Mark Guillen'},
        {'nombre' : 'KB', 'apellido' : 'Tonel', 'nombre completo' :'KB Tonel'}
    ]

    return render_template("index.html",usuarios=usuarios)

if __name__=="__main__":
    app.run(debug=True)