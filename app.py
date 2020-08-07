from http import HTTPStatus
from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
from pymongo import MongoClient

from flasgger import swag_from
from api.model.name import NameModel
from api.schema.name import NameSchema

app = Flask(__name__)
api = Api(app)


# Create and setup MongoDB client, collections, and global data flags.
client = MongoClient('mongodb://db:27017')
db = client.aNewDB
UserNum = db['UserNum']
UserNum.insert_one({'num_of_users': 0})


# Add resource access for the names endpoint.
api.add_resource(Visit, "/names")


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/search', methods=['GET', 'POST'])
def search():
    data_type = None
    if request.method == 'POST':
        req = request.form
        text = req['data_field']
    return render_template('index.html', ssc_items=display_items['SSC'], ssd_items=display_items['SSD'], ssc=SSC_FLAG, ssd=SSD_FLAG, data_title=DATA_TITLE)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
