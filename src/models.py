# Imports
from sqlalchemy import ForeignKey, Integer, Sequence, DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .database import Base


class TelegramChannel(Base):
    __tablename__ = "TelegramChannels"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    username: Mapped[str] = mapped_column(String(32))
    date: Mapped[str] = mapped_column(DateTime())

    def __repr__(self) -> str:
        return f"Channel(id={self.id!r}, username={self.username!r}, title={self.title!r}, description={self.description!r}, subscribers={self.subscribers!r}, posts={self.posts!r})"


class TelegramConnection(Base):
    __tablename__ = "TelegramConnections"

    id: Mapped[int] = mapped_column(Sequence("id", start=1), primary_key=True)
    id_origin: Mapped[int] = mapped_column(ForeignKey("TelegramChannels.id"))
    id_destination: Mapped[int] = mapped_column(ForeignKey("TelegramChannels.id"))

    strength: Mapped[int] = mapped_column(Integer())
    type: Mapped[int] = mapped_column(Integer())


class TelegramQueue(Base):
    __tablename__ = "TelegramQueue"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[str] = mapped_column(DateTime())
