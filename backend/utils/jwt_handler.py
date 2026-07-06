import jwt
import os
from datetime import timedelta,datetime
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM="HS256"
TOKEN_EXPIRY_HOURS=24

def create_token(user_id:str):
    payload={
        "sub":user_id,
        "exp":datetime.utcnow() + timedelta(hours=TOKEN_EXPIRY_HOURS)

    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token : str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
