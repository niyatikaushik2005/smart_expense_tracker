from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from database import db
from routes.auth import router as auth_router
from routes.expenses import router as expense_router
from routes.analytics import router as analytics_router

security = HTTPBearer()

app = FastAPI(title="SmartExpense API")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://smart-expense-tracker-lxtjsnakn-niyati-kaushiks-projects.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(expense_router, prefix="/expenses", tags=["Expenses"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])


@app.get("/")
def root():
    return {"message": "SmartExpense API is running"}