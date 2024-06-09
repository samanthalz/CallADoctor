import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('CAD\call-a-doctor-bbd15-firebase-adminsdk-pfmoy-2b811d48ca.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://console.firebase.google.com/u/1/project/call-a-doctor-bbd15/database/call-a-doctor-bbd15-default-rtdb/data/~2F'
})

# Get a reference to the Firebase Realtime Database
db_ref = db.reference('/')
