import pymongo, os
from bot import DB_URL, DB_NAME


dbclient = pymongo.MongoClient(DB_URL)
database = dbclient[DB_NAME]


shanks = database["shanks"]

async def present_token(user_id : int):
    found = shanks.find_one(
        {"_id": user_id},
        {"$set": {"token": token, "expires_at": expiration_time}},
        upsert=True
    )
    return bool(found)
    
async def add_token(user_id: int):
    shanks.insert_one(
        {"_id": user_id},
        {"$set": {"token": token, "expires_at": expiration_time}},
        upsert=True
    )
    return
