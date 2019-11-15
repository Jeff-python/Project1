from flask import Flask, jsonify, request
from models import User
from models import Listing
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/api/register', methods=["POST"])
def add_user():
    data = request.get_json()
    new_register = User(data['firstname'], data['lastname'], data['username'], data['email'], data['password'])
    new_register.insert()
    return jsonify({"status":"Success"})

@app.route('/api/update', methods=["POST"])
def update_user():
    data = request.get_json()
    new_register = User(data['firstname'], data['lastname'], data['username'], data['email'], data['password'])
    new_register.insert()
    return jsonify({"status":"Success"})





