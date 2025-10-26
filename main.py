from fastapi import FastAPI
from fastapi import APIRouter
from routes.accounts import router as accounts_router
from pymongo import MongoClient


app = FastAPI()
@app.on_event("startup")
async def startup_event():
    print("Connected to MongoDB")
app.include_router(accounts_router)


