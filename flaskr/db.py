from sqlmodel import SQLModel, create_engine, Field
from typing import Optional

engine = create_engine('sqlite:///flaskr.sqlite', convert_unicode=True)

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: Optional[str] = Field(default=None, unique=True)
    email: Optional[str] = Field(default=None, unique=True)
    password: Optional[str] = Field(default=None)

def init_db():
    SQLModel.metadata.create_all(engine)