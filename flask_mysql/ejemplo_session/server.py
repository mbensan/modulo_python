from app import app


from app.controllers.azar import azar
from app.controllers.twitter import twitter

app.register_blueprint(azar)
app.register_blueprint(twitter, url_prefix='/twitter')


if __name__=="__main__":   
    app.run(debug=True)    
