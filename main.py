from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["zpi-db"]
document1 = {
            "name": "Choroba 1",
            "description": "Opis choroby 1",
            "image": "base64_lub_url_do_zdjecia_1"
        }
document12 ={
            "name": "Choroba 2",
            "description": "Opis choroby 2",
            "image": "base64_lub_url_do_zdjecia_2"
        }

document13 ={
            "name": "Choroba 3",
            "description": "Opis choroby 3",
            "image": "base64_lub_url_do_zdjecia_3"
        }

db.diseases.insert_one(document1)
db.diseases.insert_one(document12)
db.diseases.insert_one(document13)

document2 = {
    "diagnosis_id": "diag123",
    "diagnosis_name": "Przykładowa diagnoza",
    "date": datetime.utcnow()
}
db.diagnoses.insert_one(document2)
document2 = {
    "diagnosis_id": "diag124",
    "diagnosis_name": "Przykładowa diagnoza",
    "date": datetime.utcnow()
}
db.diagnoses.insert_one(document2)