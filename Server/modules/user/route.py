from flask import Blueprint, request
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

    user = user_controller.signup_user(signup_credentials)


    return signup_credentials

