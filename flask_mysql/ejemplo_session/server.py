from app import app


from app.controllers.azar import azar
from app.controllers.twitter import twitter
from app.controllers.books import books

app.register_blueprint(azar)
app.register_blueprint(twitter, url_prefix='/twitter')
app.register_blueprint(books, url_prefix='/books')


if __name__=="__main__":   
    app.run(debug=True)    
