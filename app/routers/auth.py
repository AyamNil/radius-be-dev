from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..security import verify_password, create_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    row = db.execute(
    "SELECT username, password_hash FROM admin_users WHERE username=:u AND is_active=true",
    {"u": data["username"]}
    ).fetchone()


    if not row or not verify_password(data["password"], row.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_token(row.username), "token_type": "bearer"}