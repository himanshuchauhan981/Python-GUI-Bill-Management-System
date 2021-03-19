from flask import Blueprint, request, jsonify, make_response
import json

from modules.user.UserController import UserController

user_api = Blueprint('user_api', __name__)


@user_api.route('/login', methods=['POST'])
def login():
    return "hello world"


@user_api.route('/signup', methods=['POST'])
def signup():
    user_controller = UserController()
    signup_credentials = json.loads(request.data)

    user_response = user_controller.signup_user(signup_credentials)
    print(user_response)
    return make_response(jsonify(user_response), 200)

