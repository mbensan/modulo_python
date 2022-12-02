# from datetime import datetime
from flask import flash
from app.models.connection import connectToMySQL 
from app import bcrypt

class User:
    
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.avatar = data['avatar']

    @classmethod
    def validate(cls, form):
        is_valid = True
        # 1. validamos el nombre
        if form['name'].strip() == '':
            is_valid = False
            flash('Debe ingresar un nombre', 'error')
        # 2. validamos la contraseña
        if form['password'].strip() == '':
            is_valid = False
            flash('Debe ingresar una contraseña', 'error')
        
        # 3. validamos que las contraseñas coincidan
        if form['password'] != form['password_confirm']:
            is_valid = False
            flash('Ambas contraseñas debe coincidir', 'error')
        
        # 4. validamos que no exista previamente otro usuario con el mismo email
        if not cls.check_email(form['email']):
            is_valid = False
            flash('Ese email ya se encuentra registrado', 'error')

        return is_valid


    @classmethod   
    def check_email(cls, email):
        query = '''
            select * from users where email=%(email)s
        '''
        data = {
            'email': email
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ninjasdojos').query_db(query, data)

        if len(results) == 0:
            return True
        else:
            return False

    @classmethod
    def create(cls, name, email, password):
        query = '''
            insert into users (name, email, password) values (%(name)s, %(email)s, %(password)s)
        '''
        data = {
            'name': name,
            'email': email,
            'password': bcrypt.generate_password_hash(password)
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        new_user_id = connectToMySQL('ninjasdojos').query_db(query, data)

        # retornamos el ID del usuario recientemente creado
        return new_user_id
    
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_with_credentials(cls, email, password):
        # 1. Obtenemos el usuario
        query = '''SELECT * FROM users where email=%(email)s'''

        data = {
            'email': email
        }
        
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('ninjasdojos').query_db(query, data)

        if len(results) == 0:
            flash('Email inexistente o contraseña incorrecta', 'error')
            return None
        
        # 2. Verificar que las contraseñas coincidan
        encriptada = results[0]['password']

        if not bcrypt.check_password_hash(encriptada, password):
            flash('Email inexistente o contraseña incorrecta', 'error')
            return None
        
        # si llegamos hasta acá, todo está OK
        return cls(results[0])

