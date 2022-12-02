# from datetime import datetime
from flask import flash
from app.models.connection import connectToMySQL
from app.models.dojos import Dojo

class Ninja:
    
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.create_time = data['create_time']
        self.update_time = data['update_time']
    
    @staticmethod
    def validate(form):
        is_valid = True
        # primero valido el nombre
        name = form['name'].strip()
        if name == '':
            flash('El nombre no puede ser vacío', 'error')
            is_valid = False
        elif len(name) < 3:
            flash('El largo del nombre debe ser al menos 3', 'error')
            is_valid = False
        
        # ahora valido el apellido
        last_name = form['last_name'].strip()
        if last_name == '':
            flash('El apellido no puede ser vacío', 'error')
            is_valid = False
        elif len(last_name) < 3:
            flash('El largo del apellido debe ser al menos 3', 'error')
            is_valid = False
        
        age = int(form['age'].strip())
        if age < 18:
            flash('La edad debe ser de al menos 18 años', 'error')
            is_valid = False
        
        return is_valid

    @classmethod
    def create(cls, name, last_name, age, dojo_id):

        query = '''
            insert into ninjas (name, last_name, age, dojo_id)
            values (%(name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        '''
        data = {
            'name': name,
            'last_name': last_name,
            'age': int(age),
            'dojo_id': int(dojo_id)
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ninjasdojos').query_db(query, data)
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM ninjas 
        join dojos on ninjas.dojo_id=dojos.id '''
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ninjasdojos').query_db(query)

        # crear una lista vacía para agregar nuestras instancias
        ninjas = []
        
        # Iterar sobre los resultados de la base de datos y crear instancias de tweets con cls
        for result in results:
            # por cada diccionario en results creo un Ninja
            new_ninja = cls(result)
            # y creo un Dojo
            dojo = Dojo({
                'id': result['dojos.id'],
                'name': result['dojos.name'],
                'create_time': result['dojos.create_time'],
                'update_time': result['dojos.update_time']
            })
            # uno ambos objetos
            new_ninja.dojo = dojo

            ninjas.append( new_ninja )
        
        return ninjas
