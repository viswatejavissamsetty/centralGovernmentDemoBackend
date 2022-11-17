from fastapi import APIRouter, HTTPException, status

from models.user import User, UserPost, UpdateUser, LoginUser
from config.db import userDb
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user = APIRouter()


@user.get("/users")
async def find_all_users():
    return usersEntity(userDb.find())


@user.get("/user/{id}")
async def find_one_user(id):
    return userEntity(userDb.find_one({"_id": ObjectId(id)}))


@user.post("/user")
async def register_user(user: UserPost):
    if (user.password != user.confirmPassword):
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Password didnot matched"
        )
    if userDb.find_one({"email": user.email}):
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Existing email id unable to register"
        )
    newUser = User(**dict(user))
    a = userDb.insert_one(dict(newUser))
    created_user = userDb.find_one({"_id": a.inserted_id})
    return userEntity(created_user)


@user.post("/user/login")
async def login_user(login: LoginUser):
    user = userDb.find_one(
        {
            "email": login.email,
            "password": login.password
        }
    )
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Invalid User Id or Password")
    return userEntity(user)["_id"]


@user.patch("/user/update-profile/{id}")
async def update_user_profile(id, user: UpdateUser):
    userDb.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(user)
        }
    )
    return userEntity(userDb.find_one({"_id": ObjectId(id)}))
