from app import create_flask_app
from db.db_config import DbConfig

flask_object = create_flask_app()

if __name__ == '__main__':
    db_config_obj = DbConfig()

    db_config_obj.setup_firebase_admin()
    flask_object.run(debug=True)
