# import flask microservice. #
from flask import Flask
# import data model. #
from models import db

# initialize Flask object . #
votr = Flask(__name__)

# load config from the config file we created earlier. #
votr.config.from_object('config')

# initialize and create the database. #
db.init_app(votr)
db.create_all(app=votr)

@votr.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    votr.run()