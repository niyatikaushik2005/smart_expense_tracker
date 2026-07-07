from fastapi import APIRouter, HTTPException, Depends
from models.expense import ExpenseCreate
from database import expense_collection
from utils.auth_middleware import get_current_user
from datetime import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends, Request
router = APIRouter()

@router.post("/add")
def add_expense(expense: ExpenseCreate, user_id: str = Depends(get_current_user)):
    new_expense = {
        "user_id": user_id,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date or datetime.utcnow().strftime("%Y-%m-%d"),
        "description": expense.description or ""
    }
    result = expense_collection.insert_one(new_expense)
    return {"message": "Expense added", "id": str(result.inserted_id)}

@router.get("/")
def get_expenses(user_id: str = Depends(get_current_user)):
    expenses = list(expense_collection.find({"user_id": user_id}))
    for e in expenses:
        e["_id"] = str(e["_id"])
    return expenses

@router.delete("/{expense_id}")
def delete_expense(expense_id: str, user_id: str = Depends(get_current_user)):
    result = expense_collection.delete_one({
        "_id": ObjectId(expense_id),
        "user_id": user_id
    })
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted"}