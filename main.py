from pymongo import MongoClient

def dbconnect():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["pdbc"]
        users = db["users"]
        print("Connection Established")
        return users
    except Exception as e:
        print(f"Connection failed: {e}")
        return None
dbconnect()