from datetime import datetime
from app.models.connection import connectToMySQL
from app.models.users import User 

class Tweet:
    
    def __init__( self , data ):
        self.id = data['id']
        self.tweet = data['tweet']
        self.user_id = data['user_id']
        #self.user = <Object: User>
        self.author = None
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = '''
            SELECT * FROM tweets 
            join users on tweets.user_id = users.id'''
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query)

        # crear una lista vacía para agregar nuestras instancias de friends
        tweets = []
        
        # Iterar sobre los resultados de la base de datos y crear instancias de tweets con cls
        for result in results:
            author = User({
                'id': result['users.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'handle': result['handle'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at']
            })
            new_tweet = Tweet(result)
            new_tweet.author = author
            tweets.append( new_tweet )
        
        return tweets
    
    @classmethod
    def get(cls, id):
        query = '''
            SELECT * FROM tweets 
            join users on tweets.user_id = users.id
            where tweets.id=%(id)s
        '''
        data = {
            'id': id
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query, data)

        tweet = cls(results[0])
        return tweet
    
    @classmethod
    def create(cls, tweet, user_id):

        query = '''
            insert into tweets (tweet, user_id, created_at, updated_at)
            values (%(tweet)s, %(user_id)s, NOW(), NOW())
        '''
        data = {
            'tweet': tweet,
            'user_id': int(user_id)
        }

        connectToMySQL('twitter').query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = '''
            delete from tweets where id=%(id)s
        '''
        data = {
            'id': id
        }
        connectToMySQL('twitter').query_db(query, data)
