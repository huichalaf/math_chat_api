import pymongo
import sys
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

db_user = os.getenv("MONGODB_USER")
db_password = os.getenv("MONGODB_PASSWORD")
base_token = os.getenv("TOKEN_MATH")

try:
    client = pymongo.MongoClient(f"mongodb+srv://{db_user}:{db_password}@serverlessinstance0.oo6ew3r.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
except pymongo.errors.ConfigurationError:
    print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
    sys.exit(1)

db = client.test
collection1 = os.getenv("MONGODB_COLLECTION1")
collection2 = os.getenv("MONGODB_COLLECTION2")
collection3 = os.getenv("MONGODB_COLLECTION3")
collection4 = os.getenv("MONGODB_COLLECTION4")
collection5 = os.getenv("MONGODB_COLLECTION5")
collection6 = os.getenv("MONGODB_COLLECTION6")
tokens = db[collection1]
stats = db[collection2]
status = db[collection3]
chats = db[collection4]
files = db[collection5]
documents = db[collection6]

#--------------------auth-------------------------#
async def auth_user(user, token):
    global tokens
    if (token == base_token):
        return True
    response = tokens.find_one({"email": user})
    if response == None:
        return False
    if response['token'] != token:
        return False
    return True

#----------------stats------------------------#
async def get_stats(user):
    global stats
    response = stats.find_one({"email": user})
    if response == None:
        return False
    return response

async def add_tokens_usage(user, tokens_usage):
    global stats
    response = stats.find_one({"email": user})
    if response == None:
        return False
    stats.update_one({"email": user}, {"$set": {"a_tokens": tokens_usage}})
    return True

async def get_a_tokens(user):
    global stats
    response = stats.find_one({"email": user})
    if response == None:
        return False
    return response['a_tokens']