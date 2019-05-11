from flask import Flask

app = Flask(__name__)

# end of file imports serve as a workaround to circular imports in flask
from app import routes