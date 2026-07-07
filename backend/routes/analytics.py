from fastapi import APIRouter, Depends
from database import expense_collection
from utils.auth_middleware import get_current_user
from collections import defaultdict

router = APIRouter()

@router.get("/summary")
def get_summary(user_id: str = Depends(get_current_user)):
    expenses = list(expense_collection.find({"user_id": user_id}))
    
    total = sum(e["amount"] for e in expenses)
    
    by_category = defaultdict(float)
    by_month = defaultdict(float)
    
    for e in expenses:
        by_category[e["category"]] += e["amount"]
        month = e["date"][:7]  # "2026-07"
        by_month[month] += e["amount"]
    
    return {
        "total_spent": total,
        "by_category": dict(by_category),
        "by_month": dict(by_month),
        "total_expenses": len(expenses)
    }