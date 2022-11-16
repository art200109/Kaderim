#sall
from flask import Flask, render_template, request, jsonify
import os
import urllib.request, json 
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from flask_cors import CORS

##TEST_TESTqweqweqweSS
client = MongoClient()
client = MongoClient("mongodb://admin:A123a123@mongodb-36-rhel7.kaderim.svc.cluster.local:27017/?authMechanism=DEFAULT&authSource=kader")

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

@app.route("/", methods=['GET'])
def all_users():
    return parse_mongo(client.kader.users.find())

@app.route("/bar")
def bar ():
    return parse_mongo(client.kader.users.find())[0]

@app.route("/girls")
def get_girls():
    return parse_mongo(client.kader.users.find(gender=1))

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
