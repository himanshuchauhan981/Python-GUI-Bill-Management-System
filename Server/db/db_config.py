import firebase_admin
from firebase_admin import credentials
import os


class DbConfig:

    def __init__(self):
        self.dirname = os.path.dirname(__file__)

    def setup_firebase_admin(self):
        try:
            cred = credentials.Certificate(f'{self.dirname}\\firebase_admin_credentials.json')
            firebase_admin.initialize_app(cred)
            print('Firebase admin connected')
        except FileNotFoundError:
            print('Wrong firebase credentials location')
