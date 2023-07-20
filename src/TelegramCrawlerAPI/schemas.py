import datetime
from pydantic import BaseModel

class Channel(BaseModel):
    id: int
    username: str
    title: str
    date: datetime.datetime

class Connection(BaseModel):
    id_origin: int
    id_destination: int
    strength: int
    type: int