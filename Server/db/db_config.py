import firebase_admin
from firebase_admin import credentials
import os

dirname = os.path.dirname(__file__)

try:
    cred = credentials.Certificate(
        f'{dirname}\\firebase_admin_credentials.json')
    firebase_admin.initialize_app(cred)
    print('Firebase admin connected')
except FileNotFoundError:
    print('Wrong firebase credentials location')
