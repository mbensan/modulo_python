from app import app

# registramos los controladores de la app
from app.controllers.dojos import dojos
from app.controllers.auth import auth

app.register_blueprint(dojos)
app.register_blueprint(auth)

if __name__=="__main__":   
    app.run(debug=True)    
