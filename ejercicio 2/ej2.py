from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/') # define la ruta con la que se ingresa en el explorador

# muestra la pagina
def index():
	return render_template('formEjercicio.html')

# define la ruta y metodo con el que se debe llegar a este endpoint
@app.route('/respuesta', methods = ['POST']) # agarra los datos que estan en /respuesta (url)
def action_form():

	if request.method == 'POST':
		data = request.form
        nombre = data["usuario"]
        contrasenia = data["contra"]
        return render_template('respuesta.html', nom=nombre, contra=contrasenia) # respuesta.html es un archivo

if __name__ == "__main__":
    app.run (host = '127.0.0.1', port = 5000)

