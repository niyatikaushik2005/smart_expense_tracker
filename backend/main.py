from fastapi import FastAPI
from fastapi.security import HTTPBearer
from database import db
from routes.auth import router as auth_router
from routes.expenses import router as expense_router

security = HTTPBearer()

app = FastAPI(title="SmartExpense API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(expense_router, prefix="/expenses", tags=["Expenses"])

@app.get("/")
def root():
    return {"message": "SmartExpense API is running"}