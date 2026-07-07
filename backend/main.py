from fastapi import FastAPI
from fastapi.security import HTTPBearer
from database import db
from routes.auth import router as auth_router
from routes.expenses import router as expense_router
from routes.analytics import router as analytics_router

security = HTTPBearer()

app = FastAPI(title="SmartExpense API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(expense_router, prefix="/expenses", tags=["Expenses"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
app.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"]
)

@app.get("/")
def root():
    return {"message": "SmartExpense API is running"}