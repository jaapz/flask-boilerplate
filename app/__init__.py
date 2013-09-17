from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from app import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'Yolo'
