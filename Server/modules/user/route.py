from flask import Blueprint

user_api = Blueprint('user_api', __name__)


@user_api.route('/login', methods=['POST'])
def login():
    return "hello world"

