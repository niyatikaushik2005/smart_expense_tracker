from pymongo import MongoClient 
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
db = client["smartexpense"]
user_collection = db["users"]
expense_collection = db["expenses"]