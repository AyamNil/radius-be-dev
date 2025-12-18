from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..deps import get_current_admin
from ..models import AuditLog


router = APIRouter(prefix="/audit", tags=["Audit"])


@router.get("/")
def list_logs(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()