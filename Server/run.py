from app import create_flask_app

flask_object = create_flask_app()

if __name__ == '__main__':
    flask_object.run(debug=True)
