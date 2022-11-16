#sall
import logging
from splunk_handler import SplunkHandler
from flask import Flask, request, jsonify
import json 
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from flask_cors import CORS


splunk = SplunkHandler(
    host='splunk.kaderim.svc.cluster.local',
    port='8088',
    token='baaa78c2-e7c8-497c-b853-0d78917a96e5',
    index='main',
    verify=False
)

logging.getLogger('').addHandler(splunk)
logging.warning('hello!')


##TEST_TESTqweqweqweSS
client = MongoClient()
client = MongoClient("mongodb://admin:A123a123@mongo.kaderim.svc.cluster.local:27017/?authMechanism=DEFAULT&authSource=admin")

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

@app.route("/", methods=['GET'])
def all_users():
    return parse_mongo(client.kader.users.find())

@app.route("/bar")
def bar ():
    return parse_mongo(client.kader.users.find())[0]

@app.route("/filter_users", methods=['POST'])
def filter_users():
    data = request.get_json()
    soldiers = client.kader.users.find({"gender":data.genders})
    for soldier in soldiers:
        client.kader.users.update_one({ "name": soldier['name']}, {
        "$addToSet": {"activities":[data['name']]}
    })
    return "ok", 200

@app.route("/<user_id>")
def login(user_id):
    return parse_mongo(client.kader.users.find_one(ObjectId(user_id)))

@app.route("/",methods=['PUT'])
def update_item():
    data = request.get_json()
    client.kader.users.update_one({ "name": data["name"] }, {
        "$set": {"amount":data["amount"]}
    })
    return 'success', 200

@app.route("/", methods=['POST'])
def add_user():
    data = request.get_json()
    client.kader.users.insert_one(data)
   
    return 'success', 200

def parse_mongo(data):
    return jsonify(json.loads(json_util.dumps(data)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
