import datetime
from pydantic import BaseModel


class Channel(BaseModel):
    id: int
    username: str
    title: str
    date: datetime.datetime

    # @validator(date, pre=True)
    # def date_validate(cls, date):
    #     return datetime.datetime.fro


class ConnectionBase(BaseModel):
    id_origin: int
    id_destination: int
    strength: int


class Connection(ConnectionBase):
    type: int = 1


class ConnectionCreate(ConnectionBase):
    date: datetime.datetime


class Queue(BaseModel):
    id: int


class QueueCreate(Queue):
    date: datetime.datetime


class Success(BaseModel):
    ok: bool
    details: str | None = None
