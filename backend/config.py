from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Specify the location of the local sql database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# Not going to track all the modifications we make to the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create a database instance
db = SQLAlchemy(app)


