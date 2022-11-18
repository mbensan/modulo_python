from time import sleep
from flask import Flask, render_template, request, redirect
import socios as soc

app = Flask(__name__)


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html", datos=request.form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


@app.route('/socios')
def get_socios():
    socios = soc.get_socios()
    return render_template('socios.html', socios=socios)


@app.route('/addsocio', methods=['POST'])
def addsocio():
    soc.add_socio(
        request.form['first_name'],
        request.form['last_name'],
        request.form['student_id']
    )
    return redirect('/socios')

if __name__=="__main__":   
    app.run(debug=True)    