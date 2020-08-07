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
NumNames = db['NumNames']
NumNames.insert_one({'num_of_names': 0})
my_names_col = db['Names']


class NamesResource(Resource):
    def get(self):
        # Get the name entries from some public api such as Facebook Graph API,
        # Linkedin's API, or randomuser.me API.
        entries = []
        display_str = ''
        for entry in entries:
            my_dict = {
                'first': entry[0].first,
                'last': entry[0].last,
                'middle': entry[0].middle
            }
            name = my_name_col.insert_one(my_dict)
            display_str += ('Inserted id: {} into DB'.format(name.inserted_id))

        display_str += 'Processed all Names Data.'
        return display_str


@app.route('/')
def hello_world():
    return "Hello, world! Go to /namesearch for the name search endpoint"


@app.route('/namesearch', methods=['GET', 'POST'])
def namesearch():
    data_type = None
    if request.method == 'POST':
        req = request.form
        text = req['data_field']
    return render_template('index.html', ssc_items=display_items['SSC'], ssd_items=display_items['SSD'], ssc=SSC_FLAG, ssd=SSD_FLAG, data_title=DATA_TITLE)

# Add resource access for the names endpoint.
api.add_resource(NamesResource, "/names")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
