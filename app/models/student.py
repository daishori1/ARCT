from sqlmodel import Field , SQLModel 


class Student(SQLModel,table = True):
    __tablename__ = "studentscores" 
    id: int | None = Field(default=None , primary_key=True)
    name : str  = Field(index=True) 
    score : int | None = Field(default=None)
    status : str =  Field(default="active")