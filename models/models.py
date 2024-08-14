import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

tariffs = Table(
    'tariffs',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('plan', String, nullable=False),
    Column('permissions', JSON),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.datetime.now),
    Column('tariff', Integer, ForeignKey('tariffs.id')),
)
