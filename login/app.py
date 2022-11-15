#sall
from flask import Flask, render_template, request, jsonify
import os
import urllib.request, json 
from pymongo import MongoClient
from bson import json_util, ObjectId
import json

##TEST_TESTSS
client = MongoClient()
client = MongoClient("mongodb://admin:A123a123@mongodb-36-rhel7.kaderim.svc.cluster.local:27017/?authMechanism=DEFAULT&authSource=kader")

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def all_menu():
    return parse_mongo(client.kader.users.find())

@app.route("/<username>")
def login(username):
    return parse_mongo(client.kader.users.find_one({"name": username}))

def parse_mongo(data):
    return jsonify(json.loads(json_util.dumps(data)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
