import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/')         
def index():
    
    if session.get('num') is None:
        num_azar = random.randint(1, 100)
        print(f'El numero generado es el {num_azar}')
        session['num'] = num_azar

    return render_template("index.html")


@app.route('/guess', methods=['POST'])         
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


if __name__=="__main__":   
    app.run(debug=True)    
