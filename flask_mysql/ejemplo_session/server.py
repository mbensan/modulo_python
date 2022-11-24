import random
import json
from flask import Flask, render_template, request, redirect, session
from models.users import User
from models.tweets import Tweet

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


@app.route('/users')
def users_page():
    users = User.get_all()
    return render_template('users.html', users=users)


@app.route('/tweets')
def tweets_page():
    tweets = Tweet.get_all()
    users = User.get_all()
    return render_template('tweets.html', tweets=tweets, users=users)

@app.route('/tweet/<id>')
def single_tweet(id):
    
    tweet = Tweet.get(id)
    
    return json.dumps({
        'id': tweet.id,
        'user_name': tweet.user_name,
        'tweet': tweet.tweet
    })

@app.route('/add-tweet', methods=['POST'])
def add_tweet():
    Tweet.create(request.form['tweet'], request.form['user_id'])
    return redirect('/tweets')


@app.route('/delete-tweet/<int:id>')
def delete_tweet(id):
    print(f'eliminando el tweet de ID {id}')
    Tweet.delete(id)
    return redirect('/tweets')



if __name__=="__main__":   
    app.run(debug=True)    
