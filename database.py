# database.py

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["BoldConverterBot"]

users = db["users"]
sequences = db["sequences"]


# ===========================
# User Style
# ===========================

async def set_user_style(user_id: int, style: str):
    await users.update_one(
        {"_id": user_id},
        {"$set": {"style": style}},
        upsert=True
    )


async def get_user_style(user_id: int):
    user = await users.find_one({"_id": user_id})

    if not user:
        return "bold"

    return user.get("style", "bold")


# ===========================
# Sequence
# ===========================

async def start_sequence(user_id: int):
    await sequences.update_one(
        {"_id": user_id},
        {"$set": {"files": []}},
        upsert=True
    )


async def add_to_sequence(user_id: int, chat_id: int, message_id: int):
    await sequences.update_one(
        {"_id": user_id},
        {
            "$push": {
                "files": {
                    "chat_id": chat_id,
                    "message_id": message_id
                }
            }
        },
        upsert=True
    )


async def get_sequence(user_id: int):
    data = await sequences.find_one({"_id": user_id})

    if not data:
        return []

    return data.get("files", [])


async def clear_sequence(user_id: int):
    await sequences.delete_one({"_id": user_id})
