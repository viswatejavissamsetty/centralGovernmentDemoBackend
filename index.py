from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user

app = FastAPI(title="Test project")

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user)