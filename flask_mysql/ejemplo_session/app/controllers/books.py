import json
from flask import request, redirect, render_template, Blueprint
from app.models.books import Book
from app.models.users import User
from app.models.favorites import Favorite


books = Blueprint('books', __name__, template_folder='templates')

@books.route('/')
def home():
    users = User.get_all()
    books = Book.get_all()
    favorites = Favorite.get_all()
    #import pdb; pdb.set_trace()
    return render_template('favorites.html',
                           users=users,
                           books=books,
                           favorites=favorites)


@books.route('/add-favorite', methods=['POST'])
def add_favorite():
    print('usuario', request.form['user_id'])
    print('libro', request.form['book_id'])
    Favorite.create(request.form['user_id'], request.form['book_id'])
    return redirect('/books')

@books.route('/delete-favorite/<user_id>/<book_id>')
def delete_favorite(user_id, book_id):
    Favorite.delete(user_id, book_id)
    return redirect('/books')
