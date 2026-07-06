from fastapi import FastAPI
from database import db
from routes.auth import router as auth_router

app = FastAPI(title="SmartExpense API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "SmartExpense API is running"}