from datetime import datetime
from app.models.connection import connectToMySQL 

class Book:
    
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM books '''
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query)

        # crear una lista vacía para agregar nuestras instancias de friends
        books = []
        
        # Iterar sobre los resultados de la base de datos y crear instancias de tweets con cls
        for result in results:
            new_book = cls(result)  
            books.append( new_book )
        
        return books
