from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return '<h3>Hola Curso!!!</h3>'


@app.route('/dos')
def segunda():
    return '<h4>Soy la segunda ruta</h4>'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'<h4>Hola {nombre}, mucho gusto!</h4>'


@app.route('/eliminar/<int:id>')
def eliminar(id):
    return f'Eliminando al usuario {str(id)}'


@app.route('/starwars')
def star_wars():
    user = 'Maria Perez'
    return render_template('star_wars.html', nombre=user, edad=34)


@app.route('/frutas')
def frutas():
    favoritas = ['Piña', 'Guayaba', 'Papaya', 'Melón', 'Sandía']
    peores = [
        {
            'nombre': 'Tuna',
            'valor': '1.20'
        },
        {
            'nombre': 'Brevas',
            'valor': '1.50'
        },
        {
            'nombre': 'Pomelo',
            'valor': '2.00'
        },
        {
            'nombre': 'Uvas',
            'valor': '2.90'
        }
    ]

    return render_template('frutas.html', favoritas=favoritas, peores=peores)



if __name__ == '__main__':
    app.run(debug=True)
