from flask import Flask
from flask_bcrypt import Bcrypt

from tortoise import Tortoise, run_async

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'


bcrypt = Bcrypt(app)


async def init():
    await Tortoise.init(
        db_url='mysql://root:1005@localhost:3306/ejemplo_orm',
        modules={'models': ['app.models.dojos']}
    )
    await Tortoise.generate_schemas()

run_async(init())