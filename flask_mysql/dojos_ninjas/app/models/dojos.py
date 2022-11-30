# from datetime import datetime
from app.models.connection import connectToMySQL 

class Dojo:
    
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.create_time = data['create_time']
        self.update_time = data['update_time']
    
    @classmethod
    def create(cls, name):
        query = '''
            insert into dojos (name) values (%(name)s)
        '''
        data = {
            'name': name
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ninjasdojos').query_db(query, data)
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM dojos '''
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ninjasdojos').query_db(query)

        # crear una lista vacía para agregar nuestras instancias
        dojos = []
        
        # Iterar sobre los resultados de la base de datos y crear instancias de tweets con cls
        for result in results:
            new_dojo = cls(result)  
            dojos.append( new_dojo )
        
        return dojos
