import time
import pymongo, os
from bot import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']
collection = database['premium-users']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
    
async def set_apply_caption(self, id, apply_caption):
  await col.update_one({'id': id}, {'$set': {'apply_caption': apply_caption}})
        
async def get_apply_caption(self, id):
  user = await col.find_one({'id': int(id)})
  return user.get('apply_caption', True)      
        
async def set_upload_as_doc(self, id, upload_as_doc):
  await col.update_one({'id': id}, {'$set': {'upload_as_doc': upload_as_doc}})

async def get_upload_as_doc(self, id):
  user = await col.find_one({'id': int(id)})
  return user.get('upload_as_doc', False)

async def set_thumbnail(self, id, thumbnail):
  await col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})
        

async def get_thumbnail(self, id):
  user = await col.find_one({'id': int(id)})
  return user.get('thumbnail', None)

async def set_caption(self, id, caption):
  await col.update_one({'id': id}, {'$set': {'caption': caption}})
        
async def get_caption(self, id):
  user = await col.find_one({'id': int(id)})
  return user.get('caption', None)    
        
async def get_user_data(self, id) -> dict:
  user = await col.find_one({'id': int(id)})
  return user or None     
        
async def add_premium(user_id, time_limit_months):
    expiration_timestamp = int(time.time()) + time_limit_months * 30 * 24 * 60 * 60
    premium_data = {
        "user_id": user_id,
        "expiration_timestamp": expiration_timestamp,
    }
    collection.insert_one(premium_data)
    dbclient.close()

async def remove_premium(user_id):
    result = collection.delete_one({"user_id": user_id})
    dbclient.close()

async def remove_expired_users():
  
  current_timestamp = int(time.time())
  
  # Find and delete expired users
  expired_users = collection.find({"expiration_timestamp": {"$lte": current_timestamp}})
    
  for expired_user in expired_users:
    user_id = expired_user["user_id"]
    collection.delete_one({"user_id": user_id})   
    
  dbclient.close()

async def list_premium_users():
  premium_users = collection.find({})

  
  premium_user_list = []

  for user in premium_users:
    user_id = user["user_id"]
    user_info = Bot.get_users(user_id)
    username = user_info.username if user_info.username else user_info.first_name
    expiration_timestamp = user["expiration_timestamp"]
    premium_user_list.append(f"{user_id} - {username} - Expiration Timestamp: {expiration_timestamp}")

  return premium_user_list
