from flask import Flask
from config import Config

# Start the flask app with the correct configuration
app = Flask(__name__)
app.config.from_object(Config)

# end of file imports serve as a workaround to circular imports in flask
from app import routes