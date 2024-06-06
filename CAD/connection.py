import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("CAD\call-a-doctor-bbd15-firebase-adminsdk-pfmoy-2b811d48ca.json")
firebase_admin.initialize_app(cred)

ref = db.reference('/')
