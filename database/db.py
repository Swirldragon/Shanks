from pymongo import MongoClient
import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bot import DB_URL

mongo_client = MongoClient(DB_URL)
database = mongo_client.userdb.sessions

class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            apply_caption=True,
            upload_as_doc=False,
            thumbnail=None,
            caption=None
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
         user_ids = []
         async for doc in self.db.users.find({}): # Assuming 'users' is your collection name
             user_docs.append(doc)
             
         return user_ids

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_apply_caption(self, id, apply_caption):
        await self.col.update_one({'id': id}, {'$set': {'apply_caption': apply_caption}})

    async def get_apply_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('apply_caption', True)

    async def set_mode(self, id, upload_as_doc):
        await self.col.update_one({'id': id}, {'$set': {'upload_as_doc': upload_as_doc}})

    async def get_mode(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('upload_as_doc', False)

    async def set_thumbnail(self, id, thumbnail):
        await self.col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('thumbnail', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'id': id}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('caption', None)
   
    async def set_mega_email(self, id, megaemail):
        await self.col.update_one({'id': id}, {'$set': {'megaemail': megaemail}})
        
    async def get_mega_email(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('megaemail', None)
        
    async def set_mega_password(self, id, megapawword):
        await self.col.update_one({'id': id}, {'$set': {'megapassword': megapassword}})
        
    async def get_mega_password(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('megapawword', None)
        
    async def set_auto(self, id, auto):
        await self.col.update_one({'id': id}, {'$set': {'auto': auto}})
        
    async def get_auto(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('auto', None)
        
    async def get_user_data(self, id) -> dict:
        user = await self.col.find_one({'id': int(id)})
        return user or None


db = Database(DB_URL, "Cluster0")
