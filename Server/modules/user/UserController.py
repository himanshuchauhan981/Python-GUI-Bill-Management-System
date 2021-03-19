from firebase_admin import auth, exceptions
from firebase_admin import firestore

from modules.user.Schema import UserSchema


class UserController:
    def __init__(self):
        self.db = firestore.client()

    def signup_user(self, credentials):
        response = {}
        try:
            existing_user_doc = self.db.collection(u'users').where('mobile_number', '==',
                                                                   credentials['mobile_number']).get()

            if len(existing_user_doc) == 0:
                new_user = auth.create_user(email=credentials['email'], password=credentials['password'])
                user = UserSchema(credentials['mobile_number'], new_user.uid)
                self.db.collection('users').add(user.to_dict())
                response['data'] = {'msg': 'Signup successful', 'status': 200}
            else:
                response['data'] = {'msg': 'User already existed', 'status': 409}
        except exceptions.FirebaseError as error:
            if error.code == 'ALREADY_EXISTS':
                response['msg'] = {'msg': 'User already existed', 'status': 409}
            else:
                response['msg'] = {'msg': 'Unexpected error', 'status': 400}

        return response
