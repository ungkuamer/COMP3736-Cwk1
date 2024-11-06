import firebase_admin
from firebase_admin import firestore

app = firebase_admin.initialize_app()
db = firestore.client()

'''
dummy_data = {"q1":{"answer":True,"res_time":0.053,"type":1},"q2":{"answer":False,"time":2.432,"type":1}}
doc_ref = db.collection("participants").add(dummy_data)

print("Data added successfully with ID: ", doc_ref[1].id)
'''
