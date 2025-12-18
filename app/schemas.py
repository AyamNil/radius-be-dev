from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# ---------- AUTH ----------
class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ---------- USERS ----------
class UserCreate(BaseModel):
    username: str
    password: str
    group: str
    expiration: Optional[datetime] = None


class UserOut(BaseModel):
    username: str
    group: str


# ---------- ACCOUNTING ----------
class ActiveSession(BaseModel):
    username: str
    acctstarttime: datetime
    nasipaddress: Optional[str]


# ---------- AUDIT ----------
class AuditLogOut(BaseModel):
    admin_username: str
    action: str
    target: Optional[str]
    details: Optional[str]
    created_at: datetime