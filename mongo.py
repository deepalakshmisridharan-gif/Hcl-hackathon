from motor.motor_asyncio import AsyncIOMotorClient
from config.config import settings

client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.MONGO_DB]
customers_collection = db.get_collection("customers")
accounts_collection = db.get_collection("accounts")