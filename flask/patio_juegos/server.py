from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return '<h3>Tarea patio de juegos</h3>'


@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def play(num=3, color='cadetblue'):
    return render_template('play.html', num=num, color=color)


if __name__ == '__main__':
    app.run(debug=True)
