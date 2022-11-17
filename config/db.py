from pymongo import MongoClient

__conn = MongoClient("mongodb+srv://cgtest1:cgtest1@cluster0.5m0ckdy.mongodb.net/test")

userDb = __conn.fastApiTest.user