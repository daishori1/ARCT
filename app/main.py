from fastapi import FastAPI
from app.core.db import engine
from sqlmodel import SQLModel
from app.routes.students import router as students_router




app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(students_router)