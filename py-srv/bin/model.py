from typing import Optional

from sqlmodel import Field, SQLModel

class Dog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    breed: str
    color: str

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def __repr__(self):
        return "<Dog('%s', '%s')>" % (self.breed, self.color)