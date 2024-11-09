
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from bson.json_util import dumps
from bson.objectid import ObjectId
from database import mongo

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/add", methods=['POST'])
def add_user():
    _json = request.json;
    _name = _json['name'];
    _email = _json['email'];
    _password = _json['password'];

    if _name and _email and _password:
        _hashed_password = generate_password_hash(_password)
        
        result = mongo.db.Assign.insert_one({'name': _name, 'email': _email, 'password': _hashed_password})
        if result.inserted_id:
            resp = jsonify(message="User created")
            resp.status_code = 201;
            return resp;
            
    else:
        return not_found()  
        

@user_bp.route('/users')
def get_users():
    users = mongo.db.Assign.find();
    return dumps(users);

@user_bp.route("/users/<id>")
def get_user(id):
    user = mongo.db.Assign.find_one({'_id': ObjectId(id)});
    return dumps(user);

@user_bp.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    mongo.db.Assign.delete_one({"_id": ObjectId(id)});
    resp = jsonify(message="User deleted successfully");
    resp.status_code = 200;
    return resp;

@user_bp.route("/users/<id>", methods=["PUT"])
def update_user(id):
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password:
        _hashed_password = generate_password_hash(_password);
        mongo.db.Assign.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}}
        )
        resp = jsonify(message="User updated successfully")
        resp.status = 200
        return resp
    else:
        return not_found()
    

@user_bp.app_errorhandler(400)
def not_found(error=None):
    meessage = {'status': 400, 'meessage': 'Not Foundd' + request.url}
    resp = jsonify(meessage);
    resp.status_code =400
    return resp
