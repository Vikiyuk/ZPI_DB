from pymongo import MongoClient, ASCENDING
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["zpi-db"]
disease_documents = [
    {"name": "Choroba 1", "description": "Opis choroby 1", "image": "base64_lub_url_do_zdjecia_1"},
    {"name": "Choroba 2", "description": "Opis choroby 2", "image": "base64_lub_url_do_zdjecia_2"},
    {"name": "Choroba 3", "description": "Opis choroby 3", "image": "base64_lub_url_do_zdjecia_3"},
]

try:
    db.diseases.insert_many(disease_documents, ordered=False)
except Exception as e:
    print(f"Error inserting diseases: {e}")


diagnosis_documents = [
    {"diagnosis_id": "diag123", "diagnosis_name": "Przykładowa diagnoza", "date": datetime.utcnow()},
    {"diagnosis_id": "diag124", "diagnosis_name": "Przykładowa diagnoza", "date": datetime.utcnow()},
]

try:
    db.diagnoses.insert_many(diagnosis_documents, ordered=False)
except Exception as e:
    print(f"Error inserting diagnoses: {e}")

db.diagnoses.create_index([("diagnosis_id", ASCENDING)], unique=True)