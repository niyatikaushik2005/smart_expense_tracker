from fastapi import APIRouter, HTTPException
from models.user import UserRegister,UserLogin
from database import user_collection
from passlib.context import CryptContext
from utils.jwt_handler import create_token
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(user: UserRegister):
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
@router.post("/login")
def login(user: UserLogin):
    existing_user = user_collection.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Email not found")
    
    if not pwd_context.verify(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    token = create_token(str(existing_user["_id"]))
    return {"token": token, "message": "Login successful"}
   
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }
    result = user_collection.insert_one(new_user)
    
    token = create_token(str(result.inserted_id))
    return {"token": token, "message": "User registered successfully"}