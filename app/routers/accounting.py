from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..deps import get_current_admin
from ..models import RadAcct


router = APIRouter(prefix="/accounting", tags=["Accounting"])


@router.get("/active")
def active(db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    return db.query(RadAcct).filter(RadAcct.acctstoptime == None).all()