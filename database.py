
from flask import Flask

app = Flask(__name__)


app.config['MONGO_URI']='mongodb+srv://Hari:Hari@cluster0.1b5ei80.mongodb.net/test'
from flask_pymongo import PyMongo
mongo = PyMongo(app)

@app.route('/')
def get_data():
    data = mongo.db.JOBS.find()
    return 'Data:{}'.format(data)

