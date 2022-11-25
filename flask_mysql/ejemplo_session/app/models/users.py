from app.models.connection import connectToMySQL

class User:
    
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.name = self.first_name + ' ' + self.last_name
        self.handle = data['handle']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('twitter').query_db(query)
        
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        
        # Iterar sobre los resultados de la base de datos y crear instancias de users con cls
        for user in results:
            users.append( cls(user) )
        return users