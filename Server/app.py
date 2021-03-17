from flask import Flask


def create_flask_app():
    app = Flask(__name__)

    from modules.user.route import user_api
    app.register_blueprint(user_api)
    return app
