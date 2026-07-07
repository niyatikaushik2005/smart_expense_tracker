from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: Optional[str] = None
    description: Optional[str] = None