from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET = os.getenv("JWT_SECRET")
ALGO = os.getenv("JWT_ALGORITHM")
EXPIRE = int(os.getenv("JWT_EXPIRE_MINUTES"))




def hash_password(p):
    return pwd_context.hash(p)


def verify_password(p, h):
    return pwd_context.verify(p, h)


def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=EXPIRE)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)