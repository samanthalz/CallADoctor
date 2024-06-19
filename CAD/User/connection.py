import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCjcxpIIgo_q8LBGDAbnRa_L1KqERK_MoE",
  "authDomain": "call-a-doctor-bbd15.firebaseapp.com",
  "databaseURL": "https://call-a-doctor-bbd15-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "call-a-doctor-bbd15",
  "storageBucket": "call-a-doctor-bbd15.appspot.com",
  "messagingSenderId": "842962802742",
  "appId": "1:842962802742:web:6d101eb20889e082cba097",
  "measurementId": "G-XMR0QXNPJV"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()