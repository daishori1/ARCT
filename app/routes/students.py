from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.db import get_session
from app.models.student import Student

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/")
def get_students(session: Session = Depends(get_session)):
    students = session.exec(select(Student)).all()
    return students
