#salleedasdasdasd
from flask import Flask, render_template, request, jsonify
import os
import urllib.request, json 
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from flask_cors import CORS
import requests

##TEST_TESTSS
client = MongoClient()
client = MongoClient("mongodb://admin:A123a123@mongodb-36-rhel7.kaderim.svc.cluster.local:27017/?authMechanism=DEFAULT&authSource=kader")

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

@app.route("/",methods=["GET"])
def all_activities():
    return parse_mongo(client.kader.activities.find())

@app.route("/<activity_id>")
def get_activity(activity_id):
    return parse_mongo(client.kader.activities.find_one(ObjectId(activity_id)))

@app.route("/",methods=['PUT'])
def update_item():
    data = request.get_json()
    client.kader.users.update_one({ "name": data["name"] }, {
        "$set": {"amount":data["amount"]}
    })
    return 'success', 200

@app.route("/", methods=['POST'])
def add_activity():
    data = request.get_json()
    client.kader.activities.insert_one(data)
    properties = json.loads(data)
    with open('/log', 'w') as f:
        f.write("properties:" + properties['gender'])
    #result = requests.post('http://users.kaderim.svc.clutser.local/filter_users', json=data)
    result = requests.get("http://users.kaderim.svc.clutser.local/filter_users?gender={gender}&rank={rank}".format(
                                                                                                                gender=properties['gender'],
                                                                                                                rank=properties['rank'] )
    print(result)
    return 'success', 200

def parse_mongo(data):
    return jsonify(json.loads(json_util.dumps(data)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
