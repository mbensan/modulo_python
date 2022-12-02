from flask import request, redirect, render_template, Blueprint, flash, session
from app.models.users import User

auth = Blueprint('auth', __name__, template_folder='templates')


# rutas nuevas
@auth.route('/')
def home():
    return render_template('home.html')


@auth.route('/auth')
def auth_screen():
    return render_template('auth.html')


@auth.route('/register', methods=['POST'])
def register():
    # 0. Validar el formulario
    if not User.validate(request.form):
        return redirect('/auth')
    
    # 1. Creamos al usuario
    id = User.create(request.form['name'], request.form['email'], request.form['password'])

    # 2. Le damos feedback que fué creado
    flash('Usuario registrado con éxito', 'warning')

    # 3. Guardamos el nuevo usuario en session
    session['user'] = {
        'name': request.form['name'], 
        'email': request.form['email'], 
        'id': id 
    }
    return redirect('/')


@auth.route('/login', methods=['POST'])
def login():
    
    # 1. Recuperar el usuario de la base de datos
    user = User.get_with_credentials(request.form['email'], request.form['password'])

    # 2. Si user es None.
    if user is None:
        return redirect('/auth') 

    # 3. Le damos feedback que fué creado
    flash('Usuario ingresó con éxito', 'info')

    # 4. Guardamos los datos en session
    session['user'] = {
        'name': user.name,
        'email': user.email,
        'id': user.id
    }

    return redirect('/')


@auth.route('/logout')
def logout():
    session['user'] = None
    return redirect('/auth')