import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Tariff(Base):
    __tablename__ = "tariff"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    plan: Mapped[str] = mapped_column(String, nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)

    # Связь с пользователями
    user: Mapped[list["User"]] = relationship(back_populates="tariff")


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, default=datetime.datetime.now)
    tariff_id: Mapped[int] = mapped_column(Integer, ForeignKey("tariff.id"))

    # Связь с тарифами
    tariff: Mapped[Tariff] = relationship(back_populates="user")

# metadata = MetaData()
#
# tariffs = Table(
#     'tariffs',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('plan', String, nullable=False),
#     Column('permissions', JSON),
# )
#
# users = Table(
#     'users',
#     metadata,
#     Column('id', Integer, primary_key=True),
#     Column('email', String, nullable=False),
#     Column('username', String, nullable=False),
#     Column('password', String, nullable=False),
#     Column('registered_at', TIMESTAMP, default=datetime.datetime.now),
#     Column('tariff', Integer, ForeignKey('tariffs.id')),
# )
