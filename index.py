from fastapi import FastAPI
from routes.user import user

app = FastAPI(title="Test project")
app.include_router(user)