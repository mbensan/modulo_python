import random
from flask import Blueprint, render_template, redirect, session, request

azar = Blueprint('azar', __name__)


@azar.route('/clear')
def clear():
    session.clear()
    return redirect('/')


@azar.route('/')         
def index():
    
    if session.get('num') is None:
        num_azar = random.randint(1, 100)
        print(f'El numero generado es el {num_azar}')
        session['num'] = num_azar

    return render_template("index.html")


@azar.route('/guess', methods=['POST'])         
def guess():
    intento = request.form['intento']
    print(f'Se intentó el número ' + intento)
    intento = int(intento)

    if session.get('intentos') is None:
        session['intentos'] = 1
    else:
        session['intentos'] += 1
    
    if intento > session['num']:
        session['clase'] = 'primary'
    elif intento < session['num']:
        session['clase'] = 'danger'
    else:
        session['clase'] = 'success'

    return redirect('/')


