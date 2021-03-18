from firebase_admin import auth, exceptions
from firebase_admin import firestore

from modules.user.Schema import UserSchema


class UserController:
    def __init__(self):
        self.db = firestore.client()

    def signup_user(self, credentials):
        response = {}
        try:
            new_user = auth.create_user(email=credentials['email'], password=credentials['password'])

            user = UserSchema(credentials['mobile_number'], new_user.uid)
            self.db.collection('user').add(user.to_dict())

        except exceptions.FirebaseError as error:
            if error.code == 'ALREADY_EXISTS':
                response['msg'] = 'Email ID already existed'
            else:
                response['msg'] = 'Unexpected error'

        return 0
