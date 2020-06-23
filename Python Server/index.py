from flask import Flask, jsonify, request
import pyrebase
from flask_cors import CORS

firebaseConfig = {
  "apiKey": "AIzaSyDR7J1rPCLL_dQ_fIepJS76JDTQSgBzSco",
  "authDomain": "bill-management-firebase.firebaseapp.com",
  "databaseURL": "https://bill-management-firebase.firebaseio.com",
  "projectId": "bill-management-firebase",
  "storageBucket": "bill-management-firebase.appspot.com",
  "messagingSenderId": "571970783216",
  "appId": "1:571970783216:web:a7b3af47e8df127bae3f35",
  "measurementId": "G-MHGWLH7X76"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)
CORS(app)


@app.route('/api/login',methods=['POST'])
def loginuser():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        user = auth.sign_in_with_email_and_password(email,password)
        print(user)
        return jsonify(
            data='hello'
        )


if __name__ == "__main__":
    app.run(debug=True)