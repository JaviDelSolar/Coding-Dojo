from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', num=3, color="yellow")


@app.route('/play/<int:num>')
def nivel_dos(num):
    return render_template("index.html", num=num, color="yellow")


@app.route('/play/<int:num>/<string:color>')
def nivel_3(num, color):
    return render_template("index.html", num=num, color=color)


if __name__ == '__main__':
    app.run( debug= True, port=5000 )
