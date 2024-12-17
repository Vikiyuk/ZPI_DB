from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["zpi-db"]
document1 = {
    "image": "base64_lub_url_do_zdjecia",
    "diseases": [
        {"name": "Choroba 1", "description": "Opis choroby 1"},
        {"name": "Choroba 2", "description": "Opis choroby 2"},
        {"name": "Choroba 3", "description": "Opis choroby 3"}
    ]
}
db.diseases.insert_one(document1)
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