from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/hangman_pokemon')

try:
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Connection failed: {e}")