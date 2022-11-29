from datetime import datetime
from app.models.connection import connectToMySQL
from app.models.books import Book
from app.models.users import User

class Favorite:
    
    def __init__( self , data ):
        self.user_id = data['user_id']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.book = None
        self.user = None
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = '''
            SELECT * FROM favorites
            join users on users.id = favorites.user_id
            join books on books.id = favorites.book_id
        '''
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        favorites = []
        
        # Iterar sobre los resultados de la base de datos y crear instancias de tweets con cls
        for result in results:
            # primero creamos el objeto Favorite
            new_favorite = cls(result)
            # creamos el usuario de este favorito
            new_user = User({
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'id': result['id'],
                'handle': result['handle'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at'],
            })
            # creamos el libro de este favorito
            new_book = Book({
                'id': result['books.id'],
                'title': result['title'],
                'num_pages': result['num_pages'],
                'created_at': result['books.created_at'],
                'updated_at': result['books.updated_at'],
            })
            # juntamos todo
            new_favorite.book = new_book
            new_favorite.user = new_user
            # añadimos el favorito a la lista que queremos retornar
            favorites.append( new_favorite )
        
        return favorites
    
    @classmethod
    def create(cls, user_id, book_id):
        query = '''
            insert into favorites (user_id, book_id)
            values (%(user_id)s, %(book_id)s)
        '''
        data = {
            'user_id': user_id,
            'book_id': book_id
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query, data)


    @classmethod
    def delete(cls, user_id, book_id):
        query = '''
            delete from favorites
            where user_id=%(user_id)s and book_id=%(book_id)s
        '''
        data = {
            'user_id': user_id,
            'book_id': book_id
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query, data)

