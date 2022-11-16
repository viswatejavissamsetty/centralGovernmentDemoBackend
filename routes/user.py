from fastapi import APIRouter, HTTPException, status

from models.user import User, UserPost
from config.db import conn
from schemas.user import serializeDict, serializeList
from bson import ObjectId

user = APIRouter()


@user.get("/")
async def find_all_users():
    return serializeList(conn.fastApiTest.user.find())


@user.get("/{id}")
async def find_one_user(id):
    return serializeDict(conn.fastApiTest.user.find_one({"_id": ObjectId(id)}))


@user.post("/")
async def create_user(user: UserPost):
    if (user.password != user.confirmPassword):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Password didnot matched")
    newUser = User(**dict(user))
    conn.fastApiTest.user.insert_one(dict(newUser))
    return serializeList(conn.fastApiTest.user.find())


@user.put("/{id}")
async def update_user(id, user: User):
    conn.fastApiTest.user.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(user)
        }
    )
    return serializeDict(conn.fastApiTest.user.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}")
async def delete_user(id, user: User):
    return serializeDict(conn.fastApiTest.user.find_one_and_delete(
        {
            "_id": ObjectId(id)
        }
    ))
