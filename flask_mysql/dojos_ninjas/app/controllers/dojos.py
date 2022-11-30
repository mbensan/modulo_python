from flask import request, redirect, render_template, Blueprint, flash
from app.models.dojos import Dojo
from app.models.ninjas import Ninja

dojos = Blueprint('dojos', __name__, template_folder='templates')

@dojos.route('/dojos')
def home():
    # llamar al modelo para recuperar los dojos
    dojos = Dojo.get_all()
    # retornamos el template
    return render_template('dojos.html', dojos=dojos)


@dojos.route('/dojos', methods=['POST'])
def add_dojo():
    # rescato los valores del formulario
    name = request.form['name']
    # llamamos al modelo
    Dojo.create(name)

    flash('Felicidades por añadir un dojo')
    return redirect('/dojos')


@dojos.route('/ninjas', methods=['GET'])
def ninjas():
    # llamar al modelo para recuperar los dojos
    dojos = Dojo.get_all()
    ninjas = Ninja.get_all()
    return render_template('ninjas.html', dojos=dojos, ninjas=ninjas)

@dojos.route('/ninjas', methods=['POST'])
def add_ninja():
    # 0. valido el formulario
    if not Ninja.validate(request.form):
        return redirect('/ninjas')

    # 1. rescato los valores del formulario
    name = request.form['name']
    last_name = request.form['last_name']
    age = request.form['age']
    dojo_id = request.form['dojo_id']
    # 2. llamamos al modelo
    Ninja.create(name, last_name, age, dojo_id)

    # 3. Le doy feedback al usuario
    flash('Haz añadido un ninja correctamente')
    
    return redirect('/ninjas')