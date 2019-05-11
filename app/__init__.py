from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Start the flask app with the correct configuration
app = Flask(__name__)
app.config.from_object(Config)

# with the app initialized, connect to the db and perform any migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# end of file imports serve as a workaround to circular imports in flask
from app import routes, models