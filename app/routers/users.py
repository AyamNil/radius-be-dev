from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from ..database import get_db
from ..deps import get_current_admin
from ..models import RadCheck, RadUserGroup, AuditLog
from ..security import hash_password


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(data: dict, request: Request,db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):

    db.add(RadCheck(
    username=data["username"],
    attribute="Crypt-Password",
    op=":=",
    value=hash_password(data["password"])
    ))


    db.add(RadUserGroup(
    username=data["username"],
    groupname=data["group"],
    priority=1
    ))


    db.add(AuditLog(
    admin_username=admin,
    action="CREATE_USER",
    target=data["username"],
    details=f"Group={data['group']}",
    ip_address=request.client.host
    ))


    db.commit()
    return {"status": "created"}