import json
from flask import request, redirect, render_template, Blueprint
from app.models.users import User
from app.models.tweets import Tweet


twitter = Blueprint('twitter', __name__, template_folder='templates')

@twitter.route('/users')
def users_page():
    users = User.get_all()
    return render_template('users.html', users=users)


@twitter.route('/tweets')
def tweets_page():
    tweets = Tweet.get_all()
    users = User.get_all()
    return render_template('tweets.html', tweets=tweets, users=users)

@twitter.route('/tweet/<id>')
def single_tweet(id):
    
    tweet = Tweet.get(id)
    
    return json.dumps({
        'id': tweet.id,
        'user_name': tweet.user_name,
        'tweet': tweet.tweet
    })

@twitter.route('/add-tweet', methods=['POST'])
def add_tweet():
    Tweet.create(request.form['tweet'], request.form['user_id'])
    return redirect('/tweets')


@twitter.route('/delete-tweet/<int:id>')
def delete_tweet(id):
    print(f'eliminando el tweet de ID {id}')
    Tweet.delete(id)
    return redirect('/tweets')

